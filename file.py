Работа с файлами и контекстные менеджеры в Python
Содержание
Основы работы с файлами

Контекстные менеджеры

Создание собственных контекстных менеджеров

Продвинутые техники

Практические примеры

Основы работы с файлами
Открытие файлов с помощью open()
python
# Базовый синтаксис
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Простейший пример - чтение файла
file = open('example.txt', 'r')  # Открываем для чтения
content = file.read()            # Читаем весь файл
print(content)
file.close()                     # Важно закрыть файл!

# Но что если произойдет ошибка при чтении?
file = open('example.txt', 'r')
try:
    content = file.read()
    # Может произойти ошибка здесь...
    result = 10 / 0  # Искусственная ошибка
finally:
    file.close()    # Файл все равно закроется
Режимы открытия файлов
python
# 'r' - чтение (по умолчанию)
file = open('file.txt', 'r')  # Файл должен существовать

# 'w' - запись (создает или перезаписывает файл)
file = open('file.txt', 'w')  # Если файл существует, он будет перезаписан

# 'a' - добавление (добавляет в конец файла)
file = open('file.txt', 'a')  # Добавляет в конец, не перезаписывает

# 'x' - эксклюзивное создание (только если файл не существует)
try:
    file = open('new_file.txt', 'x')  # Создает новый файл
    file.write("Содержимое")
    file.close()
except FileExistsError:
    print("Файл уже существует!")

# Бинарные режимы
# 'rb' - чтение бинарного файла
# 'wb' - запись бинарного файла
# 'ab' - добавление в бинарный файл

# Комбинированные режимы
# 'r+' - чтение и запись (файл должен существовать)
# 'w+' - чтение и запись (создает или перезаписывает)
# 'a+' - чтение и добавление
Методы работы с файлами
python
# Создаем тестовый файл
with open('test.txt', 'w') as f:
    f.write("Первая строка\nВторая строка\nТретья строка\n")

# 1. read() - чтение всего файла
with open('test.txt', 'r') as f:
    content = f.read()
    print("Весь файл:")
    print(content)

# 2. readline() - чтение по одной строке
with open('test.txt', 'r') as f:
    print("\nЧтение построчно:")
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(f"1: {line1.strip()}")
    print(f"2: {line2.strip()}")
    print(f"3: {line3.strip()}")

# 3. readlines() - чтение всех строк в список
with open('test.txt', 'r') as f:
    lines = f.readlines()
    print("\nВсе строки как список:")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

# 4. Итерация по файлу (наиболее эффективно для больших файлов)
print("\nИтерация по файлу:")
with open('test.txt', 'r') as f:
    for line_number, line in enumerate(f, 1):
        print(f"{line_number}: {line.strip()}")

# 5. write() - запись строки
with open('output.txt', 'w') as f:
    f.write("Это первая строка\n")
    f.write("Это вторая строка\n")

# 6. writelines() - запись списка строк
lines_to_write = ["Строка 1\n", "Строка 2\n", "Строка 3\n"]
with open('output.txt', 'w') as f:
    f.writelines(lines_to_write)

# 7. seek() и tell() - управление позицией в файле
with open('test.txt', 'r') as f:
    print("\nИспользование seek() и tell():")
    
    # tell() - текущая позиция
    pos1 = f.tell()
    print(f"Начальная позиция: {pos1}")
    
    # Читаем 10 байт
    chunk = f.read(10)
    print(f"Прочитано: {repr(chunk)}")
    
    pos2 = f.tell()
    print(f"Позиция после чтения: {pos2}")
    
    # seek() - перемещение позиции
    f.seek(0)  # Возвращаемся в начало
    pos3 = f.tell()
    print(f"Позиция после seek(0): {pos3}")
    
    # Перемещение относительно текущей позиции
    f.seek(5, 1)  # 1 означает относительно текущей позиции
    print(f"Позиция после seek(5, 1): {f.tell()}")
    
    # Перемещение относительно конца файла
    f.seek(-10, 2)  # 2 означает относительно конца файла
    print(f"Позиция после seek(-10, 2): {f.tell()}")

# 8. flush() - принудительная запись буфера на диск
with open('buffered.txt', 'w') as f:
    f.write("Данные в буфере")
    f.flush()  # Немедленно записываем на диск
    print("\nБуфер сброшен на диск")
    # Данные теперь точно записаны, даже если программа упадет

