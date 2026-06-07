# Rule: schema

Фиксированная схема frontmatter. **Не вводи новые поля без явного запроса пользователя.**

## character

```yaml
---
type: character
book: "[[<Название книги>]]"
aliases: []                    # альтернативные имена/прозвища
age: null                      # null | число | строка ("около 7")
first_appears_in: "[[Глава-01]]"
appears_in: ["[[Глава-01]]"]
relations:
  - {to: "[[<Персонаж>]]", type: "<тип связи>", since: "[[Глава-NN]]", confidence: high}
tags: [character]
---
```

## location

```yaml
---
type: location
book: "[[<Название книги>]]"
parent: null                   # null | "[[<Объемлющее место>]]"
real_world: false              # true, если реальное место (тогда Yandex Geocoder опционально)
first_appears_in: "[[Глава-01]]"
appears_in: ["[[Глава-01]]"]
tags: [location]
---
```

## event

```yaml
---
type: event
book: "[[<Название книги>]]"
chapter: "[[Глава-01]]"
order: 1                       # порядковый номер события внутри главы
participants: ["[[<Персонаж>]]"]
location: "[[<Место>]]"
date: null                     # null | "in-story дата"
tags: [event]
---
```

## chapter

```yaml
---
type: chapter
book: "[[<Название книги>]]"
number: 1
title: "<Заголовок главы>"
read_on: null                  # YYYY-MM-DD, когда прочитали
new_characters: []
new_locations: []
new_events: []
tags: [chapter]
---
```

## book (index.md)

```yaml
---
type: book
title: "<Название>"
author: "<Автор>"
read_through: 0                # последняя ПОЛНОСТЬЮ прочитанная глава (используется для anti-spoiler)
started_on: null
finished_on: null
tags: [book]
---
```

## concept (опционально)

```yaml
---
type: concept
book: "[[<Название книги>]]"
appears_in: []
tags: [concept]
---
```

## Inline-поля Dataview (для подписей связей)

В теле заметки персонажа дублируй связи как inline-поля — это делает их видимыми для Dataview-запросов и для подписей рёбер в Extended Graph:

```
- отец :: [[Иван Петрович]]
- враг :: [[Долохов]]
```

Это **дублирует** `relations` из frontmatter — frontmatter источник истины, inline — для визуализации.

## Типы связей (контролируемый словарь)

Используй короткие, понятные ребёнку слова. Базовый набор:

- семейные: `отец`, `мать`, `сын`, `дочь`, `брат`, `сестра`, `муж`, `жена`, `дед`, `бабушка`
- социальные: `друг`, `знакомый`, `сосед`, `учитель`, `ученик`, `начальник`, `слуга`
- сюжетные: `враг`, `соперник`, `союзник`, `спаситель`, `жертва`, `любит`, `боится`
- ситуативные: `встретил`, `помог`, `обманул`, `спас`, `ищет`

Если нужного типа нет — выбери ближайший, а спорный случай помечай `confidence: low`.
