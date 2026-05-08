from datetime import datetime
from dateutil.relativedelta import relativedelta as rd

now = datetime.now()
d1, d2 = datetime(2023, 1, 1), datetime(2024, 1, 1)
birth = datetime(1995, 5, 15)
age = rd(now, birth)

print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Weekday of {d2.date()}: {d2.strftime('%A')}")
print(f"Days between {d1.date()} and {d2.date()}: {(d2 - d1).days}")
print(f"Age: {age.years}y, {age.months}m, {age.days}d")
