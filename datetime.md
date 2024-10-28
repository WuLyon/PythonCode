`datetime` 是 Python 中用于处理日期和时间的模块，它提供了多种类和方法来处理日期、时间、日期时间、时区等信息。以下是 `datetime` 模块的主要内容和常见用法详解：

## 1. `datetime` 模块的主要类
`datetime` 模块包括四个主要类：
- **`datetime.date`**：表示日期（年、月、日）
- **`datetime.time`**：表示时间（时、分、秒、微秒）
- **`datetime.datetime`**：表示日期和时间（组合了 `date` 和 `time`）
- **`datetime.timedelta`**：表示两个日期或时间之间的时间差
- **`datetime.timezone`**：表示时区

## 2. `datetime.date` 类
`datetime.date` 用于表示日期，只包含年、月、日信息。

### 常见用法
```python
from datetime import date

# 获取当前日期
today = date.today()
print("Today:", today)  # 输出类似：2023-04-01

# 创建指定日期
specific_date = date(2023, 10, 28)
print("Specific date:", specific_date)  # 输出：2023-10-28

# 获取日期的年、月、日
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
```

## 3. `datetime.time` 类
`datetime.time` 用于表示时间，只包含时、分、秒和微秒信息。

### 常见用法
```python
from datetime import time

# 创建指定时间
specific_time = time(14, 30, 45, 123456)  # 时、分、秒、微秒
print("Specific time:", specific_time)  # 输出：14:30:45.123456

# 获取时间的时、分、秒、微秒
print("Hour:", specific_time.hour)
print("Minute:", specific_time.minute)
print("Second:", specific_time.second)
print("Microsecond:", specific_time.microsecond)
```

## 4. `datetime.datetime` 类
`datetime.datetime` 同时包含日期和时间信息，提供了 `date` 和 `time` 的组合功能。

### 常见用法
```python
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print("Now:", now)  # 输出类似：2023-04-01 14:30:45.123456

# 创建指定日期和时间
specific_datetime = datetime(2023, 10, 28, 14, 30, 45)
print("Specific datetime:", specific_datetime)  # 输出：2023-10-28 14:30:45

# 获取日期部分
print("Date:", now.date())  # 输出类似：2023-04-01

# 获取时间部分
print("Time:", now.time())  # 输出类似：14:30:45.123456

# 获取年、月、日、时、分、秒、微秒
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)
```

## 5. `datetime.timedelta` 类
`datetime.timedelta` 用于表示时间间隔（或时间差），可以进行日期、时间的加减运算。

### 常见用法
```python
from datetime import datetime, timedelta

# 创建时间间隔对象
delta = timedelta(days=5, hours=3, minutes=30)
print("Timedelta:", delta)  # 输出类似：5 days, 3:30:00

# 日期加减时间间隔
today = datetime.now()
future_date = today + delta
past_date = today - delta
print("Future date:", future_date)
print("Past date:", past_date)

# 两个日期的时间差
another_day = datetime(2023, 10, 28)
time_diff = today - another_day
print("Difference:", time_diff)  # 输出两个日期之间的天数和时间
```

## 6. `datetime.timezone` 类
`datetime.timezone` 用于表示时区偏移信息，可以在创建 `datetime` 对象时指定时区。

### 常见用法
```python
from datetime import datetime, timezone, timedelta

# 创建时区对象
utc_offset = timezone(timedelta(hours=8))  # 表示 UTC+8
print("UTC+8 timezone:", utc_offset)

# 创建带时区的 datetime 对象
datetime_with_timezone = datetime(2023, 10, 28, 14, 30, 0, tzinfo=utc_offset)
print("Datetime with timezone:", datetime_with_timezone)

# 获取当前 UTC 时间
now_utc = datetime.now(timezone.utc)
print("Current UTC time:", now_utc)
```

## 7. 日期与字符串之间的转换
`datetime` 提供了 `strftime()` 和 `strptime()` 方法来在日期对象和字符串之间进行转换。

### 常见用法
```python
from datetime import datetime

# 日期对象转换为字符串
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)  # 输出类似：2023-04-01 14:30:45

# 字符串转换为日期对象
date_str = "2023-10-28 14:30:45"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Date object:", date_obj)
```

- **`strftime()`**：将日期对象转换为字符串，格式符号包括：
  - `%Y`：年（四位数），如 `2023`
  - `%m`：月（两位数），如 `04`
  - `%d`：日（两位数），如 `01`
  - `%H`：小时（24小时制），如 `14`
  - `%M`：分钟，如 `30`
  - `%S`：秒，如 `45`

- **`strptime()`**：将字符串转换为日期对象，需指定字符串的日期格式。
