Итераторы и генераторы в Python: полное руководство
Содержание
Протокол итерации

Создание собственных итераторов

Генераторы и yield

Генераторные выражения

Практические примеры

Протокол итерации
Что такое итератор?
Итератор — это объект, который позволяет последовательно получать доступ к элементам коллекции или последовательности без необходимости знать внутреннюю структуру данных.

Протокол итератора состоит из двух методов:
__iter__() — возвращает сам итератор

__next__() — возвращает следующий элемент или вызывает StopIteration

python
# Встроенные итераторы в Python
my_list = [1, 2, 3, 4, 5]

# Получаем итератор
iterator = iter(my_list)  # или my_list.__iter__()
print(type(iterator))  # <class 'list_iterator'>

# Используем итератор
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
print(next(iterator))  # 5

# После последнего элемента
try:
    print(next(iterator))  # Вызовет StopIteration
except StopIteration:
    print("Итератор исчерпан")

# Цикл for автоматически использует протокол итерации
for item in my_list:
    print(f"Элемент: {item}")

# Что на самом деле делает цикл for:
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(f"Элемент: {item}")
    except StopIteration:
        break
Итерируемые объекты (Iterable) vs Итераторы (Iterator)
python
# Итерируемый объект (Iterable) - объект, который можно итерировать
# Должен иметь метод __iter__(), возвращающий итератор

# Итератор (Iterator) - объект, который непосредственно производит итерацию
# Должен иметь методы __iter__() и __next__()

# Все итераторы - итерируемые объекты, но не все итерируемые объекты - итераторы

my_list = [1, 2, 3]

# Проверяем типы
print("Список итерируемый?", hasattr(my_list, '__iter__'))  # True
print("Список итератор?", hasattr(my_list, '__next__'))     # False

iterator = iter(my_list)
print("Итератор итерируемый?", hasattr(iterator, '__iter__'))  # True
print("Итератор итератор?", hasattr(iterator, '__next__'))     # True

# Итератор истощается
list(iterator)  # Потребляем все элементы
print("Итератор пуст?", next(iterator, "Пусто"))  # "Пусто"

# Но исходный список остается неизменным
print("Список:", my_list)  # [1, 2, 3]

# Каждый вызов iter() создает новый итератор
iterator1 = iter(my_list)
iterator2 = iter(my_list)
print(next(iterator1))  # 1
print(next(iterator2))  # 1 (не 2!) - независимые итераторы
Создание собственных итераторов
Классический подход: класс с __iter__() и __next__()
python
class CountDown:
    """Итератор обратного отсчета"""
    def __init__(self, start):
        self.current = start
        self.start = start
    
    def __iter__(self):
        # Возвращает сам объект, так как он является итератором
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Использование
countdown = CountDown(5)
for number in countdown:
    print(number)  # 5, 4, 3, 2, 1, 0

# Можно использовать вручную
countdown = CountDown(3)
print(next(countdown))  # 3
print(next(countdown))  # 2
print(next(countdown))  # 1
print(next(countdown))  # 0
try:
    print(next(countdown))  # StopIteration
except StopIteration:
    print("Обратный отсчет завершен")

# Повторное использование (не сработает - итератор истощен)
print("Повторная итерация:")
for number in countdown:  # Не выполнится
    print(number)
print("Итератор пуст")
Итератор с состоянием и повторным использованием
python
class RangeIterator:
    """Итератор диапазона с возможностью сброса"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.current = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        # Сбрасываем состояние при каждом новом вызове iter()
        self.current = self.start
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value
    
    def reset(self):
        """Сброс итератора в начальное состояние"""
        self.current = self.start

# Использование
range_iter = RangeIterator(1, 5)
print("Первая итерация:")
for num in range_iter:
    print(num)  # 1, 2, 3, 4

print("\nВторая итерация (после сброса):")
range_iter.reset()
for num in range_iter:
    print(num)  # 1, 2, 3, 4

# Итератор с отрицательным шагом
neg_range = RangeIterator(5, 0, -1)
print("\nОбратный диапазон:")
for num in neg_range:
    print(num)  # 5, 4, 3, 2, 1
Итерируемый объект, который не является итератором
python
class TreeNode:
    """Узел бинарного дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def add_left(self, value):
        self.left = TreeNode(value)
        return self.left
    
    def add_right(self, value):
        self.right = TreeNode(value)
        return self.right

