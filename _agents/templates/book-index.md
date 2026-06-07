---
type: book
title: "<Название>"
author: "<Автор>"
read_through: 0
started_on: null
finished_on: null
tags: [book]
---

# <Название>

**Автор:** <Автор>

## Прогресс

- Прочитано до главы: `= this.read_through`
- Начали: `= this.started_on`

## Главы

```dataview
TABLE number AS "№", title AS "Название", read_on AS "Прочитано"
FROM "Книги/<Название>/Главы"
WHERE type = "chapter"
SORT number ASC
```

## Персонажи

```dataview
TABLE first_appears_in AS "Появился", length(relations) AS "Связей"
FROM "Книги/<Название>/Персонажи"
WHERE type = "character"
SORT first_appears_in ASC
```

## Места

```dataview
TABLE first_appears_in AS "Появилось"
FROM "Книги/<Название>/Места"
WHERE type = "location"
SORT first_appears_in ASC
```

## События

```dataview
TABLE chapter AS "Глава", location AS "Место", participants AS "Участники"
FROM "Книги/<Название>/События"
WHERE type = "event"
SORT chapter ASC, order ASC
```
