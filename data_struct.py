# 📌 Списки (Lists) - изменяемая последовательность

my_list = [1, 2, 3]

# append() - добавить в конец
my_list.append(4)  # [1, 2, 3, 4]

# insert() - вставить по индексу
my_list.insert(1, 10)  # [1, 10, 2, 3, 4]

# extend() - расширить другим списком
my_list.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6]

# remove() - удалить первое вхождение значения
my_list.remove(10)  # удаляет элемент 10

# pop() - удалить по индексу (по умолчанию последний)
popped = my_list.pop()  # удаляет 6, возвращает его
popped = my_list.pop(2)  # удаляет элемент с индексом 2

# del - оператор удаления
del my_list[0]  # удаляет первый элемент
del my_list[1:3]  # удаляет срезы

# clear() - очистить весь список
my_list.clear()  # []


my_list = [1, 2, 3, 4]

# Прямое присваивание по индексу
my_list[0] = 10  # [10, 2, 3, 4]

# Изменение среза
my_list[1:3] = [20, 30]  # [10, 20, 30, 4]


numbers = [3, 1, 4, 1, 5, 9]

# sort() - сортировка на месте (изменяет оригинал)
numbers.sort()  # [1, 1, 3, 4, 5, 9]
numbers.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]

# sorted() - возвращает новый отсортированный список
sorted_nums = sorted(numbers)  # оригинал не меняется

# Сортировка по ключу
words = ['яблоко', 'банан', 'Апельсин', 'вишня']
words.sort(key=str.lower)  # без учета регистра
words.sort(key=len)  # по длине строки

# 📌 Кортежи (Tuples) - неизменяемая последовательность

my_tuple = (1, 2, 3, 2)

# Элементы нельзя изменять после создания
# my_tuple[0] = 10  # Ошибка!

# Но можно создавать новые кортежи
new_tuple = my_tuple + (4, 5)  # (1, 2, 3, 2, 4, 5)

# count() - подсчет вхождений
count_2 = my_tuple.count(2)  # 2

# index() - поиск индекса элемента
idx = my_tuple.index(3)  # 2

# Сортировка через sorted()
sorted_tuple = tuple(sorted(my_tuple))  # (1, 2, 2, 3)

# 📌 Множества (Sets) - уникальные неупорядоченные элементы

my_set = {1, 2, 3}

# add() - добавить элемент
my_set.add(4)  # {1, 2, 3, 4}

# update() - добавить несколько элементов
my_set.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}

# remove() - удалить элемент (ошибка если нет)
my_set.remove(4)  # {1, 2, 3, 5, 6, 7}

# discard() - удалить элемент (без ошибки если нет)
my_set.discard(10)  # ничего не происходит

# pop() - удалить случайный элемент
elem = my_set.pop()

# clear() - очистить множество
my_set.clear()  # set()

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Объединение
union = A | B  # {1, 2, 3, 4, 5, 6}
union = A.union(B)

# Пересечение
intersection = A & B  # {3, 4}
intersection = A.intersection(B)

# Разность
difference = A - B  # {1, 2}
difference = A.difference(B)

# Симметрическая разность
sym_diff = A ^ B  # {1, 2, 5, 6}
sym_diff = A.symmetric_difference(B)

# 📌 Словари (Dictionaries) - пары ключ-значение

my_dict = {'a': 1, 'b': 2}

# Добавление/изменение
my_dict['c'] = 3  # {'a': 1, 'b': 2, 'c': 3}
my_dict['a'] = 10  # {'a': 10, 'b': 2, 'c': 3}

# setdefault() - получить значение или создать
value = my_dict.setdefault('d', 4)  # создает 'd': 4

# update() - обновить словарь
my_dict.update({'e': 5, 'f': 6})
my_dict.update([('g', 7), ('h', 8)])

# pop() - удалить по ключу
value = my_dict.pop('a')  # удаляет 'a' и возвращает значение

# popitem() - удалить последнюю пару (Python 3.7+)
key, value = my_dict.popitem()

# del - оператор удаления
del my_dict['b']

# clear() - очистить словарь
my_dict.clear()  # {}