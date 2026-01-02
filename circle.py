# Поиск элемента в списке
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
search_for = 7

for num in numbers:
    if num == search_for:
        print(f"Нашли число {search_for}!")
        break  # выходим из цикла немедленно
    print(f"Проверяем {num}...")
# Если нашли 7, проверка 8, 9, 10 не произойдет

# Выход из вложенного цикла
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print("Выход из внутреннего цикла")
            break  # выходит только из внутреннего цикла
        print(f"i={i}, j={j}")

# Для выхода из всех вложенных циклов используйте флаги
should_break = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            should_break = True
            break
        print(f"i={i}, j={j}")
    if should_break:
        break
    
    # Множества (set comprehension)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}  # фигурные скобки
print(unique_squares)  # {16, 1, 9, 4} (только уникальные значения)

# Словари (dictionary comprehension)
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# С условием для словарей
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
high_scores = {name: score for name, score in student_scores.items() if score >= 90}
print(high_scores)  # {'Bob': 92, 'Diana': 95}

# Меняем ключи и значения местами
inverted = {v: k for k, v in student_scores.items()}
print(inverted)  # {85: 'Alice', 92: 'Bob', 78: 'Charlie', 95: 'Diana'}

# Матрица 3x3
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Эквивалентный код:
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j + 1)
    matrix.append(row)

# Выравнивание матрицы (преобразование в одномерный список)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Порядок вложенности важен!
# Сначала внешний цикл, потом внутренний
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# Пропуск нечетных чисел
for i in range(10):
    if i % 2 != 0:  # если число нечетное
        continue    # пропускаем оставшийся код цикла
    print(f"Четное число: {i}")
# Вывод: 0, 2, 4, 6, 8

# Обработка только валидных данных
data = [10, 0, 5, "текст", 15, None, 20]

for item in data:
    if not isinstance(item, int) or item == 0:
        continue  # пропускаем не-числа и нули
    result = 100 / item
    print(f"100 / {item} = {result:.2f}")
    
    # else выполняется, если цикл завершился НОРМАЛЬНО (без break)
# Для for
for i in range(5):
    print(i)
else:
    print("Цикл завершен без прерываний")
# Вывод: 0, 1, 2, 3, 4, "Цикл завершен без прерываний"

# Если был break, else не выполняется
for i in range(5):
    if i == 3:
        print("Нашли 3, выходим")
        break
    print(i)
else:
    print("Этот текст не выведется")
# Вывод: 0, 1, 2, "Нашли 3, выходим"

# Практический пример: проверка, найден ли элемент
numbers = [1, 2, 3, 4, 5]
search_value = 6

for num in numbers:
    if num == search_value:
        print(f"Нашли {search_value}")
        break
else:  # выполнится, если break не был вызван
    print(f"{search_value} не найден в списке")