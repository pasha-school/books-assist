---
type: book
title: "Уроки французского"
author: "Валентин Распутин"
read_through: 1
started_on: 2026-07-12
finished_on: null
tags: [book]
---

# Уроки французского

**Автор:** Валентин Распутин

## Прогресс

- Прочитано до главы: `= this.read_through`
- Начали: `= this.started_on`

## Главы

```dataview
TABLE number AS "№", title AS "Название", read_on AS "Прочитано"
FROM "Книги/Уроки французского - Распутин/Главы"
WHERE type = "chapter"
SORT number ASC
```

## Персонажи

```dataview
TABLE first_appears_in AS "Появился", length(relations) AS "Связей"
FROM "Книги/Уроки французского - Распутин/Персонажи"
WHERE type = "character"
SORT first_appears_in ASC
```

## Места

```dataview
TABLE first_appears_in AS "Появилось"
FROM "Книги/Уроки французского - Распутин/Места"
WHERE type = "location"
SORT first_appears_in ASC
```

## События

```dataview
TABLE chapter AS "Глава", location AS "Место", participants AS "Участники"
FROM "Книги/Уроки французского - Распутин/События"
WHERE type = "event"
SORT chapter ASC, order ASC
```
