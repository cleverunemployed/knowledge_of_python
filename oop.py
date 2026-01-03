# Основы ООП в Python

## 1. Создание классов и объектов

**Класс** - это шаблон для создания объектов. **Объект** - экземпляр класса.

```python
# Создание класса
class Dog:
    # Конструктор класса (вызывается при создании объекта)
    def __init__(self, name, age):
        self.name = name  # атрибут экземпляра
        self.age = age    # атрибут экземпляра
    
    # Метод класса
    def bark(self):
        return f"{self.name} говорит: Гав!"

# Создание объектов (экземпляров класса)
dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)

print(dog1.bark())  # Бобик говорит: Гав!
print(dog2.bark())  # Шарик говорит: Гав!
```

## 2. Атрибуты и методы

**Атрибуты** - переменные, принадлежащие объекту или классу.
**Методы** - функции, принадлежащие объекту или классу.

```python
class Student:
    # Атрибут класса (общий для всех экземпляров)
    university = "Мой Университет"
    
    def __init__(self, name, student_id):
        # Атрибуты экземпляра
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    # Метод экземпляра
    def add_grade(self, grade):
        self.grades.append(grade)
    
    # Метод экземпляра
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # Статический метод (не имеет доступа к self или cls)
    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 100
    
    # Метод класса (работает с классом, а не с экземпляром)
    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name

# Использование
student1 = Student("Иван", "S001")
student1.add_grade(85)
student1.add_grade(90)
print(f"Средний балл: {student1.calculate_average()}")  # Средний балл: 87.5
print(f"Университет: {Student.university}")  # Университет: Мой Университет

# Изменение атрибута класса
Student.change_university("Новый Университет")
print(f"Университет: {Student.university}")  # Университет: Новый Университет
```

## 3. Инкапсуляция и доступ к данным

Инкапсуляция - сокрытие внутренней реализации и предоставление контролируемого доступа.

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        # Приватный атрибут (начинается с двух подчеркиваний)
        self.__balance = initial_balance
    
    # Публичный метод для доступа к приватным данным
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    # Геттер для получения баланса
    def get_balance(self):
        return self.__balance
    
    # Свойство (property) - более питонический способ
    @property
    def balance(self):
        return self.__balance
    
    @property
    def is_overdrawn(self):
        return self.__balance < 0

account = BankAccount("Иван", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Баланс: {account.get_balance()}")  # Баланс: 1300
print(f"Баланс (через property): {account.balance}")  # Баланс: 1300

# Прямой доступ к приватному атрибуту невозможен
# account.__balance  # Ошибка: AttributeError

# Но в Python приватность условна (name mangling)
# print(account._BankAccount__balance)  # Так можно, но не нужно!
```

## 4. Наследование и композиция

**Наследование** - создание нового класса на основе существующего.

```python
# Базовый (родительский) класс
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Звук животного"
    
    def move(self):
        return f"{self.name} двигается"

# Дочерний класс
class Dog(Animal):
    def __init__(self, name, breed):
        # Вызов конструктора родительского класса
        super().__init__(name)
        self.breed = breed
    
    # Переопределение метода
    def speak(self):
        return "Гав!"
    
    # Добавление нового метода
    def fetch(self, item):
        return f"{self.name} принес {item}"

# Другой дочерний класс
class Cat(Animal):
    def speak(self):
        return "Мяу!"
    
    def climb(self):
        return f"{self.name} лазает по деревьям"

# Использование
dog = Dog("Бобик", "Такса")
cat = Cat("Мурка")

print(dog.speak())  # Гав!
print(cat.speak())  # Мяу!
print(dog.fetch("мяч"))  # Бобик принес мяч
```

**Композиция** - включение объектов других классов в качестве атрибутов.

```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        return "Двигатель запущен"
    
    def stop(self):
        return "Двигатель остановлен"

class Wheel:
    def __init__(self, size):
        self.size = size
        self.pressure = 2.5
    
    def inflate(self, pressure):
        self.pressure = pressure
        return f"Давление установлено: {pressure}"

class Car:
    def __init__(self, model, engine_power):
        self.model = model
        # Композиция: Car содержит Engine и Wheels
        self.engine = Engine(engine_power)
        self.wheels = [Wheel(17) for _ in range(4)]
    
    def start(self):
        return f"{self.model}: {self.engine.start()}"
    
    def check_tires(self):
        return f"Давление в шинах: {self.wheels[0].pressure}"

car = Car("Toyota", 150)
print(car.start())  # Toyota: Двигатель запущен
print(car.check_tires())  # Давление в шинах: 2.5
```

## 5. Полиморфизм

Полиморфизм - способность объектов с одинаковым интерфейсом иметь разную реализацию.

```python
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Полиморфизм в действии
shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 7)]

for shape in shapes:
    print(f"Площадь: {shape.area():.2f}, Периметр: {shape.perimeter():.2f}")
# Вывод:
# Площадь: 20.00, Периметр: 18.00
# Площадь: 28.27, Периметр: 18.85
# Площадь: 14.00, Периметр: 18.00
```

## 6. Переопределение методов

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def description(self):
        return f"{self.brand} {self.model}"
    
    def start_engine(self):
        return "Двигатель транспортного средства запущен"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    # Переопределение метода
    def start_engine(self):
        return "Электродвигатель бесшумно запущен"
    
    # Расширение функциональности родительского метода
    def description(self):
        base_description = super().description()
        return f"{base_description} (Электромобиль, батарея: {self.battery_capacity} кВт·ч)"

car = ElectricCar("Tesla", "Model 3", 75)
print(car.description())  # Tesla Model 3 (Электромобиль, батарея: 75 кВт·ч)
print(car.start_engine())  # Электродвигатель бесшумно запущен
```

