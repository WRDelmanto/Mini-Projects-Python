from datetime import date

born = date(1996, 1, 5)  # YYYY, MM, DD

today = date.today()

try:
    birthday = born.replace(year=today.year)
except ValueError:  # When born in Feb 29
    birthday = born.replace(year=today.year, month=born.month + 1, day=1)

if birthday > today:
    print(today.year - born.year - 1, "years")
else:
    print(today.year - born.year, "years")
