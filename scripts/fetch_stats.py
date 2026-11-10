#!/usr/bin/env python3
"""Channel statistics — read-only pull from the YouTube Data and Analytics APIs.

Writes analytics/<date>/videos.json (one row per upload: title, length, views,
watch time, average view duration and percentage, subscribers gained, traffic
sources) and analytics/<date>/retention/<video_id>.csv (the 100-point audience
retention curve). Retention is the reason this exists: laid over a record's
shots.yaml it shows where viewers leave — a pause, a card, the cold open.

Impressions and thumbnail CTR are not in the API. Export them from Studio by
hand if needed.

First run opens a browser for consent; the token is kept in .keys/, which is
not versioned.

Usage: fetch_stats.py [--since 2025-01-01]
"""
import sys, json, csv, glob, datetime, pathlib

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from googleapiclient.discovery import build

print = __import__('functools').partial(print, flush=True)

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEYS = ROOT / ".keys"
TOKEN = KEYS / "youtube-token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/yt-analytics.readonly"]
METRICS = ("views,estimatedMinutesWatched,averageViewDuration,"
           "averageViewPercentage,subscribersGained,likes,comments")


def creds():
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES) if TOKEN.exists() else None
    if c and c.valid:
        return c
    if c and c.expired and c.refresh_token:
        try:
            c.refresh(Request())
        except RefreshError:
            # A token issued while the consent screen was in Testing dies
            # after 7 days with invalid_grant; fall through to a new consent.
            c = None
    if not (c and c.valid):
        # A "Web application" client has no localhost redirect and Google
        # answers redirect_uri_mismatch; only a "Desktop app" client works here.
        secret = [f for f in glob.glob(str(KEYS / "client_secret*.json"))
                  if "installed" in json.loads(pathlib.Path(f).read_text())]
        if not secret:
            sys.exit("no Desktop-app client_secret*.json in .keys/")
        c = InstalledAppFlow.from_client_secrets_file(secret[0], SCOPES).run_local_server(port=8080)
    TOKEN.write_text(c.to_json())
    return c


def iso_seconds(d):
    # PT1H2M3S -> 3723
    n, out = "", 0
    for ch in d.removeprefix("PT"):
        if ch.isdigit():
            n += ch
        else:
            out += int(n) * {"H": 3600, "M": 60, "S": 1}[ch]
            n = ""
    return out


def rows(resp):
    cols = [h["name"] for h in resp.get("columnHeaders", [])]
    return [dict(zip(cols, r)) for r in resp.get("rows", [])]


def main():
    since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else "2025-01-01"
    today = datetime.date.today().isoformat()
    c = creds()
    yt = build("youtube", "v3", credentials=c)
    ya = build("youtubeAnalytics", "v2", credentials=c)

    ch = yt.channels().list(part="snippet,contentDetails,statistics", mine=True).execute(num_retries=5)["items"][0]
    print(f"channel: {ch['snippet']['title']}  subs={ch['statistics'].get('subscriberCount')}  "
          f"views={ch['statistics'].get('viewCount')}")
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]

    ids, tok = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=uploads,
                                    maxResults=50, pageToken=tok).execute(num_retries=5)
        ids += [i["contentDetails"]["videoId"] for i in r["items"]]
        tok = r.get("nextPageToken")
        if not tok:
            break

    out = ROOT / "analytics" / today
    (out / "retention").mkdir(parents=True, exist_ok=True)
    videos = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,contentDetails,statistics", id=",".join(ids[i:i + 50])).execute(num_retries=5)
        for v in r["items"]:
            vid = v["id"]
            q = dict(ids="channel==MINE", startDate=since, endDate=today, filters=f"video=={vid}")
            m = rows(ya.reports().query(metrics=METRICS, **q).execute(num_retries=5))
            src = rows(ya.reports().query(metrics="views", dimensions="insightTrafficSourceType",
                                          sort="-views", **q).execute(num_retries=5))
            ret = rows(ya.reports().query(metrics="audienceWatchRatio,relativeRetentionPerformance",
                                          dimensions="elapsedVideoTimeRatio", **q).execute(num_retries=5))
            if ret:
                with open(out / "retention" / f"{vid}.csv", "w", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=list(ret[0]))
                    w.writeheader()
                    w.writerows(ret)
            row = {
                "id": vid,
                "title": v["snippet"]["title"],
                "published": v["snippet"]["publishedAt"],
                "seconds": iso_seconds(v["contentDetails"]["duration"]),
                "public_views": int(v["statistics"].get("viewCount", 0)),
                "analytics": m[0] if m else {},
                "traffic": {s["insightTrafficSourceType"]: s["views"] for s in src},
                "retention_points": len(ret),
            }
            videos.append(row)
            a = row["analytics"]
            print(f"{row['published'][:10]}  {row['seconds']:>4}s  views={a.get('views', '-'):>6}  "
                  f"avg%={a.get('averageViewPercentage', '-')}  ret={len(ret):>3}  {row['title'][:60]}")

    videos.sort(key=lambda r: r["published"])
    (out / "videos.json").write_text(json.dumps(videos, indent=2, ensure_ascii=False))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
