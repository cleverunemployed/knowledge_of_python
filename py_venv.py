venv:
    
* py -m venv venv создание
* venv\Scripts\activate
* pip install requests
* pip freeze
* deactivate
* Set-ExecutionPolicy RemoteSigned
* pip install -r requerements.txt

UV:

* powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
* uv init venv
* uv run hello.py
* uv add requests
* uv sync
* uv tree
* uv remove requests yt-dlp
* uv python install 3.10
* uv python pin 3.10
* uv cache clean
При первом запуске команды uv run, внутри venv будет создана директория .venv, содержащая устанавливаемые зависимости, используемые в окружении. Помимо этого, будет создан кроссплатформенный uv.lock файл.

.venv
.gitignore
.python-version
hello.py
pyproject.toml
README.md
uv.lock

Взглянем ещё раз на значение dependences в файле pyproject.toml после установки requests:

[project]
name = "venv"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "requests>=2.32.3",
]

One more thing
Помимо удобного интерфейса, быстрой скорости работы, инлайн-запуска и возможности работы с несколькими версиями Python в одном окружении, в uv есть мощный инструмент — tool.

Как это работает:

uvx black main.py
Объяснить код с
Команда uvx black main.py выполняет следующие действия:

uvx создает временное изолированное виртуальное окружение

Загружает и устанавливает пакет black (форматтер кода для Python) в это временное окружение

Запускает инструмент black из установленного пакета

Запущенный black анализирует и форматирует код в файле main.py

Poetry:
    
* (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
* poetry install
* poetry update
* poetry show --tree
* poetry install --extras "mysql pgsql"
* poetry install -E mysql -E pgsql
* poetry new new_project
* poetry init
* poetry add "pygame>=2"
* poetry show
* poetry show --tree
* poetry run python main.py