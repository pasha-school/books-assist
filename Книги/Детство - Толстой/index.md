---
type: book
title: "Детство"
author: "Лев Толстой"
read_through: 3
started_on: null
finished_on: null
tags: [book]
---

# Детство

**Автор:** Лев Толстой

## Карта книги

См. [[Карта.canvas|карту книги]] — главные герои, места и ключевые события (обновляется по мере чтения).

## Прогресс

- Прочитано до главы: `= this.read_through`
- Начали: `= this.started_on`

## Главы

```dataview
TABLE number AS "№", title AS "Название", read_on AS "Прочитано"
FROM "Книги/Детство - Толстой/Главы"
WHERE type = "chapter"
SORT number ASC
```

## Персонажи

```dataview
TABLE first_appears_in AS "Появился", length(relations) AS "Связей"
FROM "Книги/Детство - Толстой/Персонажи"
WHERE type = "character"
SORT first_appears_in ASC
```

## Места

```dataview
TABLE first_appears_in AS "Появилось"
FROM "Книги/Детство - Толстой/Места"
WHERE type = "location"
SORT first_appears_in ASC
```

## События

```dataview
TABLE chapter AS "Глава", location AS "Место", participants AS "Участники"
FROM "Книги/Детство - Толстой/События"
WHERE type = "event"
SORT chapter ASC, order ASC
```