class BinaryTree:
    """Бинарное дерево с разными стратегиями обхода"""
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    def __iter__(self):
        # Возвращаем новый итератор при каждом вызове
        return self.inorder_iterator()
    
    def inorder_iterator(self):
        """Итератор для inorder обхода (левый-корень-правый)"""
        class InorderIterator:
            def __init__(self, root):
                self.stack = []
                self._push_left(root)
            
            def _push_left(self, node):
                while node:
                    self.stack.append(node)
                    node = node.left
            
            def __iter__(self):
                return self
            
            def __next__(self):
                if not self.stack:
                    raise StopIteration
                
                node = self.stack.pop()
                self._push_left(node.right)
                return node.value
        
        return InorderIterator(self.root)
    
    def preorder_iterator(self):
        """Итератор для preorder обхода (корень-левый-правый)"""
        class PreorderIterator:
            def __init__(self, root):
                self.stack = [root] if root else []
            
            def __iter__(self):
                return self
            
            def __next__(self):
                if not self.stack:
                    raise StopIteration
                
                node = self.stack.pop()
                if node.right:
                    self.stack.append(node.right)
                if node.left:
                    self.stack.append(node.left)
                return node.value
        
        return PreorderIterator(self.root)

# Создание дерева
tree = BinaryTree(1)
root = tree.root
root.add_left(2)
root.add_right(3)
root.left.add_left(4)
root.left.add_right(5)

print("Inorder обход (по умолчанию):")
for value in tree:  # Использует __iter__()
    print(value)  # 4, 2, 5, 1, 3

print("\nPreorder обход:")
for value in tree.preorder_iterator():
    print(value)  # 1, 2, 4, 5, 3

# Множественные итераторы
print("\nДва независимых итератора:")
iter1 = iter(tree)
iter2 = iter(tree)
print(f"iter1: {next(iter1)}, iter2: {next(iter2)}")  # iter1: 4, iter2: 4
print(f"iter1: {next(iter1)}, iter2: {next(iter2)}")  # iter1: 2, iter2: 2
Итератор для чтения файла по частям
python
class FileChunkReader:
    """Итератор для чтения файла частями"""
    def __init__(self, filename, chunk_size=1024):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = None
    
    def __iter__(self):
        # Открываем файл при начале итерации
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()
            self.file = None
            raise StopIteration
        
        return chunk
    
    def __del__(self):
        # Закрываем файл при удалении объекта
        if self.file:
            self.file.close()

# Использование
# Создаем тестовый файл
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, World!\n" * 10)

# Читаем файл по частям
print("Чтение файла по 20 символов:")
reader = FileChunkReader('test_file.txt', chunk_size=20)
for i, chunk in enumerate(reader, 1):
    print(f"Чанк {i}: {repr(chunk)}")

# Автоматическое закрытие файла
import os
os.remove('test_file.txt')
Генераторы и yield
Генераторы — это специальный тип итераторов, которые создаются с помощью функций, содержащих ключевое слово yield.

Базовый пример генератора
python
def simple_generator():
    """Простейший генератор"""
    print("Начало генератора")
    yield 1
    print("Продолжение после первого yield")
    yield 2
    print("Продолжение после второго yield")
    yield 3
    print("Конец генератора")

# Создаем генератор
gen = simple_generator()
print("Генератор создан, но код еще не выполнен")

# Получаем значения
print("Первое значение:", next(gen))
# Начало генератора
# Первое значение: 1

print("Второе значение:", next(gen))
# Продолжение после первого yield
# Второе значение: 2

print("Третье значение:", next(gen))
# Продолжение после второго yield
# Третье значение: 3

try:
    print("Четвертое значение:", next(gen))
except StopIteration:
    print("Генератор завершен")

# Итерация через for
print("\nИтерация через for:")
for value in simple_generator():
    print(f"Значение: {value}")
Генератор с состоянием
python
def fibonacci_generator(n):
    """Генератор чисел Фибоначчи"""
    a, b = 0, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Генерируем первые 10 чисел Фибоначчи
print("Первые 10 чисел Фибоначчи:")
for num in fibonacci_generator(10):
    print(num, end=" ")
print()

# Можно использовать вручную
fib_gen = fibonacci_generator(5)
print("Первые 5 вручную:", [next(fib_gen) for _ in range(5)])

# Генератор бесконечной последовательности
def infinite_counter(start=0, step=1):
    """Бесконечный счетчик"""
    current = start
    while True:
        yield current
        current += step

