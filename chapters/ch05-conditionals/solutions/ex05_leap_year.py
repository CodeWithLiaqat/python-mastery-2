# file: solutions/ex05_leap_year.py
year = int(input("Saal: "))
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False
print(f"{year} leap year hai? {is_leap}")
