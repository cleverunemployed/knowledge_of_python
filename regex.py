# Регулярные выражения в Python: подробное руководство

Регулярные выражения (regex) - мощный инструмент для поиска, извлечения и обработки текста по шаблонам. В Python работа с ними осуществляется через модуль `re`.

## Содержание
1. [Основы синтаксиса](#основы-синтаксиса)
2. [Специальные символы](#специальные-символы)
3. [Предопределенные классы](#предопределенные-классы)
4. [Квантификаторы](#квантификаторы)
5. [Группировка](#группировка)
6. [Флаги](#флаги)
7. [Методы модуля re](#методы-модуля-re)
8. [Практические примеры](#практические-примеры)

## Основы синтаксиса

```python
import re

# Простейший пример - поиск точного совпадения
pattern = r"hello"
text = "hello world"
result = re.search(pattern, text)
print(result.group() if result else "Not found")  # hello

# Сырые строки (raw strings) - важно использовать!
# Без r обратная косая черта будет интерпретироваться как escape-последовательность
pattern = r"\d+"  # правильно
pattern = "\\d+"  # сложнее читать
```

## Специальные символы

### Основные метасимволы

```python
# . - любой символ, кроме новой строки
pattern = r"h.llo"
print(re.findall(pattern, "hello hallo h3llo h\nllo"))  
# ['hello', 'hallo', 'h3llo']

# ^ - начало строки
pattern = r"^Hello"
print(re.findall(pattern, "Hello world"))    # ['Hello']
print(re.findall(pattern, "Say Hello"))      # []

# $ - конец строки
pattern = r"world$"
print(re.findall(pattern, "Hello world"))    # ['world']
print(re.findall(pattern, "world peace"))    # []

# [] - набор символов
pattern = r"[aeiou]"  # любая гласная
print(re.findall(pattern, "hello world"))    # ['e', 'o', 'o']

pattern = r"[A-Z]"    # любая заглавная буква
print(re.findall(pattern, "Hello World"))    # ['H', 'W']

pattern = r"[0-9]"    # любая цифра
print(re.findall(pattern, "Year 2024"))      # ['2', '0', '2', '4']

# [^] - отрицание набора
pattern = r"[^aeiou]"  # любой символ, кроме гласных
print(re.findall(pattern, "hello"))          # ['h', 'l', 'l']

# | - логическое ИЛИ
pattern = r"cat|dog"
print(re.findall(pattern, "I have a cat and a dog"))  # ['cat', 'dog']

# \ - экранирование специальных символов
pattern = r"\.\*\?"  # ищем .*?
print(re.findall(pattern, "Test .*? end"))   # ['.*?']
```

## Предопределенные классы

```python
# \d - цифра [0-9]
pattern = r"\d"
print(re.findall(pattern, "Phone: 123-45-67"))  # ['1', '2', '3', '4', '5', '6', '7']

# \D - не цифра [^0-9]
pattern = r"\D"
print(re.findall(pattern, "Phone: 123-45-67"))  # ['P', 'h', 'o', 'n', 'e', ':', ' ', '-', '-']

# \w - буквенно-цифровой символ или подчеркивание [a-zA-Z0-9_]
pattern = r"\w"
print(re.findall(pattern, "User_name123!"))     # ['U', 's', 'e', 'r', '_', 'n', 'a', 'm', 'e', '1', '2', '3']

# \W - не \w [^a-zA-Z0-9_]
pattern = r"\W"
print(re.findall(pattern, "User_name123!"))     # ['!']

# \s - пробельный символ (пробел, табуляция, новая строка)
pattern = r"\s"
print(re.findall(pattern, "Hello\tWorld\n"))    # ['\t', '\n']

# \S - не пробельный символ
pattern = r"\S"
print(re.findall(pattern, "Hello\tWorld\n"))    # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# \b - граница слова
pattern = r"\bcat\b"  # слово "cat", но не "category" или "scat"
print(re.findall(pattern, "cat category scat a cat"))  # ['cat', 'cat']

# \B - не граница слова
pattern = r"\Bcat\B"  # "cat" внутри слова
print(re.findall(pattern, "category bobcat scat cat"))  # ['cat'] (только в "category")
```

## Квантификаторы

Квантификаторы определяют количество повторений.

```python
# * - 0 или более раз
pattern = r"lo*"  # l, затем o 0 или более раз
print(re.findall(pattern, "ll lol loooool"))  # ['l', 'l', 'lo', 'loooo']

# + - 1 или более раз
pattern = r"lo+"  # l, затем o 1 или более раз
print(re.findall(pattern, "ll lol loooool"))  # ['lo', 'looooo']

# ? - 0 или 1 раз
pattern = r"colou?r"  # colour или color
print(re.findall(pattern, "color colour"))  # ['color', 'colour']

# {n} - ровно n раз
pattern = r"\d{3}"  # ровно 3 цифры
print(re.findall(pattern, "12 123 1234 12345"))  # ['123', '123', '123']

# {n,} - n или более раз
pattern = r"\d{3,}"  # 3 или более цифр
print(re.findall(pattern, "12 123 1234 12345"))  # ['123', '1234', '12345']

# {n,m} - от n до m раз
pattern = r"\d{2,4}"  # от 2 до 4 цифр
print(re.findall(pattern, "1 12 123 1234 12345"))  # ['12', '123', '1234', '1234', '45']
```

### Жадные vs ленивые квантификаторы

```python
text = "<div>content1</div><div>content2</div>"

# Жадный режим (по умолчанию) - максимальное совпадение
pattern_greedy = r"<div>.*</div>"
match = re.search(pattern_greedy, text)
print("Жадный:", match.group() if match else "Not found")
# <div>content1</div><div>content2</div>

# Ленивый режим (добавляем ?) - минимальное совпадение
pattern_lazy = r"<div>.*?</div>"
matches = re.findall(pattern_lazy, text)
print("Ленивый:", matches)
# ['<div>content1</div>', '<div>content2</div>']

# Другие примеры ленивых квантификаторов
text = "aaaab"
pattern1 = r"a+"      # жадный
pattern2 = r"a+?"     # ленивый
print(re.findall(pattern1, text))  # ['aaaa']
print(re.findall(pattern2, text))  # ['a', 'a', 'a', 'a']
```

## Группировка

Группы позволяют выделять части совпадения и использовать их для замены или дальнейшей обработки.

### Простые группы

```python
# () - создание группы
pattern = r"(\d{3})-(\d{2})-(\d{2})"
text = "Phone: 123-45-67"

match = re.search(pattern, text)
if match:
    print("Полное совпадение:", match.group())      # 123-45-67
    print("Группа 1:", match.group(1))              # 123
    print("Группа 2:", match.group(2))              # 45
    print("Группа 3:", match.group(3))              # 67
    print("Все группы:", match.groups())            # ('123', '45', '67')
    
# Именованные группы (?P<name>...)
pattern = r"(?P<area>\d{3})-(?P<middle>\d{2})-(?P<end>\d{2})"
match = re.search(pattern, text)
if match:
    print("Именованные группы:", match.groupdict())  
    # {'area': '123', 'middle': '45', 'end': '67'}
    print("По имени:", match.group('area'))         # 123
```

### Группы без сохранения

```python
# (?:...) - группа без сохранения (не сохраняется в groups())
pattern = r"(?:Mr|Ms|Mrs)\. (\w+)"
text = "Mr. Smith and Ms. Johnson"

matches = re.findall(pattern, text)
print(matches)  # ['Smith', 'Johnson'] - только имена, без титулов

# Сравним с сохранением
pattern_save = r"(Mr|Ms|Mrs)\. (\w+)"
matches_save = re.findall(pattern_save, text)
print(matches_save)  # [('Mr', 'Smith'), ('Ms', 'Johnson')]
```

### Обратные ссылки

```python
# \n - ссылка на n-ную группу
pattern = r"(\w+) \1"  # повтор слова
text = "hello hello world bye bye"
matches = re.findall(pattern, text)
print(matches)  # ['hello', 'bye']

# Именованные обратные ссылки
pattern = r"(?P<word>\w+) (?P=word)"
text = "test test not match test"
matches = re.findall(pattern, text)
print(matches)  # ['test', 'test']

# Практический пример: поиск HTML тегов
pattern = r"<(\w+)>.*?</\1>"
text = "<div>Content</div><span>Text</span><div>More</div>"
matches = re.findall(pattern, text)
print("Теги:", matches)  # ['div', 'span', 'div']
```

### Условные выражения

```python
# (?(id/name)yes-pattern|no-pattern)
# Если группа найдена, ищем yes-pattern, иначе no-pattern

# Пример: проверка кода страны
pattern = r"(?:(?P<country>\+7) )?(?(country)\d{10}|\d{11})"
tests = ["+7 1234567890", "12345678901", "+1 1234567890"]

for test in tests:
    match = re.match(pattern, test)
    if match:
        print(f"Совпадение: {test} -> {match.group()}")
    else:
        print(f"Не совпало: {test}")
```

## Флаги

Флаги изменяют поведение регулярных выражений.

```python
text = "Hello\nWORLD\npython"

# re.IGNORECASE или re.I - игнорирование регистра
pattern = r"hello"
print(re.findall(pattern, text, re.I))  # ['Hello']

# re.MULTILINE или re.M - многострочный режим
# ^ и $ работают для начала/конца каждой строки
pattern = r"^\w+"
print(re.findall(pattern, text, re.M))  # ['Hello', 'WORLD', 'python']

# re.DOTALL или re.S - точка включает символ новой строки
pattern = r"Hello.*python"
print("Без DOTALL:", re.findall(pattern, text))        # []
print("С DOTALL:", re.findall(pattern, text, re.S))    # ['Hello\nWORLD\npython']

# re.VERBOSE или re.X - разрешает комментарии и пробелы
pattern = r"""
    \d{3}   # код города
    -       # дефис
    \d{2}   # первые две цифры
    -       # дефис
    \d{2}   # последние две цифры
"""
text = "Phone: 123-45-67"
match = re.search(pattern, text, re.VERBOSE)
print(match.group() if match else "Not found")  # 123-45-67

# re.ASCII или re.A - только ASCII символы для \w, \d и т.д.
text = "Hello Привет 123"
pattern = r"\w+"
print("Без ASCII:", re.findall(pattern, text))      # ['Hello', 'Привет', '123']
print("С ASCII:", re.findall(pattern, text, re.A))  # ['Hello', '123']

# Комбинация флагов
combined = re.I | re.M | re.S
pattern = r"^hello.*python$"
match = re.search(pattern, text, combined)
print("Комбинированные флаги:", match.group() if match else "Not found")
```

## Методы модуля re

### Основные методы поиска

```python
text = "Python is great. Python is powerful. Python is easy."

# re.search() - первое совпадение
match = re.search(r"Python", text)
print("search:", match.group() if match else "Not found")  # Python

# re.match() - совпадение с начала строки
match = re.match(r"Python", text)
print("match:", match.group() if match else "Not found")   # Python

match = re.match(r"great", text)
print("match (не с начала):", match.group() if match else "Not found")  # Not found

# re.findall() - все совпадения
matches = re.findall(r"Python", text)
print("findall:", matches)  # ['Python', 'Python', 'Python']

# re.finditer() - итератор с объектами Match
for match in re.finditer(r"Python", text):
    print(f"finditer: {match.group()} at {match.start()}-{match.end()}")

# re.fullmatch() - полное совпадение со всей строкой
pattern = r"\w+ \w+ \w+\."
match = re.fullmatch(pattern, "Python is great.")
print("fullmatch:", match.group() if match else "Not found")  # Python is great.

match = re.fullmatch(r"Python", text)
print("fullmatch (не вся строка):", match.group() if match else "Not found")  # Not found
```

### Методы замены и разделения

```python
# re.sub() - замена по шаблону
text = "Цена: 100 руб, скидка 20%"
result = re.sub(r"\d+", "XXX", text)
print("sub:", result)  # Цена: XXX руб, скидка XXX%

# С использованием функции для замены
def double(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double, text)
print("sub с функцией:", result)  # Цена: 200 руб, скидка 40%

# Использование групп в замене
text = "John Doe, Jane Smith"
result = re.sub(r"(\w+) (\w+)", r"\2, \1", text)
print("sub с группами:", result)  # Doe, John, Smith, Jane

# re.subn() - замена с подсчетом количества замен
result, count = re.subn(r"\d", "#", "a1b2c3")
print(f"subn: '{result}', замен: {count}")  # 'a#b#c#', замен: 3

# re.split() - разделение по шаблону
text = "apple,banana;orange grape"
result = re.split(r"[,; ]", text)
print("split:", result)  # ['apple', 'banana', 'orange', 'grape']

# С сохранением разделителя
result = re.split(r"([,;])", text)
print("split с сохранением:", result)  # ['apple', ',', 'banana', ';', 'orange grape']

# Максимальное количество разделений
result = re.split(r"[,; ]", text, maxsplit=2)
print("split с maxsplit:", result)  # ['apple', 'banana', 'orange grape']
```

### Компиляция регулярных выражений

```python
# re.compile() - компиляция шаблона для многократного использования
pattern = re.compile(r"\d{3}-\d{2}-\d{2}")
texts = ["Phone: 123-45-67", "ID: 987-65-43", "Invalid: 12-345-6"]

compiled_pattern = re.compile(r"""
    (\d{3})   # группа 1: код
    -         # дефис
    (\d{2})   # группа 2: первые две цифры
    -         # дефис
    (\d{2})   # группа 3: последние две цифры
""", re.VERBOSE)

for text in texts:
    match = compiled_pattern.search(text)
    if match:
        print(f"Найдено: {match.groups()}")
    else:
        print("Не найдено")

# Методы у скомпилированного объекта
pattern = re.compile(r"python", re.I)
text = "Python is great. python is easy."

print("findall:", pattern.findall(text))
print("search:", pattern.search(text).group())
print("match:", pattern.match(text).group() if pattern.match(text) else "No match")
print("sub:", pattern.sub("Java", text))
```

## Практические примеры

### Пример 1: Валидация email

```python
import re

def validate_email(email):
    pattern = r"""
        ^                     # начало строки
        [a-zA-Z0-9._%+-]+    # локальная часть (username)
        @                    # символ @
        [a-zA-Z0-9.-]+       # домен
        \.                   # точка
        [a-zA-Z]{2,}         # доменная зона (2+ букв)
        $                    # конец строки
    """
    
    if re.match(pattern, email, re.VERBOSE):
        return True
    return False

emails = [
    "user@example.com",
    "user.name@domain.co.uk",
    "user@localhost",
    "@domain.com",
    "user@.com",
    "user@domain.c"
]

for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
```

### Пример 2: Извлечение данных из текста

```python
import re

def extract_data(text):
    # Извлечение дат в формате DD/MM/YYYY или DD-MM-YYYY
    date_pattern = r"\b(\d{2})[/-](\d{2})[/-](\d{4})\b"
    
    # Извлечение сумм денег
    money_pattern = r"\$?(\d+(?:\.\d{2})?)\s*(?:долларов|USD|рублей|RUB)?"
    
    # Извлечение email
    email_pattern = r"\b[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b"
    
    dates = re.findall(date_pattern, text)
    money = re.findall(money_pattern, text)
    emails = re.findall(email_pattern, text)
    
    return {
        'dates': ['-'.join(date) for date in dates],  # преобразуем в YYYY-MM-DD
        'money': money,
        'emails': emails
    }

text = """
Заказ от 15/03/2024. Сумма: 100.50 долларов.
Контакты: client@example.com, support@company.com.
Доставка запланирована на 20-03-2024. Цена: 5000 рублей.
"""

result = extract_data(text)
print("Извлеченные данные:")
for key, value in result.items():
    print(f"{key}: {value}")
```

### Пример 3: Парсинг логов

```python
import re
from collections import defaultdict

def parse_logs(log_text):
    # Шаблон для логов вида: [TIMESTAMP] LEVEL: Message (User: username)
    log_pattern = r"""
        \[(?P<timestamp>[^\]]+)\]    # timestamp в квадратных скобках
        \s+                         # пробелы
        (?P<level>\w+):             # уровень лога
        \s+                         # пробелы
        (?P<message>[^\(]+)         # сообщение
        \s*                         # пробелы
        (?:\(User:\s*(?P<user>\w+)\))?  # опционально: пользователь
    """
    
    stats = defaultdict(int)
    user_activity = defaultdict(list)
    
    for line in log_text.strip().split('\n'):
        match = re.match(log_pattern, line, re.VERBOSE)
        if match:
            data = match.groupdict()
            stats[data['level']] += 1
            
            if data['user']:
                user_activity[data['user']].append({
                    'timestamp': data['timestamp'],
                    'level': data['level'],
                    'message': data['message'].strip()
                })
    
    return {
        'statistics': dict(stats),
        'user_activity': dict(user_activity)
    }

log_data = """
[2024-03-15 10:00:00] INFO: Application started (User: admin)
[2024-03-15 10:01:00] WARNING: High memory usage detected
[2024-03-15 10:02:00] ERROR: Database connection failed (User: user1)
[2024-03-15 10:03:00] INFO: Backup completed (User: admin)
[2024-03-15 10:04:00] ERROR: File not found (User: user2)
"""

result = parse_logs(log_data)
print("Статистика логов:")
for level, count in result['statistics'].items():
    print(f"  {level}: {count}")

print("\nАктивность пользователей:")
for user, activities in result['user_activity'].items():
    print(f"  {user}: {len(activities)} событий")
```

### Пример 4: Очистка и форматирование текста

```python
import re

def clean_text(text):
    # Удаление HTML тегов
    text = re.sub(r'<[^>]+>', '', text)
    
    # Замена множественных пробелов одним
    text = re.sub(r'\s+', ' ', text)
    
    # Удаление специальных символов, кроме пунктуации
    text = re.sub(r'[^\w\s.,!?\-]', '', text)
    
    # Форматирование телефонных номеров
    text = re.sub(
        r'(\+7|8)?[\s\-]?\(?(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{2})[\s\-]?(\d{2})',
        r'+7 (\2) \3-\4-\5',
        text
    )
    
    # Капитализация предложений
    sentences = re.split(r'([.!?] )', text)
    text = ''.join(sent.capitalize() for sent in sentences)
    
    return text.strip()

dirty_text = """
<p>Hello   world!!!</p> мой телефон 8(912)345-67-89 
another phone +7 999 888 77 66   CONTACT ME!!!
"""

clean = clean_text(dirty_text)
print("Очищенный текст:")
print(clean)
```

### Пример 5: Продвинутая замена с callback

```python
import re

def process_template(template, context):
    def replace_match(match):
        key = match.group(1)
        # Поддержка фильтров: ключ|фильтр
        if '|' in key:
            key, filter_name = key.split('|')
            value = context.get(key, '')
            
            # Применение фильтров
            if filter_name == 'upper':
                return str(value).upper()
            elif filter_name == 'lower':
                return str(value).lower()
            elif filter_name == 'capitalize':
                return str(value).capitalize()
            elif filter_name.startswith('default:'):
                default = filter_name.split(':', 1)[1]
                return str(value) if value else default
        else:
            value = context.get(key, '')
        
        return str(value)
    
    # Шаблон: {{ключ}} или {{ключ|фильтр}}
    pattern = r'{{(\w+(?:\|[^}]+)?)}}'
    
    return re.sub(pattern, replace_match, template)

template = """
Hello {{name|capitalize}}!

Your order {{order_id}} is {{status}}.
Total: ${{amount}}.

{% if status == 'pending' %}
Please complete your payment.
{% endif %}

Contact: {{email|lower}}
Default: {{missing|default:Not specified}}
"""

context = {
    'name': 'john doe',
    'order_id': '12345',
    'status': 'pending',
    'amount': '99.99',
    'email': 'JOHN@EXAMPLE.COM'
}

result = process_template(template, context)
print("Результат обработки шаблона:")
print(result)
```

## Советы и лучшие практики

1. **Используйте сырые строки** (префикс `r`) для регулярных выражений
2. **Компилируйте** часто используемые шаблоны
3. **Используйте VERBOSE режим** для сложных шаблонов
4. **Будьте осторожны с жадными квантификаторами**
5. **Тестируйте** регулярные выражения на разных данных
6. **Используйте онлайн-тестеры** для отладки (regex101.com, rexegg.com)
7. **Экранируйте** пользовательский ввод при использовании в regex
8. **Помните о производительности** - сложные regex могут быть медленными
9. **Рассмотрите альтернативы** - иногда простые строковые методы эффективнее
10. **Документируйте** сложные регулярные выражения

## Производительность и оптимизация

```python
import re
import time

# Пример сравнения производительности
text = "a" * 10000 + "b"

# Катастрофический backtracking
start = time.time()
pattern = r"(a+)+b"
try:
    re.match(pattern, text)
except:
    print("Catastrophic backtracking!")
print(f"Время: {time.time() - start:.4f} сек")

# Оптимизированный вариант
start = time.time()
pattern = r"a+b"
match = re.match(pattern, text)
print(f"Оптимизированный: {time.time() - start:.6f} сек")

# Использование atomic групп для предотвращения backtracking
start = time.time()
pattern = r"(?>(a+))+b"  # atomic группа
try:
    re.match(pattern, text)
except:
    print("Atomic group предотвратил backtracking!")
```

Регулярные выражения - мощный инструмент, но требующий осторожного использования. Начинайте с простых шаблонов, тестируйте на различных данных и не забывайте о читаемости кода.