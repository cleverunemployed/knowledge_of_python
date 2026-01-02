# Пользовательские функции в Python

## Объявление функций с помощью `def`

Функции объявляются с помощью ключевого слова `def`:

```python
def имя_функции(параметры):
    """Документация функции (docstring)"""
    # тело функции
    return результат
```

Пример:
```python
def greet(name):
    """Приветствует пользователя по имени"""
    return f"Привет, {name}!"

print(greet("Анна"))  # Вывод: Привет, Анна!
```

## Возврат значений через `return`

Функция может возвращать одно или несколько значений:

```python
def calculate(a, b):
    """Возвращает несколько значений"""
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result  # Возвращает кортеж

result_sum, result_diff = calculate(10, 5)
print(result_sum)   # 15
print(result_diff)  # 5

# Функция без return возвращает None
def no_return():
    print("Эта функция ничего не возвращает")

value = no_return()  # value = None
```

## Передача аргументов

### 1. Позиционные аргументы
```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))  # 8
```

### 2. Именованные аргументы
```python
def introduce(name, age, city):
    return f"{name}, {age} лет, из {city}"

# Разные способы вызова
print(introduce("Иван", 25, "Москва"))  # Позиционные
print(introduce(name="Иван", age=25, city="Москва"))  # Именованные
print(introduce(age=25, city="Москва", name="Иван"))  # Порядок не важен
```

### 3. Аргументы по умолчанию
```python
def greet(name, greeting="Привет", punctuation="!"):
    """Аргументы со значениями по умолчанию"""
    return f"{greeting}, {name}{punctuation}"

print(greet("Мария"))                 # Привет, Мария!
print(greet("Петр", "Здравствуйте"))  # Здравствуйте, Петр!
print(greet("Анна", punctuation="?")) # Привет, Анна?
```

**Важно:** Аргументы по умолчанию вычисляются один раз при определении функции!

```python
def add_item(item, items=[]):  # ОПАСНО!
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - список сохраняется между вызовами!

# Правильный подход:
def add_item_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 4. Произвольное количество аргументов

#### *args - произвольное количество позиционных аргументов
```python
def sum_all(*args):
    """Принимает любое количество позиционных аргументов"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # 6
print(sum_all(1, 2, 3, 4, 5)) # 15
```

#### **kwargs - произвольное количество именованных аргументов
```python
def print_info(**kwargs):
    """Принимает любое количество именованных аргументов"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Иван", age=30, city="Москва")
# name: Иван
# age: 30
# city: Москва
```

### 5. Комбинирование разных типов аргументов
```python
def complex_function(a, b=10, *args, c=20, **kwargs):
    """Все типы аргументов вместе"""
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, c=30, name="Иван", age=25)
# a: 1, b: 2, c: 30
# args: (3, 4, 5)
# kwargs: {'name': 'Иван', 'age': 25}
```

## Область видимости переменных

### 1. Локальные переменные
```python
def my_function():
    local_var = "Я локальная переменная"
    print(local_var)

my_function()  # Вывод: Я локальная переменная
# print(local_var)  # Ошибка! local_var не определена вне функции
```

### 2. Глобальные переменные
```python
global_var = "Я глобальная переменная"

def show_global():
    print(global_var)  # Можно читать

show_global()  # Вывод: Я глобальная переменная

def modify_global():
    global global_var  # Объявляем, что будем изменять глобальную переменную
    global_var = "Измененное значение"

modify_global()
print(global_var)  # Вывод: Измененное значение
```

### 3. Нелокальные переменные (nonlocal)
```python
def outer():
    x = "локальная переменная outer"
    
    def inner():
        nonlocal x  # Используем переменную из внешней функции
        x = "изменена inner"
        print(f"inner: {x}")
    
    inner()
    print(f"outer: {x}")

