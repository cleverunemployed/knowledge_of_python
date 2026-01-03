# Расширенные коллекции в Python: Counter, deque, defaultdict и namedtuple

Модуль `collections` в Python содержит специализированные структуры данных, которые дополняют стандартные встроенные коллекции (list, tuple, dict, set). Рассмотрим подробно каждую из перечисленных.

## 1. Counter - счетчик объектов

`Counter` - это подкласс словаря для подсчета хешируемых объектов.

### Основное применение:
```python
from collections import Counter

# Создание счетчика
word_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(word_counts)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Подсчет символов в строке
char_count = Counter('abracadabra')
print(char_count)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Работа со словарем
cnt = Counter({'red': 4, 'blue': 2})
print(cnt)  # Counter({'red': 4, 'blue': 2})
```

### Основные методы:
```python
c = Counter(a=3, b=2, c=1, d=0)

# most_common(n) - n самых частых элементов
print(c.most_common(2))  # [('a', 3), ('b', 2)]

# elements() - итератор по элементам
print(list(c.elements()))  # ['a', 'a', 'a', 'b', 'b', 'c']

# Арифметические операции
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)   # Counter({'a': 4, 'b': 3})
print(c1 - c2)   # Counter({'a': 2})
print(c1 & c2)   # Counter({'a': 1, 'b': 1}) - минимум
print(c1 | c2)   # Counter({'a': 3, 'b': 2}) - максимум
```

## 2. deque - двусторонняя очередь

`deque` (double-ended queue) - оптимизированная очередь с быстрым добавлением/удалением с обоих концов.

### Основные возможности:
```python
from collections import deque

# Создание deque
d = deque([1, 2, 3])
print(d)  # deque([1, 2, 3])

# Добавление элементов
d.append(4)           # в конец
d.appendleft(0)       # в начало
print(d)  # deque([0, 1, 2, 3, 4])

# Удаление элементов
right = d.pop()       # с конца
left = d.popleft()    # с начала
print(right, left)    # 4 0
print(d)  # deque([1, 2, 3])

# Вращение
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # положительный - вправо
print(d)  # deque([4, 5, 1, 2, 3])

d.rotate(-1)  # отрицательный - влево
print(d)  # deque([5, 1, 2, 3, 4])

# Ограничение размера
d = deque(maxlen=3)
for i in range(5):
    d.append(i)
    print(d)
# deque([0], maxlen=3)
# deque([0, 1], maxlen=3)
# deque([0, 1, 2], maxlen=3)
# deque([1, 2, 3], maxlen=3)  # 0 вытеснен
# deque([2, 3, 4], maxlen=3)  # 1 вытеснен
```

## 3. defaultdict - словарь со значением по умолчанию

`defaultdict` автоматически создает значения для несуществующих ключей.

### Примеры использования:
```python
from collections import defaultdict

# Создание со значением по умолчанию
# int() возвращает 0
d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['c'])  # 0 (ключ создан автоматически)

# Использование list в качестве фабрики
d = defaultdict(list)
d['fruits'].append('apple')
d['fruits'].append('banana')
d['vegetables'].append('carrot')
print(d)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})

# Сложные структуры
nested_dict = lambda: defaultdict(nested_dict)
data = nested_dict()
data['user']['profile']['name'] = 'Alice'
data['user']['profile']['age'] = 25
print(data['user']['profile'])  # defaultdict(<function <lambda> at ...>, {'name': 'Alice', 'age': 25})

# Словарь множеств
d = defaultdict(set)
d['group1'].add('user1')
d['group1'].add('user2')
d['group2'].add('user1')
print(d)  # defaultdict(<class 'set'>, {'group1': {'user1', 'user2'}, 'group2': {'user1'}})
```

## 4. namedtuple - именованный кортеж

`namedtuple` создает подкласс кортежа с именованными полями, что делает код более читаемым.

### Создание и использование:
```python
from collections import namedtuple

# Определение структуры
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Создание объектов
p1 = Point(10, 20)
p2 = Point(x=5, y=15)

person = Person('Alice', 30, 'New York')

# Доступ к полям
print(p1.x, p1.y)  # 10 20
print(person.name, person.age)  # Alice 30

# Доступ по индексу (как к обычному кортежу)
print(p1[0])  # 10
print(person[1])  # 30

# Именованные кортежи неизменяемы
# person.age = 31  # Вызовет AttributeError

# _replace() создает новую копию с изменениями
person_updated = person._replace(age=31)
print(person_updated)  # Person(name='Alice', age=31, city='New York')

# _asdict() преобразует в OrderedDict
print(person._asdict())  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# _make() создает из итерируемого объекта
p3 = Point._make([7, 14])
print(p3)  # Point(x=7, y=14)
```