## 7. Абстрактные классы и интерфейсы

```python
from abc import ABC, abstractmethod

# Абстрактный класс
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    # Обычный метод в абстрактном классе
    def test_connection(self):
        print("Тестирование соединения...")
        self.connect()
        print("Соединение установлено")

# Конкретная реализация
class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "Подключение к MySQL базе данных"
    
    def disconnect(self):
        return "Отключение от MySQL базы данных"
    
    def execute_query(self, query):
        return f"Выполнение запроса в MySQL: {query}"

# Другая реализация
class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        return "Подключение к PostgreSQL базе данных"
    
    def disconnect(self):
        return "Отключение от PostgreSQL базы данных"
    
    def execute_query(self, query):
        return f"Выполнение запроса в PostgreSQL: {query}"

# Использование
connectors = [MySQLConnector(), PostgreSQLConnector()]
for connector in connectors:
    print(connector.connect())
    print(connector.execute_query("SELECT * FROM users"))
    print(connector.disconnect())
    print()
```

## 8. Множественное наследование

```python
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} работает"
    
    def get_salary(self):
        return f"Зарплата: {self.salary}"

class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university
    
    def study(self):
        return f"{self.name} учится в {self.university}"
    
    def take_exam(self):
        return f"{self.name} сдает экзамен"

# Множественное наследование
class WorkingStudent(Worker, Student):
    def __init__(self, name, salary, university):
        # Явный вызов конструкторов родительских классов
        Worker.__init__(self, name, salary)
        Student.__init__(self, name, university)
    
    def busy_schedule(self):
        return f"{self.name} и работает, и учится"

ws = WorkingStudent("Анна", 50000, "МГУ")
print(ws.work())  # Анна работает
print(ws.study())  # Анна учится в МГУ
print(ws.busy_schedule())  # Анна и работает, и учится
```

## 9. Решение конфликтов с помощью `super()` и порядок разрешения методов (MRO)

```python
class A:
    def method(self):
        return "Метод из класса A"

class B(A):
    def method(self):
        # Вызов метода родительского класса
        parent_result = super().method()
        return f"Метод из класса B -> {parent_result}"

class C(A):
    def method(self):
        parent_result = super().method()
        return f"Метод из класса C -> {parent_result}"

# Алмазная проблема множественного наследования
class D(B, C):
    def method(self):
        # Python использует C3 Linearization для определения MRO
        parent_result = super().method()
        return f"Метод из класса D -> {parent_result}"

# Просмотр порядка разрешения методов (MRO)
print("MRO класса D:", D.__mro__)
# MRO класса D: (<class '__main__.D'>, <class '__main__.B'>, 
# <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
print(d.method())
# Вывод: Метод из класса D -> Метод из класса B -> Метод из класса C -> Метод из класса A

# Еще один пример с явным указанием класса
class E(C, B):
    def method(self):
        # Явный вызов метода конкретного родительского класса
        c_result = C.method(self)
        b_result = B.method(self)
        return f"E: {c_result}, затем {b_result}"

print("\nMRO класса E:", E.__mro__)
# MRO класса E: (<class '__main__.E'>, <class '__main__.C'>, 
# <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

e = E()
print(e.method())
```

## Практический пример: система управления библиотекой

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False
    
    def __str__(self):
        status = "взята" if self.is_borrowed else "доступна"
        return f"{self.title} ({self.author}) - {status}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def list_borrowed_books(self):
        return [str(book) for book in self.borrowed_books]

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def list_available_books(self):
        return [str(book) for book in self.books if not book.is_borrowed]

# Использование
library = Library("Центральная библиотека")

# Добавление книг
library.add_book(Book("1984", "Джордж Оруэлл", "12345"))
library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков", "67890"))
library.add_book(Book("Преступление и наказание", "Федор Достоевский", "11223"))

# Регистрация членов
member1 = Member("Иван Иванов", "M001")
library.register_member(member1)

# Поиск и взятие книги
book = library.find_book("1984")
if book:
    member1.borrow_book(book)

print("Взятые книги:")
for book_title in member1.list_borrowed_books():
    print(f"- {book_title}")

print("\nДоступные книги:")
for book_info in library.list_available_books():
    print(f"- {book_info}")
```

## Ключевые выводы:

1. **Классы** - это шаблоны, **объекты** - их экземпляры
2. **Инкапсуляция** защищает данные через приватные атрибуты и методы
3. **Наследование** позволяет создавать иерархии классов
4. **Полиморфизм** обеспечивает единый интерфейс для разных типов
5. **Композиция** предпочтительнее наследования во многих случаях
6. **Абстрактные классы** определяют интерфейсы без реализации
7. **MRO** в Python решает проблемы алмазного наследования
8. **super()** правильно вызывает методы родительских классов

ООП в Python отличается гибкостью и минималистичным синтаксисом, что делает его мощным инструментом для создания сложных и поддерживаемых приложений.