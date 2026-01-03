# Ruff: быстрый линтер и форматтер для Python

Ruff — это чрезвычайно быстрый инструмент для линтинга и форматирования Python-кода, написанный на Rust. Вот подробное руководство по его использованию:

## Установка

```bash
# Установка через pip
pip install ruff

# Или через pipx (рекомендуется для инструментов)
pipx install ruff

# Проверка установки
ruff --version
```

## Основное использование

### Линтинг (проверка кода)

```bash
# Проверить все файлы в проекте
ruff check .

# Проверить конкретный файл
ruff check path/to/file.py

# Проверить с выводом всех ошибок
ruff check . --verbose

# Автоматическое исправление исправимых ошибок
ruff check . --fix

# Автоматическое исправление с безопасными исправлениями
ruff check . --fix --unsafe-fixes

# Проверить только определенные правила
ruff check . --select E501,W293

# Игнорировать определенные правила
ruff check . --ignore E501,F401
```

### Форматирование кода

```bash
# Проверить форматирование
ruff format --check .

# Отформатировать все файлы
ruff format .

# Отформатировать конкретный файл
ruff format path/to/file.py

# Показать diff без применения изменений
ruff format --diff .
```

## Конфигурация

### Файл `pyproject.toml`

Ruff ищет конфигурацию в `pyproject.toml`, `ruff.toml`, или `.ruff.toml`:

```toml
[tool.ruff]
# Включение/выключение правил
select = ["E", "F", "I"]  # Включить все ошибки (E), нарушения формата (F), нарушения импортов (I)
ignore = ["E501"]         # Игнорировать длину строк

# Настройки линтера
line-length = 88
target-version = "py311"

# Включение/выключение правил по категориям
extend-select = [
    "UP",  # pyupgrade правила
    "B",   # flake8-bugbear
    "S",   # flake8-bandit (безопасность)
]

[tool.ruff.lint]
# Настройка конкретных правил
isort = {known-first-party = ["my_project"]}

[tool.ruff.format]
# Настройки форматтера
indent-style = "space"
quote-style = "double"
```

### Файл `.ruff.toml` (альтернатива)

```toml
# Пример минимальной конфигурации
line-length = 100
select = ["E", "F", "B", "I"]
target-version = "py310"
```

## Интеграция с редакторами

### VS Code

1. Установите расширение "Ruff"
2. Добавьте в `settings.json`:
```json
{
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.ruffEnabled": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": true
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
    }
}
```

### PyCharm/IntelliJ IDEA

1. Установите плагин Ruff
2. Настройки → Tools → Ruff
3. Включите "Run on save"

### Pre-commit hooks

Добавьте в `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6  # Используйте актуальную версию
    hooks:
      # Линтинг
      - id: ruff
        args: [--fix]
      # Форматирование
      - id: ruff-format
```

## Полезные команды

```bash
# Показать все доступные правила
ruff rule

# Показать информацию о конкретном правиле
ruff rule E501

# Сгенерировать конфигурационный файл
ruff generate-config > pyproject.toml

# Проверить только измененные файлы (по сравнению с main)
ruff check --diff origin/main

# Проверить и отсортировать импорты
ruff check --select I --fix

# Использовать с cache для ускорения
ruff check . --cache-dir .ruff_cache
```

## Примеры использования в CI/CD

### GitHub Actions

```yaml
name: Ruff
on: [push, pull_request]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: astral-sh/ruff-action@v1
        with:
          args: check --format=github
```

### GitLab CI

```yaml
lint:
  image: python:3.11
  script:
    - pip install ruff
    - ruff check .
    - ruff format --check .
```

## Советы и лучшие практики

1. **Начните с минимальной конфигурации** и постепенно добавляйте правила
2. **Используйте `--fix`** для автоматического исправления большинства проблем
3. **Интегрируйте в pre-commit** для проверки перед коммитом
4. **Настройте ваш редактор** для автоматического форматирования при сохранении
5. **Используйте строгий режим в CI**, но более мягкий локально

## Сравнение с другими инструментами

Ruff заменяет:
- `flake8` (линтер)
- `isort` (сортировка импортов)
- `black` (форматирование)
- `pyupgrade` (обновление синтаксиса)
- `pydocstyle` (документация)
- и многие другие плагины

**Преимущества Ruff:**
- ⚡ В 10-100 раз быстрее альтернатив
- 🎯 Одна зависимость вместо многих
- 🔧 Единая конфигурация
- 🛠 Встроенный автофикс

Ruff — это современный, быстрый и удобный инструмент для поддержания качества Python-кода, который значительно упрощает рабочий процесс разработки.