outer()
# Вывод:
# inner: изменена inner
# outer: изменена inner
```

### 4. Замыкания (closures)
```python
def make_multiplier(factor):
    """Функция, возвращающая другую функцию"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## Использование блоков `try`, `except`, `else`, `finally`

### Базовый синтаксис обработки исключений
```python
try:
    # Код, который может вызвать исключение
    result = 10 / 0
except ZeroDivisionError:
    # Обработка конкретного исключения
    print("Деление на ноль!")
except ValueError:
    # Обработка другого исключения
    print("Неверное значение!")
except Exception as e:
    # Обработка всех остальных исключений
    print(f"Произошла ошибка: {e}")
else:
    # Выполняется, если исключений не было
    print("Ошибок не произошло")
finally:
    # Выполняется всегда
    print("Блок finally выполняется в любом случае")
```

### Практические примеры
```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except TypeError:
        return "Ошибка: неверный тип данных"
    else:
        return f"Результат: {result}"
    finally:
        print("Операция деления завершена")

print(divide(10, 2))    # Результат: 5.0
print(divide(10, 0))    # Ошибка: деление на ноль
print(divide(10, "a"))  # Ошибка: неверный тип данных
```

### Создание собственных исключений
```python
class NegativeNumberError(Exception):
    """Исключение для отрицательных чисел"""
    pass

def sqrt_positive(number):
    if number < 0:
        raise NegativeNumberError("Число не может быть отрицательным")
    return number ** 0.5

try:
    print(sqrt_positive(4))   # 2.0
    print(sqrt_positive(-4))  # Вызовет исключение
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
```

## Декораторы

Декораторы - это функции, которые изменяют поведение других функций.

### Базовый декоратор
```python
def my_decorator(func):
    def wrapper():
        print("Действие перед вызовом функции")
        func()
        print("Действие после вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

say_hello()
# Вывод:
# Действие перед вызовом функции
# Привет!
# Действие после вызовом функции
```

### Декоратор с аргументами
```python
def repeat(times):
    """Декоратор, повторяющий вызов функции"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Привет, {name}!")

greet("Анна")
# Вывод:
# Привет, Анна!
# Привет, Анна!
# Привет, Анна!
```

### Декоратор с сохранением метаданных
```python
import functools

def debug(func):
    """Декоратор, выводящий информацию о вызове функции"""
    @functools.wraps(func)  # Сохраняем метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    """Складывает два числа"""
    return a + b

print(add(2, 3))
# Вывод:
# Вызов функции add
# Аргументы: (2, 3), {}
# Результат: 5
# 5

print(add.__name__)  # 'add' (без @functools.wraps было бы 'wrapper')
print(add.__doc__)   # 'Складывает два числа'
```

### Несколько декораторов
```python
def decorator1(func):
    def wrapper():
        print("Декоратор 1: до")
        func()
        print("Декоратор 1: после")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Декоратор 2: до")
        func()
        print("Декоратор 2: после")
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Основная функция")

my_function()
# Вывод:
# Декоратор 1: до
# Декоратор 2: до
# Основная функция
# Декоратор 2: после
# Декоратор 1: после
```

### Декоратор класса
```python
def singleton(cls):
    """Декоратор, превращающий класс в singleton"""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Создание подключения к БД")
    
    def query(self, sql):
        print(f"Выполнение запроса: {sql}")

db1 = DatabaseConnection()  # Создание подключения к БД
db2 = DatabaseConnection()  # Ничего не выведет - объект уже создан
print(db1 is db2)  # True
```

### Встроенные декораторы
```python
class MyClass:
    @staticmethod
    def static_method():
        """Не требует self, не имеет доступа к экземпляру или классу"""
        return "Статический метод"
    
    @classmethod
    def class_method(cls):
        """Принимает cls вместо self, имеет доступ к классу"""
        return f"Метод класса {cls.__name__}"
    
    @property
    def property_method(self):
        """Превращает метод в свойство (геттер)"""
        return self._value
    
    @property_method.setter
    def property_method(self, value):
        """Сеттер для свойства"""
        self._value = value
```

## Практический пример: кэширующий декоратор
```python
import functools
import time

def cache(func):
    """Декоратор для кэширования результатов функции"""
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Создаем ключ на основе аргументов
        key = str(args) + str(kwargs)
        
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print(f"Вычисление результата для {key}")
        else:
            print(f"Использование кэша для {key}")
        
        return cache_dict[key]
    
    return wrapper

@cache
def slow_function(x):
    """Имитация медленной функции"""
    time.sleep(2)
    return x * x

print(slow_function(4))  # Вычисление, затем вывод 16
print(slow_function(4))  # Использование кэша, быстрый вывод 16
print(slow_function(5))  # Вычисление, затем вывод 25
```

Эти концепции являются фундаментальными для эффективного программирования на Python и позволяют создавать чистый, модульный и поддерживаемый код.