name = "Alice"
age = 25
height = 1.75

# Позиционные аргументы
print("Привет, {}! Тебе {} лет.".format(name, age))

# Нумерованные позиции
print("Привет, {0}! {0}, тебе {1} лет.".format(name, age))

# Именованные аргументы
print("Имя: {name}, Возраст: {age}".format(name=name, age=age))

# Комбинированный вариант
print("Имя: {0}, Возраст: {age}".format(name, age=age))

# Форматирование чисел
print("Рост: {:.2f} м".format(height))      # 1.75
print("Число: {:10d}".format(age))          # '        25'
print("Число: {:010d}".format(age))         # '0000000025'
print("Процент: {:.1%}".format(0.25))       # 25.0%

# Выравнивание
print("{:<20}".format("левое"))     # 'левое               '
print("{:>20}".format("правое"))    # '               правое'
print("{:^20}".format("центр"))     # '        центр        '