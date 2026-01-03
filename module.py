"""
Структура пакета mypackage:

mypackage/
├── __init__.py          # Инициализация пакета
├── core.py             # Основные функции
├── utils.py            # Вспомогательные функции
├── constants.py        # Константы
├── subpackage/         # Подпакет
│   ├── __init__.py
│   └── helpers.py
└── tests/              # Тесты
    ├── __init__.py
    ├── test_core.py
    └── test_utils.py
"""

# Файл: mypackage/__init__.py
"""
Пакет mypackage - пример структурированного пакета.
"""

__version__ = "1.0.0"
__author__ = "Ваше Имя"
__license__ = "MIT"

# Импорт ключевых объектов для удобного доступа
from .core import main_function, HelperClass
from .utils import utility_function
from .constants import DEFAULT_SETTINGS

# Контроль экспорта
__all__ = [
    'main_function',
    'HelperClass',
    'utility_function',
    'DEFAULT_SETTINGS',
    'subpackage'  # Экспортируем подпакет
]

# Инициализация пакета
print(f"Пакет mypackage v{__version__} инициализирован")

# Файл: mypackage/core.py
def main_function():
    """Основная функция пакета"""
    return "Hello from main_function!"

class HelperClass:
    """Вспомогательный класс"""
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

# Файл: mypackage/utils.py
def utility_function():
    """Вспомогательная функция"""
    return "Utility function called"

# Файл: mypackage/constants.py
DEFAULT_SETTINGS = {
    'timeout': 30,
    'retries': 3,
    'debug': False
}

# Файл: mypackage/subpackage/__init__.py
from .helpers import helper_function

__all__ = ['helper_function']

# Файл: mypackage/subpackage/helpers.py
def helper_function():
    """Функция-помощник"""
    return "Help from subpackage!"

# Использование пакета
print("Использование пакета:")

# Способ 1: Импорт из пакета
import mypackage

print(f"Версия пакета: {mypackage.__version__}")
print(f"Основная функция: {mypackage.main_function()}")

# Создание экземпляра класса
helper = mypackage.HelperClass("Alice")
print(f"Приветствие: {helper.greet()}")

# Доступ к константам
print(f"Настройки: {mypackage.DEFAULT_SETTINGS}")

# Доступ к подпакету
print(f"Помощник: {mypackage.subpackage.helper_function()}")

# Способ 2: Импорт конкретных объектов
from mypackage import main_function, utility_function
from mypackage.subpackage import helper_function

print(f"\nmain_function: {main_function()}")
print(f"utility_function: {utility_function()}")
print(f"helper_function: {helper_function()}")

# Способ 3: Относительный импорт (внутри пакета)
# В файле внутри пакета можно использовать:
# from . import core              # импорт из текущего пакета
# from .. import another_package  # импорт из родительского пакета
# from .subpackage import helpers # импорт из подпакета