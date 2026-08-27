---
type: book
title: "Дети капитана Гранта"
author: "Жюль Верн"
read_through: 35
started_on: 2026-08-09
finished_on: null
tags: [book]
---

# Дети капитана Гранта

**Автор:** Жюль Верн

## Прогресс

- Прочитано до главы: `= this.read_through`
- Начали: `= this.started_on`

## Главы

```dataview
TABLE number AS "№", title AS "Название", read_on AS "Прочитано"
FROM "Книги/Дети капитана Гранта - Верн/Главы"
WHERE type = "chapter"
SORT number ASC
```

## Персонажи

```dataview
TABLE first_appears_in AS "Появился", length(relations) AS "Связей"
FROM "Книги/Дети капитана Гранта - Верн/Персонажи"
WHERE type = "character"
SORT first_appears_in ASC
```

## Места

```dataview
TABLE first_appears_in AS "Появилось"
FROM "Книги/Дети капитана Гранта - Верн/Места"
WHERE type = "location"
SORT first_appears_in ASC
```

## События

```dataview
TABLE chapter AS "Глава", location AS "Место", participants AS "Участники"
FROM "Книги/Дети капитана Гранта - Верн/События"
WHERE type = "event"
SORT chapter ASC, order ASC
```