### Расширенные возможности:
```python
# Значения по умолчанию
Person = namedtuple('Person', 'name age city', defaults=['Unknown', 0, 'Unknown'])
p = Person('Bob')
print(p)  # Person(name='Bob', age=0, city='Unknown')

# Дочерние классы
class Employee(namedtuple('Employee', 'id name position')):
    __slots__ = ()  # экономим память
    
    @property
    def email(self):
        return f"{self.name.lower().replace(' ', '.')}@company.com"
    
    def promote(self, new_position):
        return self._replace(position=new_position)

emp = Employee(1, 'John Doe', 'Developer')
print(emp.email)  # john.doe@company.com
emp2 = emp.promote('Senior Developer')
print(emp2)  # Employee(id=1, name='John Doe', position='Senior Developer')
```

## Практические примеры использования

### Пример 1: Анализ текста
```python
from collections import Counter, defaultdict

def analyze_text(text):
    # Подсчет слов
    words = text.lower().split()
    word_counter = Counter(words)
    
    # Группировка по длине слова
    by_length = defaultdict(list)
    for word in words:
        by_length[len(word)].append(word)
    
    return word_counter, by_length

text = "hello world hello python world code"
word_counts, length_groups = analyze_text(text)
print("Word counts:", word_counts)
print("Words by length:", dict(length_groups))
```

### Пример 2: Кэш с ограниченным размером (LRU)
```python
from collections import deque, OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Использование
cache = LRUCache(2)
cache.put(1, 'a')
cache.put(2, 'b')
print(cache.get(1))  # 'a'
cache.put(3, 'c')    # ключ 2 удаляется (наименее используемый)
print(cache.get(2))  # -1
```

### Пример 3: Система инвентаря
```python
from collections import Counter, namedtuple

Product = namedtuple('Product', 'id name price')

class Inventory:
    def __init__(self):
        self.products = {}
        self.stock = Counter()
    
    def add_product(self, product_id, name, price):
        self.products[product_id] = Product(product_id, name, price)
    
    def receive_stock(self, product_id, quantity):
        if product_id not in self.products:
            raise ValueError(f"Product {product_id} not found")
        self.stock[product_id] += quantity
    
    def sell(self, product_id, quantity):
        if self.stock[product_id] < quantity:
            raise ValueError(f"Insufficient stock for product {product_id}")
        self.stock[product_id] -= quantity
    
    def get_low_stock(self, threshold=5):
        return {pid: qty for pid, qty in self.stock.items() if qty < threshold}

# Использование
inv = Inventory()
inv.add_product(1, 'Laptop', 999.99)
inv.add_product(2, 'Mouse', 29.99)

inv.receive_stock(1, 10)
inv.receive_stock(2, 50)

inv.sell(1, 3)
inv.sell(2, 10)

print("Stock:", inv.stock)
print("Low stock:", inv.get_low_stock(20))
```

## Преимущества и недостатки

### Counter
**Плюсы:**
- Удобный подсчет элементов
- Богатый набор операций
- Эффективная реализация

**Минусы:**
- Только для хешируемых объектов
- Требует дополнительной памяти

### deque
**Плюсы:**
- O(1) для операций с обоих концов
- Поддержка ограничения размера
- Потокобезопасность для некоторых операций

**Минусы:**
- Медленнее списка для произвольного доступа
- Нет срезов (slicing)

### defaultdict
**Плюсы:**
- Упрощает код
- Избегает проверок на существование ключей
- Гибкость в выборе фабрики

**Минусы:**
- Может скрывать ошибки (автоматическое создание ключей)
- Немного больше накладных расходов

### namedtuple
**Плюсы:**
- Читаемость кода
- Легковесность (как кортеж)
- Совместимость с кортежами

**Минусы:**
- Неизменяемость
- Ограниченная функциональность по сравнению с классами

Эти коллекции из модуля `collections` являются мощными инструментами, которые могут значительно упростить и оптимизировать код Python при работе со специализированными структурами данных.