# Осторожно с бесконечными генераторами!
counter = infinite_counter(10, 2)
print("Первые 5 значений бесконечного счетчика:")
for i in range(5):
    print(next(counter), end=" ")
print()

# Использование с itertools.islice для ограничения
from itertools import islice
print("Следующие 5 значений через islice:")
for num in islice(infinite_counter(0, 5), 5):
    print(num, end=" ")
print()
Генераторы с send(), throw() и close()
python
def interactive_generator():
    """Генератор с двусторонней коммуникацией"""
    total = 0
    print("Генератор запущен")
    
    try:
        while True:
            value = yield total
            if value is not None:
                print(f"Получено значение: {value}")
                total += value
            else:
                total += 1
    except GeneratorExit:
        print("Генератор завершен")
    except ValueError as e:
        print(f"Ошибка в генераторе: {e}")
        yield "Ошибка обработана"

# Создаем генератор
gen = interactive_generator()
next(gen)  # Инициализация (доходим до первого yield)

print("Текущее значение:", gen.send(None))  # 0
print("Текущее значение:", gen.send(5))     # Получено значение: 5, затем 5
print("Текущее значение:", next(gen))       # 6 (прибавили 1)
print("Текущее значение:", gen.send(10))    # Получено значение: 10, затем 16

# Отправка исключения в генератор
print("Исключение в генератор:", gen.throw(ValueError, "Тестовая ошибка"))

# Закрытие генератора
gen.close()
print("Генератор закрыт")

# Генератор корутина
def accumulator():
    """Генератор-аккумулятор"""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value
    return total

acc = accumulator()
next(acc)  # Инициализация

acc.send(10)
acc.send(20)
acc.send(30)

try:
    acc.send(None)  # Завершаем генератор
except StopIteration as e:
    print(f"Итоговая сумма: {e.value}")  # 60
yield from - делегирование генераторов
python
def chain_generators(*iterables):
    """Объединение нескольких итерируемых объектов"""
    for iterable in iterables:
        yield from iterable  # Делегирование генерации

# Эквивалентно:
# for iterable in iterables:
#     for item in iterable:
#         yield item

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (7, 8, 9)

print("Объединенные последовательности:")
for item in chain_generators(list1, list2, tuple1):
    print(item, end=" ")
print()

# Более сложный пример
def flatten(nested_list):
    """Рекурсивное выравнивание вложенных списков"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # Рекурсивное делегирование
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print("Выровненный список:", list(flatten(nested)))

# yield from с возвращаемым значением
def subgenerator():
    yield 1
    yield 2
    return "Завершено"

def delegating_generator():
    """Генератор, делегирующий другому генератору"""
    result = yield from subgenerator()
    print(f"Результат subgenerator: {result}")
    yield 3

print("\nДелегирование с возвращаемым значением:")
for item in delegating_generator():
    print(item)
Генераторные выражения
Генераторные выражения похожи на списковые включения, но возвращают генератор вместо списка.

Синтаксис генераторных выражений
python
# Создание генераторного выражения
gen_exp = (x ** 2 for x in range(5))
print(type(gen_exp))  # <class 'generator'>

print("Квадраты чисел:")
for num in gen_exp:
    print(num, end=" ")
print()

# Сравнение с списковым включением
list_comp = [x ** 2 for x in range(5)]
gen_exp = (x ** 2 for x in range(5))

print("Список:", list_comp)  # [0, 1, 4, 9, 16]
print("Генератор:", list(gen_exp))  # [0, 1, 4, 9, 16]

# Генераторные выражения ленивые
print("\nЛенивое вычисление:")
gen = (print(f"Вычисляю {x}") or x for x in range(3))
print("Генератор создан, но ничего не вычислено")

first = next(gen)  # Вычисляю 0
print(f"Получено первое значение: {first}")

print("Остальные значения:", list(gen))

# Сложные генераторные выражения
numbers = range(10)
even_squares = (x ** 2 for x in numbers if x % 2 == 0)
print("Квадраты четных чисел:", list(even_squares))

# Вложенные генераторные выражения
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (item for row in matrix for item in row)
print("Выровненная матрица:", list(flattened))

# Генераторные выражения как аргументы функций
numbers = [1, 2, 3, 4, 5]
total = sum(x ** 2 for x in numbers)  # Не нужно дополнительные скобки!
print(f"Сумма квадратов: {total}")

max_value = max(x for x in range(10) if x % 3 == 0)
print(f"Максимум кратных 3: {max_value}")
Преимущества генераторных в