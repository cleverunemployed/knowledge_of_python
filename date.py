from datetime import datetime, date, time, timedelta, timezone
import time as tm  # для модуля time

# date - только дата (год, месяц, день)
# time - только время (час, минута, секунда, микросекунда)
# datetime - и дата, и время
# timedelta - разница между двумя датами/временем
# timezone - информация о часовом поясе

from datetime import datetime, date

# Текущие дата и время
now = datetime.now()        # 2024-01-15 14:30:25.123456
today = date.today()        # 2024-01-15
current_time = now.time()   # 14:30:25.123456

print(f"Сейчас: {now}")
print(f"Сегодня: {today}")
print(f"Текущее время: {current_time}")

# Только определенные компоненты
print(f"Год: {now.year}")
print(f"Месяц: {now.month}")
print(f"День: {now.day}")
print(f"Час: {now.hour}")
print(f"Минута: {now.minute}")
print(f"Секунда: {now.second}")
print(f"Микросекунда: {now.microsecond}")
print(f"День недели: {now.weekday()}")  # 0=понедельник, 6=воскресенье
print(f"День недели ISO: {now.isoweekday()}")  # 1=понедельник, 7=воскресенье

from datetime import datetime, date, time

# Создание date (год, месяц, день)
d = date(2024, 1, 15)
print(d)  # 2024-01-15

# Создание time (час, минута, секунда, микросекунда)
t = time(14, 30, 45, 123456)
print(t)  # 14:30:45.123456

# Создание datetime
dt = datetime(2024, 1, 15, 14, 30, 45, 123456)
print(dt)  # 2024-01-15 14:30:45.123456

# Из строки (ISO 8601 формат)
dt_from_iso = datetime.fromisoformat("2024-01-15T14:30:45")
print(dt_from_iso)

# Из timestamp (количество секунд с 1 января 1970 UTC)
timestamp = 1705336225
dt_from_ts = datetime.fromtimestamp(timestamp)
print(dt_from_ts)  # 2024-01-15 14:30:25

# timestamp в миллисекундах
dt_from_ms = datetime.fromtimestamp(1705336225123 / 1000)
print(dt_from_ms)


from datetime import datetime

now = datetime.now()

# Основные спецификаторы формата
print(now.strftime("%Y-%m-%d %H:%M:%S"))       # 2024-01-15 14:30:25
print(now.strftime("%d.%m.%Y"))                # 15.01.2024
print(now.strftime("%d/%m/%y"))                # 15/01/24
print(now.strftime("%A, %d %B %Y"))            # Monday, 15 January 2024
print(now.strftime("%H:%M"))                   # 14:30
print(now.strftime("%I:%M %p"))                # 02:30 PM (12-часовой формат)

# Русские названия (требуется локаль)
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
print(now.strftime("%A, %d %B %Y"))            # понедельник, 15 января 2024

# Возвращаем обратно английскую локаль
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

# f-строки с форматированием дат (Python 3.6+)
print(f"{now:%Y-%m-%d %H:%M:%S}")
print(f"{now:%d.%m.%Y}")
print(f"{now:%A, %d %B %Y}")

from datetime import datetime, timedelta

now = datetime.now()

# Добавление интервалов
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)
in_90_minutes = now + timedelta(minutes=90)

print(f"Сейчас: {now}")
print(f"Завтра: {tomorrow}")
print(f"Через неделю: {next_week}")
print(f"Через 2 часа: {in_2_hours}")

# Вычитание интервалов
yesterday = now - timedelta(days=1)
last_month = now - timedelta(days=30)

# Комбинированные интервалы
complex_delta = timedelta(days=5, hours=3, minutes=30, seconds=45)
future_date = now + complex_delta

# Разница между датами
date1 = datetime(2024, 1, 10)
date2 = datetime(2024, 1, 15)
difference = date2 - date1
print(f"Разница: {difference}")          # 5 days, 0:00:00
print(f"Дней: {difference.days}")        # 5
print(f"Секунд: {difference.total_seconds()}")  # 432000.0

# Практический пример: возраст
birth_date = datetime(1990, 5, 15)
age_delta = now - birth_date
age_years = age_delta.days // 365
print(f"Возраст: {age_years} лет")