# file: solutions/ex09_leap_year.py
year = 2024
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 1900
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 2000
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 2026
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
