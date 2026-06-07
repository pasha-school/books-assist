#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для разбиения книги "Дубровский - Пушкин" на главы по томам
"""

import os
import re
from pathlib import Path

def read_book_file():
    """Читает исходный файл книги"""
    book_path = "Книги/Дубровский - Пушкин/Пушкин - Дубровский.md"
    with open(book_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_chapters(text):
    """Разбирает текст на главы и тома"""
    # Находим все маркеры глав и томов
    chapter_pattern = r'(ГЛАВА [IVX1-9]+[\.,]?)'
    volume_pattern = r'\* ТОМ ([А-Я]+) \*'

    # Находим все позиции глав
    chapter_matches = list(re.finditer(chapter_pattern, text))

    # Находим позиции томов
    volume_matches = list(re.finditer(volume_pattern, text))

    chapters = []

    # Обрабатываем каждую главу
    for i, match in enumerate(chapter_matches):
        chapter_title = match.group(1).strip()
        start_pos = match.start()

        # Определяем конец главы (начало следующей главы или конец файла)
        if i < len(chapter_matches) - 1:
            end_pos = chapter_matches[i + 1].start()
        else:
            end_pos = len(text)

        # Определяем том для этой главы
        current_volume = "ПЕРВЫЙ"  # по умолчанию
        for vol_match in volume_matches:
            if vol_match.start() < start_pos:
                current_volume = vol_match.group(1)

        chapter_text = text[start_pos:end_pos].strip()

        chapters.append({
            'title': chapter_title,
            'volume': current_volume,
            'text': chapter_text,
            'start_pos': start_pos,
            'end_pos': end_pos
        })

    return chapters

def create_directory_structure():
    """Создает структуру директорий для томов"""
    base_dir = Path("Книги/Дубровский - Пушкин/Главы")

    # Создаем директории для томов
    volume_dirs = {
        "ПЕРВЫЙ": base_dir / "Том I",
        "ВТОРОЙ": base_dir / "Том II"
    }

    for volume_name, volume_dir in volume_dirs.items():
        volume_dir.mkdir(parents=True, exist_ok=True)
        print(f"Создана директория: {volume_dir}")

    return volume_dirs

def create_chapter_file(chapter, volume_dirs, chapter_template):
    """Создает файл для главы"""
    # Нормализуем название главы для имени файла
    chapter_name = chapter['title'].replace(' ', '-').replace('.', '').lower()
    volume_dir = volume_dirs[chapter['volume']]

    # Формируем имя файла
    filename = f"{chapter_name}.md"
    filepath = volume_dir / filename

    # Создаем frontmatter
    frontmatter = f"""---
type: chapter
title: {chapter['title']}
volume: {chapter['volume']}
---

"""

    # Добавляем текст главы
    content = frontmatter + chapter['text']

    # Записываем файл
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Создан файл: {filepath}")
    return filepath

def read_chapter_template():
    """Читает шаблон для главы"""
    template_path = "_agents/templates/chapter.md"
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return """## Краткое содержание

## Что новое появилось

## Обсудить с ребёнком
"""

def main():
    """Основная функция"""
    print("Начинаем разбиение книги на главы...")

    # Читаем исходный текст
    text = read_book_file()
    print(f"Прочитано {len(text)} символов")

    # Разбираем на главы
    chapters = parse_chapters(text)
    print(f"Найдено {len(chapters)} глав")

    # Создаем структуру директорий
    volume_dirs = create_directory_structure()

    # Читаем шаблон главы
    chapter_template = read_chapter_template()

    # Создаем файлы для каждой главы
    created_files = []
    for i, chapter in enumerate(chapters, 1):
        print(f"Обрабатываем главу {i}: {chapter['title']} (Том {chapter['volume']})")
        filepath = create_chapter_file(chapter, volume_dirs, chapter_template)
        created_files.append(filepath)

    print(f"\nГотово! Создано {len(created_files)} файлов глав.")

    # Выводим список созданных файлов
    print("\nСозданные файлы:")
    for filepath in created_files:
        print(f"  - {filepath}")

if __name__ == "__main__":
    main()
