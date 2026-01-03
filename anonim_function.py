# Анонимные функции (лямбды), функции высшего порядка и замыкания в Python

## Содержание
1. [Лямбда-функции](#лямбда-функции)
2. [Функции высшего порядка](#функции-высшего-порядка)
3. [Замыкания](#замыкания)
4. [Практические примеры](#практические-примеры)

## Лямбда-функции

Лямбда-функции — это анонимные функции, определяемые в одной строке с помощью ключевого слова `lambda`.

### Базовый синтаксис

```python
# Обычная функция
def add(x, y):
    return x + y

# Эквивалентная лямбда-функция
add_lambda = lambda x, y: x + y

print(add(5, 3))          # 8
print(add_lambda(5, 3))   # 8

# Лямбда может быть использована сразу без присваивания
print((lambda x, y: x * y)(4, 5))  # 20
```

### Особенности лямбда-функций

```python
# Лямбда всегда возвращает значение
square = lambda x: x ** 2
print(square(5))  # 25

# Несколько аргументов
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # 24

# Без аргументов (редко используется)
always_true = lambda: True
print(always_true())  # True

# Лямбда с условием
get_sign = lambda x: "positive" if x > 0 else ("zero" if x == 0 else "negative")
print(get_sign(10))   # positive
print(get_sign(-5))   # negative
print(get_sign(0))    # zero

# Нельзя использовать операторы присваивания или сложные конструкции
# Это НЕ сработает:
# lambda x: y = x * 2  # SyntaxError
```

### Ограничения лямбда-функций

```python
# 1. Только одно выражение
# Можно:
simple = lambda x: x + 1

# Нельзя использовать несколько выражений:
# complex_lambda = lambda x: print(x); return x * 2  # SyntaxError

# 2. Нет docstring
# Обычная функция может иметь документацию
def func(x):
    """Возвращает x + 1"""
    return x + 1

# Лямбда не может
lambda_func = lambda x: x + 1
# print(lambda_func.__doc__)  # None

# 3. Неявный return
# Всегда возвращает результат последнего выражения
result = (lambda: 42)()
print(result)  # 42

# 4. Нельзя использовать аннотации типов внутри
# Это НЕ сработает:
# lambda x: int: x + 1  # SyntaxError

# Но можно аннотировать переменную лямбды
from typing import Callable
add: Callable[[int, int], int] = lambda x, y: x + y
```

## Функции высшего порядка

Функции высшего порядка — это функции, которые принимают другие функции в качестве аргументов или возвращают функции.

### map() - применение функции к каждому элементу

```python
# Базовое использование
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# С несколькими итерируемыми объектами
a = [1, 2, 3]
b = [10, 20, 30]
result = map(lambda x, y: x + y, a, b)
print(list(result))  # [11, 22, 33]

# С обычной функцией вместо лямбды
def to_upper(string):
    return string.upper()

words = ['hello', 'world', 'python']
upper_words = map(to_upper, words)
print(list(upper_words))  # ['HELLO', 'WORLD', 'PYTHON']

# Комбинирование с другими функциями
numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, numbers))
print(int_numbers)  # [1, 2, 3, 4]

# Работа с разными типами данных
mixed = [1, '2', 3.0, '4.5']
parsed = map(lambda x: float(x) if isinstance(x, str) else float(x), mixed)
print(list(parsed))  # [1.0, 2.0, 3.0, 4.5]
```

### filter() - фильтрация элементов

```python
# Фильтрация четных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6, 8, 10]

# Фильтрация непустых строк
strings = ['hello', '', 'world', '', 'python', '']
non_empty = filter(lambda s: s != '', strings)
print(list(non_empty))  # ['hello', 'world', 'python']

# Использование bool как функции фильтрации
# bool возвращает False для: 0, 0.0, '', [], {}, None, False
values = [0, 1, '', 'hello', [], [1, 2], None, False, True]
truthy = filter(bool, values)
print(list(truthy))  # [1, 'hello', [1, 2], True]

# Фильтрация по сложному условию
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 16}
]

adults = filter(lambda p: p['age'] >= 18, data)
print(list(adults))  
# [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

# Цепочка фильтров
numbers = range(1, 21)
# Числа, которые делятся на 2 или на 3, но не на 6
filtered = filter(
    lambda x: (x % 2 == 0 or x % 3 == 0) and x % 6 != 0,
    numbers
)
print(list(filtered))  # [2, 3, 4, 8, 9, 10, 14, 15, 16, 20]
```

### sorted() - сортировка с ключом

```python
# Сортировка по длине строки
words = ['python', 'java', 'c', 'javascript', 'go']
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  # ['c', 'go', 'java', 'python', 'javascript']

# Обратная сортировка
sorted_by_length_desc = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_by_length_desc)  # ['javascript', 'python', 'java', 'go', 'c']

# Сортировка по последнему символу
sorted_by_last_char = sorted(words, key=lambda x: x[-1])
print(sorted_by_last_char)  # ['java', 'python', 'c', 'go', 'javascript']

# Сортировка сложных объектов
students = [
    {'name': 'Alice', 'grade': 85, 'age': 20},
    {'name': 'Bob', 'grade': 90, 'age': 19},
    {'name': 'Charlie', 'grade': 85, 'age': 21},
    {'name': 'David', 'grade': 92, 'age': 19}
]

# Сортировка по оценке (по убыванию), затем по возрасту (по возрастанию)
sorted_students = sorted(
    students,
    key=lambda s: (-s['grade'], s['age'])
)
for student in sorted_students:
    print(student)

# Сортировка с преобразованием
mixed_case = ['Apple', 'banana', 'Cherry', 'date']
# Без учета регистра
sorted_ignore_case = sorted(mixed_case, key=lambda x: x.lower())
print(sorted_ignore_case)  # ['Apple', 'banana', 'Cherry', 'date']

# Сортировка по нескольким критериям с разной направленностью
data = [
    ('Alice', 'B', 25),
    ('Bob', 'A', 30),
    ('Charlie', 'B', 20),
    ('David', 'A', 25)
]

# Сортировка: сначала по букве (по возрастанию), затем по числу (по убыванию)
sorted_data = sorted(data, key=lambda x: (x[1], -x[2]))
print(sorted_data)
# [('Bob', 'A', 30), ('David', 'A', 25), ('Alice', 'B', 25), ('Charlie', 'B', 20)]
```

### reduce() - накопление результата

**Важно**: `reduce()` находится в модуле `functools`

```python
from functools import reduce

# Сумма элементов списка
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15

# То же самое с начальным значением
sum_with_init = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_init)  # 25 (10 + 1 + 2 + 3 + 4 + 5)

# Произведение элементов
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Поиск максимального элемента
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # 5

# Конкатенация строк
words = ['Hello', ' ', 'World', '!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Hello World!

# Более сложный пример: преобразование списка в словарь
pairs = [('a', 1), ('b', 2), ('c', 3)]
to_dict = reduce(lambda d, pair: {**d, pair[0]: pair[1]}, pairs, {})
print(to_dict)  # {'a': 1, 'b': 2, 'c': 3}

# Построение иерархии
data = [
    ('root', 'dir1'),
    ('dir1', 'file1.txt'),
    ('root', 'dir2'),
    ('dir2', 'file2.txt'),
    ('dir1', 'subdir1'),
    ('subdir1', 'file3.txt')
]

def build_tree(tree, item):
    parent, child = item
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)
    return tree

file_tree = reduce(build_tree, data, {})
print(file_tree)
# {'root': ['dir1', 'dir2'], 'dir1': ['file1.txt', 'subdir1'], 
#  'dir2': ['file2.txt'], 'subdir1': ['file3.txt']}
```

## Замыкания

Замыкание — это функция, которая запоминает значения из окружающей её области видимости, даже когда эти значения больше не существуют в памяти.

### Базовое понимание замыканий

```python
def outer_function(msg):
    # Внешняя функция
    message = msg
    
    def inner_function():
        # Внутренняя функция - ЗАМЫКАНИЕ
        # Она имеет доступ к переменным внешней функции
        print(message)
    
    return inner_function

# Создаем замыкания
hello_func = outer_function('Hello')
bye_func = outer_function('Goodbye')

# Вызываем замыкания
hello_func()  # Hello
bye_func()    # Goodbye

# Переменная message больше не существует в области видимости,
# но замыкания помнят её значения
```

### Как работают замыкания

```python
def counter():
    count = 0
    
    def increment():
        nonlocal count  # Объявляем, что используем переменную из внешней области
        count += 1
        return count
    
    return increment

# Создаем счетчик
c1 = counter()
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3

# Создаем второй независимый счетчик
c2 = counter()
print(c2())  # 1
print(c2())  # 2

# Они независимы, так как каждый имеет свою область видимости
print(c1())  # 4
print(c2())  # 3
```

### Практическое использование замыканий

#### 1. Создание специализированных функций

```python
def power_factory(exponent):
    """Создает функцию, возводящую в указанную степень"""
    def power(base):
        return base ** exponent
    
    return power

# Создаем специализированные функции
square = power_factory(2)
cube = power_factory(3)
sqrt = power_factory(0.5)

print(square(5))  # 25
print(cube(3))    # 27
print(sqrt(16))   # 4.0

# Более сложный пример
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    
    # Добавим метаданные к функции
    multiplier.__name__ = f"multiply_by_{factor}"
    multiplier.__doc__ = f"Умножает аргумент на {factor}"
    
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))      # 20
print(triple(10))      # 30
print(double.__name__) # multiply_by_2
print(double.__doc__)  # Умножает аргумент на 2
```

#### 2. Кэширование (мемоизация)

```python
def memoize(func):
    """Декоратор для кэширования результатов функции"""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

# Применяем мемоизацию
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Без мемоизации вычисление fibonacci(35) заняло бы очень долго
print(fibonacci(35))  # 9227465

# Проверка кэша (косвенно)
print(fibonacci.__closure__[0].cell_contents)  # покажет кэш
```

#### 3. Конфигурация функций

```python
def make_adder(n):
    """Создает функцию, добавляющую n к аргументу"""
    def adder(x):
        return x + n
    return adder

# Создаем специализированные функции
add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))   # 8
print(add10(3))  # 13

# Использование в обработчиках событий
def event_handler_factory(event_type):
    def handler(data):
        print(f"Event {event_type} received with data: {data}")
        # Здесь может быть сложная логика обработки
        return f"Processed {event_type}"
    return handler

click_handler = event_handler_factory('click')
hover_handler = event_handler_factory('hover')

print(click_handler({'x': 100, 'y': 200}))
print(hover_handler({'x': 50, 'y': 60}))
```

#### 4. Состояние между вызовами

```python
def make_account(initial_balance=0):
    balance = initial_balance
    
    def account(action, amount=0):
        nonlocal balance
        
        if action == 'deposit':
            balance += amount
            return f"Deposited {amount}. New balance: {balance}"
        elif action == 'withdraw':
            if amount > balance:
                return f"Insufficient funds. Balance: {balance}"
            balance -= amount
            return f"Withdrew {amount}. New balance: {balance}"
        elif action == 'balance':
            return f"Current balance: {balance}"
        else:
            return "Invalid action"
    
    return account

# Создаем банковский счет
my_account = make_account(1000)

print(my_account('balance'))     # Current balance: 1000
print(my_account('deposit', 500)) # Deposited 500. New balance: 1500
print(my_account('withdraw', 200)) # Withdrew 200. New balance: 1300
print(my_account('withdraw', 1500)) # Insufficient funds. Balance: 1300
```

### Замыкания с изменяемыми и неизменяемыми объектами

```python
# С неизменяемыми объектами (требуется nonlocal)
def counter_immutable():
    count = 0  # int - неизменяемый
    
    def increment():
        nonlocal count  # Без nonlocal будет UnboundLocalError
        count += 1
        return count
    
    return increment

# С изменяемыми объектами (nonlocal не всегда нужен)
def counter_mutable():
    count = [0]  # list - изменяемый
    
    def increment():
        count[0] += 1  # Можем изменять содержимое списка
        return count[0]
    
    return increment

# Другой пример с изменяемыми объектами
def make_averager():
    series = []  # list - изменяемый
    
    def averager(new_value):
        series.append(new_value)  # Изменяем содержимое списка
        total = sum(series)
        return total / len(series)
    
    return averager

avg = make_averager()
print(avg(10))  # 10.0
print(avg(20))  # 15.0
print(avg(30))  # 20.0

# Проверим, что series сохраняется
print(avg.__closure__[0].cell_contents)  # [10, 20, 30]
```

### Замыкания vs Классы

```python
# Реализация счетчика через замыкание
def make_counter_closure():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = 0
        return count
    
    # Возвращаем словарь методов
    return {
        'increment': increment,
        'decrement': decrement,
        'get': get_count,
        'reset': reset
    }

# Реализация счетчика через класс
class CounterClass:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def decrement(self):
        self.count -= 1
        return self.count
    
    def get(self):
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count

# Использование
counter1 = make_counter_closure()
counter2 = CounterClass()

print("Замыкание:")
print(counter1['increment']())  # 1
print(counter1['increment']())  # 2
print(counter1['get']())        # 2

print("\nКласс:")
print(counter2.increment())     # 1
print(counter2.increment())     # 2
print(counter2.get())           # 2
```

## Практические примеры

### Пример 1: Обработка данных с комбинацией map, filter, sorted

```python
# Обработка данных о продажах
sales_data = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 3, 'category': 'electronics'},
    {'product': 'Mouse', 'price': 25, 'quantity': 10, 'category': 'electronics'},
    {'product': 'Notebook', 'price': 5, 'quantity': 50, 'category': 'stationery'},
    {'product': 'Pen', 'price': 2, 'quantity': 100, 'category': 'stationery'},
    {'product': 'Monitor', 'price': 300, 'quantity': 2, 'category': 'electronics'},
    {'product': 'Keyboard', 'price': 80, 'quantity': 5, 'category': 'electronics'},
]

# 1. Вычислить общую стоимость для каждого товара
with_totals = list(map(
    lambda item: {**item, 'total': item['price'] * item['quantity']},
    sales_data
))

# 2. Отфильтровать только электронику
electronics = list(filter(
    lambda item: item['category'] == 'electronics',
    with_totals
))

# 3. Отсортировать по убыванию общей стоимости
sorted_electronics = sorted(
    electronics,
    key=lambda item: item['total'],
    reverse=True
)

# 4. Вывести результат
print("Электроника, отсортированная по выручке:")
for item in sorted_electronics:
    print(f"{item['product']}: ${item['total']}")

# 5. Общая выручка от электроники
total_revenue = reduce(
    lambda acc, item: acc + item['total'],
    sorted_electronics,
    0
)
print(f"\nОбщая выручка от электроники: ${total_revenue}")
```

### Пример 2: Конвейер обработки текста

```python
from functools import reduce

def create_text_pipeline(*functions):
    """Создает конвейер обработки текста из последовательности функций"""
    def pipeline(text):
        return reduce(lambda acc, func: func(acc), functions, text)
    return pipeline

# Функции обработки
clean_spaces = lambda text: ' '.join(text.split())
to_lower = lambda text: text.lower()
remove_punctuation = lambda text: ''.join(char for char in text if char.isalnum() or char == ' ')
remove_stopwords = lambda text: ' '.join(
    word for word in text.split() 
    if word not in {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at'}
)
stem_words = lambda text: ' '.join(word[:-1] if word.endswith('s') else word for word in text.split())

# Создаем конвейер
process_text = create_text_pipeline(
    clean_spaces,
    to_lower,
    remove_punctuation,
    remove_stopwords,
    stem_words
)

# Текст для обработки
text = "The cats and dogs are playing in the gardens!"
result = process_text(text)
print(f"Исходный текст: {text}")
print(f"Обработанный текст: {result}")
# Исходный текст: The cats and dogs are playing in the gardens!
# Обработанный текст: cat dog are playing garden
```

### Пример 3: Система плагинов с замыканиями

```python
def plugin_system():
    """Система плагинов с использованием замыканий"""
    plugins = []
    
    def register_plugin(name, func):
        plugins.append((name, func))
        print(f"Плагин '{name}' зарегистрирован")
    
    def execute_plugins(data, context=None):
        results = {}
        for name, plugin in plugins:
            try:
                results[name] = plugin(data, context) if context else plugin(data)
            except Exception as e:
                results[name] = f"Error in {name}: {str(e)}"
        return results
    
    def list_plugins():
        return [name for name, _ in plugins]
    
    return {
        'register': register_plugin,
        'execute': execute_plugins,
        'list': list_plugins
    }

# Создаем систему плагинов
system = plugin_system()

# Создаем плагины с помощью замыканий
def create_log_plugin(log_file):
    """Создает плагин для логирования"""
    def log_plugin(data, context):
        import datetime
        log_entry = f"{datetime.datetime.now()}: {data}\n"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        return f"Logged to {log_file}"
    return log_plugin

def create_transform_plugin(transformation):
    """Создает плагин для преобразования данных"""
    def transform_plugin(data, context):
        if transformation == 'upper':
            return data.upper()
        elif transformation == 'reverse':
            return data[::-1]
        else:
            return data
    return transform_plugin

# Регистрируем плагины
system['register']('logger', create_log_plugin('app.log'))
system['register']('uppercaser', create_transform_plugin('upper'))
system['register']('reverser', create_transform_plugin('reverse'))

# Используем плагины
data = "Hello, Plugin System!"
results = system['execute'](data, {'user': 'admin'})

print("Результаты выполнения плагинов:")
for plugin, result in results.items():
    print(f"  {plugin}: {result}")

print(f"\nЗарегистрированные плагины: {system['list']()}")
```

### Пример 4: Валидация данных с цепочкой валидаторов

```python
def create_validator_chain(*validators):
    """Создает цепочку валидаторов"""
    def validate(value):
        errors = []
        for validator in validators:
            result = validator(value)
            if result is not True:
                errors.append(result)
        return errors if errors else True
    return validate

# Фабрики валидаторов с замыканиями
def min_length_validator(min_len):
    def validator(value):
        if len(value) < min_len:
            return f"Длина должна быть не менее {min_len} символов"
        return True
    return validator

def max_length_validator(max_len):
    def validator(value):
        if len(value) > max_len:
            return f"Длина должна быть не более {max_len} символов"
        return True
    return validator

def regex_validator(pattern, message):
    import re
    def validator(value):
        if not re.match(pattern, value):
            return message
        return True
    return validator

def contains_validator(chars):
    def validator(value):
        for char in chars:
            if char not in value:
                return f"Должен содержать символ '{char}'"
        return True
    return validator

# Создаем цепочку валидаторов для пароля
validate_password = create_validator_chain(
    min_length_validator(8),
    max_length_validator(20),
    regex_validator(r'.*[A-Z].*', 'Должна быть хотя бы одна заглавная буква'),
    regex_validator(r'.*[a-z].*', 'Должна быть хотя бы одна строчная буква'),
    regex_validator(r'.*\d.*', 'Должна быть хотя бы одна цифра'),
    contains_validator(['!', '@', '#', '$', '%'])
)

# Тестируем валидацию
test_passwords = [
    "weak",
    "NoSpecialChar123",
    "Short1!",
    "GoodPassword123!",
    "nouppercase123!",
    "NOLOWERCASE123!"
]

print("Результаты валидации паролей:")
for password in test_passwords:
    result = validate_password(password)
    if result is True:
        print(f"  '{password}': ✓ Валиден")
    else:
        print(f"  '{password}': ✗ Ошибки: {result}")
```

### Пример 5: Функциональный стиль с reduce для сложных преобразований

```python
from functools import reduce
from collections import defaultdict

# Сложная обработка данных: агрегация и статистика
orders = [
    {'customer': 'Alice', 'product': 'Laptop', 'amount': 1200, 'date': '2024-01-15'},
    {'customer': 'Bob', 'product': 'Mouse', 'amount': 25, 'date': '2024-01-15'},
    {'customer': 'Alice', 'product': 'Mouse', 'amount': 25, 'date': '2024-01-16'},
    {'customer': 'Charlie', 'product': 'Laptop', 'amount': 1200, 'date': '2024-01-16'},
    {'customer': 'Bob', 'product': 'Keyboard', 'amount': 80, 'date': '2024-01-17'},
    {'customer': 'Alice', 'product': 'Monitor', 'amount': 300, 'date': '2024-01-17'},
    {'customer': 'Charlie', 'product': 'Mouse', 'amount': 25, 'date': '2024-01-18'},
]

# Агрегируем данные: сумма покупок по клиенту и дате
def aggregate_orders(acc, order):
    customer = order['customer']
    date = order['date']
    amount = order['amount']
    
    if customer not in acc:
        acc[customer] = {'total': 0, 'by_date': defaultdict(int)}
    
    acc[customer]['total'] += amount
    acc[customer]['by_date'][date] += amount
    
    return acc

# Используем reduce для агрегации
customer_stats = reduce(aggregate_orders, orders, {})

print("Статистика по клиентам:")
for customer, stats in customer_stats.items():
    print(f"\n{customer}:")
    print(f"  Общая сумма: ${stats['total']}")
    print(f"  Покупки по датам:")
    for date, amount in stats['by_date'].items():
        print(f"    {date}: ${amount}")

# Дополнительно: находим лучшего клиента
best_customer = reduce(
    lambda best, current: current if current[1]['total'] > best[1]['total'] else best,
    customer_stats.items()
)
print(f"\nЛучший клиент: {best_customer[0]} с суммой ${best_customer[1]['total']}")
```

## Советы и лучшие практики

### Когда использовать лямбды:
1. **Короткие одноразовые операции** в функциях высшего порядка
2. **Простые преобразования** в `map()`, `filter()`, `sorted()`
3. **Ключи сортировки**, которые можно выразить в одной строке

### Когда НЕ использовать лямбды:
1. **Сложная логика** - используйте обычные функции
2. **Многократное использование** - дайте функции имя для переиспользования
3. **Нужна документация** - у лямбд нет `__doc__`

### Замыкания vs Классы:
- **Замыкания** лучше для простого сохранения состояния
- **Классы** лучше для сложных объектов с множеством методов
- **Замыкания** более легковесны и функциональны
- **Классы** более явны и поддерживают наследование

### Производительность:
```python
import timeit

# Тест производительности: лямбда vs обычная функция
test_code = '''
def square_func(x):
    return x ** 2

square_lambda = lambda x: x ** 2

numbers = list(range(1000))

# Использование map с обычной функцией
list(map(square_func, numbers))

# Использование map с лямбдой
list(map(square_lambda, numbers))
'''

# Разница в производительности обычно минимальна
# Читаемость важнее микрооптимизаций
```

### Отладка замыканий:
```python
def make_closure(value):
    def inner():
        return value
    return inner

closure = make_closure(42)

# Информация о замыкании
print(closure.__code__.co_freevars)  # ('value',)
print(closure.__closure__[0].cell_contents)  # 42
```

## Заключение

Лямбда-функции, функции высшего порядка и замыкания — мощные инструменты функционального программирования в Python. Они позволяют писать более выразительный, компактный и гибкий код. Ключ к их эффективному использованию — понимание, когда они действительно улучшают читаемость и поддерживаемость кода, а когда лучше использовать более традиционные подходы.