
### 1. `enumerate(iterable, start=0)`

fruits = ['apple', 'banana', 'cherry']

# Без enumerate (неудобно)
for i in range(len(fruits)):
    print(i, fruits[i])

# С enumerate (элегантно!)
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Вывод:
# 0 apple
# 1 banana
# 2 cherry

# Можно начать с любого числа
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Вывод:
# 1 apple
# 2 banana
# 3 cherry


### 2. `zip(*iterables)`

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Объединение двух списков
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Вывод:
# Alice: 85
# Bob: 92
# Charlie: 78

# Можно "распаковать" zip для создания списков/словарей
zipped_list = list(zip(names, scores))  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
dict_from_zip = dict(zip(names, scores)) # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Работа с тремя и более итераторами
ages = [24, 31, 29]
for name, score, age in zip(names, scores, ages):
    print(name, score, age)


### 3. `all(iterable)`

numbers1 = [2, 4, 6, 8, 10]
numbers2 = [2, 4, 6, 7, 10]

# Все числа четные?
print(all(x % 2 == 0 for x in numbers1))  # True
print(all(x % 2 == 0 for x in numbers2))  # False (7 - нечетное)

# Проверка списка на заполненность (нет пустых строк/нулей/None)
data = ["Alice", "Bob", "Charlie"]
print(all(data))  # True, все строки непустые (а значит, истинны)

data_with_empty = ["Alice", "", "Charlie"]
print(all(data_with_empty))  # False, потому что "" - ложно


### 4. `any(iterable)`
numbers = [0, 1, 2, 3]

# Есть ли хотя бы одно истинное значение?
print(any(numbers))  # True (1, 2, 3 - истинны)

# Есть ли хотя бы одно отрицательное число?
print(any(x < 0 for x in numbers))  # False

# Поиск в строках
keywords = ['error', 'critical', 'fail']
log_message = "Process completed successfully."
print(any(keyword in log_message for keyword in keywords))  # False

log_message2 = "A critical error occurred."
print(any(keyword in log_message2 for keyword in keywords)) # True ('critical' найден)


### 5. `len(s)`

my_list = [10, 20, 30, 40, 50]
print(len(my_list))  # 5

my_string = "Hello, World!"
print(len(my_string))  # 13 (символы и знаки препинания)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # 3 (количество пар ключ-значение)

my_set = {1, 2, 3, 4, 4, 4}  # Дубликаты удаляются
print(len(my_set))  # 4


### 6. `max(iterable, *[, key, default])` / `max(arg1, arg2, *args[, key])`

numbers = [3, 1, 4, 1, 5, 9, 2]
print(max(numbers))  # 9

# max() с несколькими аргументами
print(max(10, 20, 5))  # 20

# Использование key
words = ['apple', 'banana', 'cherry', 'date']
print(max(words))  # 'date' (лексикографическое сравнение)
print(max(words, key=len))  # 'banana' (самое длинное слово)

# Поиск словаря с максимальным значением по ключу
students = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}]
print(max(students, key=lambda x: x['score']))  # {'name': 'Bob', 'score': 92}

# Использование default
empty_list = []
# print(max(empty_list))  # ValueError: max() arg is an empty sequence
print(max(empty_list, default=0))  # 0 (без ошибки!)


### 7. `min(iterable, *[, key, default])` / `min(arg1, arg2, *args[, key])`

numbers = [3, 1, 4, 1, 5, 9, 2]
print(min(numbers))  # 1

words = ['apple', 'banana', 'cherry', 'date']
print(min(words, key=len))  # 'date' (самое короткое слово)

### 8. `sum(iterable, /, start=0)`

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

# С начальным значением (start)
print(sum(numbers, start=10))  # 25 (10 + 1+2+3+4+5)

# Сумма квадратов
print(sum(x*x for x in numbers))  # 55 (1+4+9+16+25)

# Конкатенация списков с помощью sum (не самый эффективный способ, но возможный)
lists = [[1, 2], [3, 4], [5, 6]]
print(sum(lists, start=[]))  # [1, 2, 3, 4, 5, 6]
# Лучше использовать list comprehension или itertools.chain

