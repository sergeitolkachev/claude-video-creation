# Голоса канала (ElevenLabs)

Оба голоса созданы через Voice Design и существуют только в аккаунте проекта.
В Voice Library они не публикуются и не могут быть опубликованы — шарить туда
можно только Professional Voice Clones.

> При потере голоса точную копию восстановить нельзя: Voice Design каждый раз
> даёт новый результат. Описания ниже — только отправная точка для повторной
> генерации.

---

## Narrator — mockumentary

- **voice_id:** `tdl2YAu4Nj41holo8yUO`
- **Роль:** закадровый диктор псевдодокументальных эпизодов
- **Акцент:** американский

**voice_description:**

```
A man in his early fifties with a neutral American accent. Measured, unhurried
pace with deliberate pauses. Dry, restrained delivery — an archivist reading
case notes aloud, not a storyteller. Warm mid-range timbre, slight gravel,
minimal emotional inflection. Sounds like he believes every word and expects
you to as well.
```

**Референсный текст для тестов:**

```
Reel four was recovered in nineteen seventy-eight, roughly forty kilometers
from the original survey camp. The audio track is intact. The visual track is
not. What follows is a transcript, read here for the first time. We have made
no corrections to the record. Where the speaker is inaudible, we have marked
the gap and moved on.
```

**Настройки синтеза** (заполнить после калибровки):

| Параметр | Значение |
| --- | --- |
| model_id | |
| stability | |
| similarity_boost | |
| style | |
| speed | |
| use_speaker_boost | |

---

## Character — found footage

- **voice_id:** `EiVTLiipxYldU5SJvo5d`
- **Роль:** голос персонажа, записывающего себя на камеру
- **Акцент:** американский

**voice_description:**

```
A man in his late twenties, neutral American accent. Speaks in uneven bursts —
fast when startled, then trailing off. Audible breath between phrases, slightly
strained upper register, conversational and unpolished. He is recording
himself, talking to a camera he is holding, not performing for an audience.
```

**Референсный текст для тестов:**

```
Okay. Okay, I'm recording. It's — I don't know, past two, the phone died so I'm
going off the camera clock. I went back to the fence line like we said and it's
not there anymore. The whole section. I'm not saying somebody moved it, I'm
saying there's nothing in the ground where it was. Just tell me you're getting
this.
```

**Настройки синтеза** (заполнить после калибровки):

| Параметр | Значение |
| --- | --- |
| model_id | |
| stability | |
| similarity_boost | |
| style | |
| speed | |
| use_speaker_boost | |

---

## Правила

- Настройки синтеза фиксируются один раз и не меняются между эпизодами —
  разброс слышен и ломает ощущение единого канала.
- Мелкие правки голоса делать через `POST /v1/text-to-voice/{voice_id}/remix`,
  а не новой генерацией с нуля.
- Эталонные сэмплы озвучки держать в репозитории рядом с этим файлом, чтобы
  было с чем сравнивать при подозрении на дрейф.