# Очистка тестовых файлов
import os
for file in ['test.txt', 'output.txt', 'buffered.txt']:
    if os.path.exists(file):
        os.remove(file)
Кодировки и обработка ошибок
python
# Создаем файл в разных кодировках
text = "Привет, мир! Hello, world! 你好，世界！"

# UTF-8 (по умолчанию в Python 3)
with open('utf8.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# UTF-8 с BOM (Byte Order Mark)
with open('utf8_bom.txt', 'w', encoding='utf-8-sig') as f:
    f.write(text)

# Windows-1251 (кириллица)
with open('cp1251.txt', 'w', encoding='cp1251') as f:
    # Только кириллические символы
    f.write("Привет, мир!")

# Чтение с разными кодировками и обработкой ошибкок
print("Чтение файлов с разными кодировками:")

# 1. strict (по умолчанию) - выбрасывает UnicodeDecodeError
try:
    with open('cp1251.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError as e:
    print(f"1. Ошибка чтения cp1251 как utf-8: {e}")

# 2. ignore - игнорирует неверные символы
with open('cp1251.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    print(f"2. Чтение с ignore: {repr(content)}")

# 3. replace - заменяет неверные символы на �
with open('cp1251.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
    print(f"3. Чтение с replace: {repr(content)}")

# 4. backslashreplace - заменяет на escape-последовательности
with open('cp1251.txt', 'r', encoding='utf-8', errors='backslashreplace') as f:
    content = f.read()
    print(f"4. Чтение с backslashreplace: {repr(content)}")

# Автоматическое определение кодировки (используя chardet)
try:
    import chardet
    
    with open('cp1251.txt', 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        print(f"\nОпределенная кодировка: {result['encoding']} с уверенностью {result['confidence']:.2%}")
        
        # Чтение с определенной кодировкой
        text = raw_data.decode(result['encoding'])
        print(f"Текст: {text}")
except ImportError:
    print("\nУстановите chardet: pip install chardet")

# Очистка
for file in ['utf8.txt', 'utf8_bom.txt', 'cp1251.txt']:
    if os.path.exists(file):
        os.remove(file)
Работа с бинарными файлами
python
import struct

# Запись бинарных данных
with open('data.bin', 'wb') as f:
    # Записываем разные типы данных
    f.write(struct.pack('i', 42))           # int (4 байта)
    f.write(struct.pack('f', 3.14))         # float (4 байта)
    f.write(struct.pack('d', 2.71828))      # double (8 байт)
    f.write(struct.pack('10s', b'Hello'))   # строка байт (10 байт)
    f.write(struct.pack('?', True))         # bool (1 байт)

# Чтение бинарных данных
with open('data.bin', 'rb') as f:
    # Читаем в том же порядке, в котором записывали
    int_value = struct.unpack('i', f.read(4))[0]
    float_value = struct.unpack('f', f.read(4))[0]
    double_value = struct.unpack('d', f.read(8))[0]
    bytes_string = struct.unpack('10s', f.read(10))[0]
    bool_value = struct.unpack('?', f.read(1))[0]
    
    print(f"Целое число: {int_value}")
    print(f"Float: {float_value}")
    print(f"Double: {double_value}")
    print(f"Строка байт: {bytes_string}")
    print(f"Bool: {bool_value}")

# Работа с изображениями
try:
    from PIL import Image
    
    # Создаем простое изображение
    img = Image.new('RGB', (100, 100), color='red')
    img.save('test_image.png')
    
    # Читаем как бинарный файл
    with open('test_image.png', 'rb') as f:
        header = f.read(8)  # PNG заголовок
        print(f"\nPNG заголовок: {header.hex()}")
        
        # Проверяем, что это PNG
        if header == b'\x89PNG\r\n\x1a\n':
            print("Это PNG файл!")
        
        # Получаем размер файла
        f.seek(0, 2)  # Перемещаемся в конец
        file_size = f.tell()
        print(f"Размер файла: {file_size} байт")
        
except ImportError:
    print("\nУстановите Pillow: pip install Pillow")
except Exception as e:
    print(f"Ошибка работы с изображением: {e}")

# Копирование файла побайтно
def copy_file_binary(source, destination):
    """Копирование бинарного файла"""
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        chunk_size = 1024  # 1KB за раз
        while True:
            chunk = src.read(chunk_size)
            if not chunk:
                break
            dst.write(chunk)
    
    print(f"Файл {source} скопирован в {destination}")

# Создаем тестовый бинарный файл
test_data = b'\x00\x01\x02\x03' * 256  # 1KB данных
with open('source.bin', 'wb') as f:
    f.write(test_data)

# Копируем
copy_file_binary('source.bin', 'copy.bin')

# Проверяем
with open('source.bin', 'rb') as src, open('copy.bin', 'rb') as dst:
    source_data = src.read()
    dest_data = dst.read()
    print(f"\nКопирование успешно: {source_data == dest_data}")

# Очистка
for file in ['data.bin', 'test_image.png', 'source.bin', 'copy.bin']:
    if os.path.exists(file):
        os.remove(file)
Контекстные менеджеры
Что такое контекстные менеджеры?
Контекстные менеджеры - это объекты, которые определяют методы __enter__() и __exit__() для управления контекстом выполнения блока кода.

Синтаксис with
python
# Без контекстного менеджера
file = open('example.txt', 'r')
try:
    data = file.read()
    # Работа с данными
finally:
    file.close()

# С контекстным менеджером
with open('example.txt', 'r') as file:
    data = file.read()
    # Работа с данными
# Файл автоматически закрывается, даже если произошла ошибка

# Несколько контекстных менеджеров в одном выражении
with open('input.txt', 'r') as src, open('output.txt', 'w') as dst:
    data = src.read()
    dst.write(data.upper())

# Эквивалентная запись
with open('input.txt', 'r') as src:
    with open('output.txt', 'w') as dst:
        data = src.read()
        dst.write(data.upper())
Встроенные контекстные менеджеры
python
import threading
import sqlite3
import tempfile
import decimal

# 1. threading.Lock() - блокировки для многопоточности
lock = threading.Lock()

def thread_safe_operation():
    with lock:
        # Критическая секция
        print("Выполняется в одном потоке за раз")
        # Блокировка автоматически снимается после выхода из блока

# 2. sqlite3 - работа с базами данных
with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
    cursor.execute('INSERT INTO users VALUES (1, "Alice")')
    conn.commit()  # Автоматически выполняется при успешном завершении
    # При ошибке автоматически откатывается

# 3. tempfile.TemporaryFile() - временные файлы
with tempfile.TemporaryFile(mode='w+') as temp_file:
    temp_file.write("Временные данные")
    temp_file.seek(0)
    print(temp_file.read())
# Файл автоматически удаляется

# 4. decimal.localcontext() - контекст для точных вычислений
with decimal.localcontext() as ctx:
    ctx.prec = 50  # Устанавливаем точность 50 знаков
    result = decimal.Decimal(1) / decimal.Decimal(7)
    print(f"1/7 с точностью 50 знаков: {result}")

# 5. Изменение текущей директории
import os
from contextlib import redirect_stdout
import io

print("\nПеренаправление вывода:")
with redirect_stdout(io.StringIO()) as f:
    print("Этот текст не появится в консоли")
    print("Он будет захвачен в StringIO")
captured_output = f.getvalue()
print(f"Захваченный вывод: {captured_output}")
Модуль contextlib
python
from contextlib import contextmanager, closing, suppress, ExitStack
import urllib.request

# 1. @contextmanager - создание контекстных менеджеров через декоратор
@contextmanager
def timer():
    """Контекстный менеджер для замера времени"""
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Выполнение заняло {end - start:.4f} секунд")

print("Использование timer():")
with timer():
    # Имитация долгой операции
    import time
    time.sleep(0.5)
    print("Операция завершена")

# 2. closing() - для объектов с методом close()
print("\nИспользование closing():")
with closing(urllib.request.urlopen('http://python.org')) as page:
    content = page.read(100)  # Читаем первые 100 байт
    print(f"Первые 100 байт python.org: {content[:100]}")

# Без closing пришлось бы делать:
# page = urllib.request.urlopen('http://python.org')
# try:
#     content = page.read(100)
# finally:
#     page.close()

# 3. suppress() - подавление исключений
print("\nИспользование suppress():")
with suppress(FileNotFoundError):
    os.remove('non_existent_file.txt')
    print("Файл удален")  # Эта строка не выполнится, если файла нет
print("Продолжаем выполнение, даже если файла не было")

# Эквивалентно:
# try:
#     os.remove('non_existent_file.txt')
# except FileNotFoundError:
#     pass

# 4. ExitStack - динамическое управление несколькими контекстами
print("\nИспользование ExitStack():")
with ExitStack() as stack:
    # Динамически добавляем контексты
    files = [
        stack.enter_context(open(f'temp_{i}.txt', 'w'))
        for i in range(3)
    ]
    
    for i, file in enumerate(files):
        file.write(f"Данные файла {i}\n")
        print(f"Файл temp_{i}.txt создан")
    
    # Все файлы будут автоматически закрыты
print("Все файлы закрыты")

# Очистка временных файлов
for i in range(3):
    if os.path.exists(f'temp_{i}.txt'):
        os.remove(f'temp_{i}.txt')
Создание собственных контекстных менеджеров
Способ 1: Класс с методами __enter__ и __exit__
python
class FileManager:
    """Контекстный менеджер для работы с файлами с логированием"""
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
        self.log = []
    
    def __enter__(self):
        """Вызывается при входе в контекст"""
        self.log.append(f"Открытие файла {self.filename} в режиме {self.mode}")
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Вызывается при выходе из контекста"""
        if self.file:
            self.file.close()
            self.log.append(f"Файл {self.filename} закрыт")
        
        # Логирование исключения, если оно было
        if exc_type is not None:
            self.log.append(f"Произошла ошибка: {exc_type.__name__}: {exc_value}")
        
        # Вывод лога
        print("\nЛог работы с файлом:")
        for entry in self.log:
            print(f"  {entry}")
        
        # Если возвращаем True, исключение подавляется
        # Если False (по умолчанию), исключение пробрасывается дальше
        return False  # Пробрасываем исключение дальше

print("Пример использования FileManager:")
try:
    with FileManager('test_file.txt', 'w') as f:
        f.write("Тестовые данные\n")
        # Искусственная ошибка
        # result = 10 / 0
except ZeroDivisionError:
    print("Перехвачено исключение ZeroDivisionError")

# Чтение файла
with FileManager('test_file.txt', 'r') as f:
    content = f.read()
    print(f"\nСодержимое файла: {content}")

# Очистка
if os.path.exists('test_file.txt'):
    os.remove('test_file.txt')
Способ 2: Использование @contextmanager
python
from contextlib import contextmanager
import time

@contextmanager
def database_connection(db_url):
    """Контекстный менеджер для работы с БД"""
    import sqlite3
    
    print(f"Подключение к базе данных: {db_url}")
    conn = sqlite3.connect(db_url)
    
    try:
        yield conn
        # Если не было исключений, коммитим изменения
        conn.commit()
        print("Изменения зафиксированы")
    except Exception as e:
        # При ошибке откатываем изменения
        conn.rollback()
        print(f"Произошла ошибка, откат изменений: {e}")
        raise  # Пробрасываем исключение дальше
    finally:
        # Всегда закрываем соединение
        conn.close()
        print("Соединение с БД закрыто")

# Использование
print("\nИспользование database_connection():")
try:
    with database_connection(':memory:') as conn:  # In-memory база
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
        cursor.execute('INSERT INTO users VALUES (1, "Alice")')
        cursor.execute('INSERT INTO users VALUES (2, "Bob")')
        
        # Искусственная ошибка (раскомментировать для теста)
        # raise ValueError("Тестовая ошибка!")
        
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
        print(f"Результаты: {results}")
except Exception as e:
    print(f"Исключение перехвачено: {e}")

@contextmanager
def change_directory(new_dir):
    """Контекстный менеджер для временной смены рабочей директории"""
    import os
    
    original_dir = os.getcwd()
    print(f"Текущая директория: {original_dir}")
    print(f"Переход в: {new_dir}")
    
    try:
        os.chdir(new_dir)
        yield
    finally:
        print(f"Возврат в: {original_dir}")
        os.chdir(original_dir)

print("\nИспользование change_directory():")
# Создаем тестовую директорию
test_dir = 'test_folder'
os.makedirs(test_dir, exist_ok=True)

with change_directory(test_dir):
    print(f"Текущая директория внутри контекста: {os.getcwd()}")
    # Создаем файл в тестовой директории
    with open('temp.txt', 'w') as f:
        f.write("Создано в test_folder")

print(f"Текущая директория после контекста: {os.getcwd()}")

# Очистка
import shutil
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)