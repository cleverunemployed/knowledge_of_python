age = 25
has_license = True
has_car = False

if (age >= 18 and has_license) and not has_car:
    print("Можно арендовать машину")
# Читается как: если возраст >= 18 И есть права И НЕТ машины

# С приоритетами
elif age >= 18 and (has_license or has_car):
    print("Может управлять транспортным средством")
    
else:
    print("Иди нахуй!")
    
    # Синтаксис: значение_если_True if условие else значение_если_False
age = 20
status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
print(f"Вы {status}")  # Вы совершеннолетний

# Эквивалентно:
if age >= 18:
    status = "совершеннолетний"
else:
    status = "несовершеннолетний"

# Пример с числами
x = 10
y = 5
max_value = x if x > y else y
print(f"Максимум: {max_value}")  # 10

# Вложенный тернарный оператор (осторожно, сложно читается!)
grade = 85
result = "Отлично" if grade >= 90 else "Хорошо" if grade >= 75 else "Удовлетворительно"
print(result)  # Хорошо


# Оператор := (морж) позволяет присваивать и проверять в одном выражении
data = "Python 3.8"

if (n := len(data)) > 10:
    print(f"Слишком длинная строка ({n} символов)")

# Без моржового оператора:
n = len(data)
if n > 10:
    print(f"Слишком длинная строка ({n} символов)")

# Полезно в циклах
while (command := input("Введите команду: ")) != "выход":
    print(f"Выполняю: {command}")