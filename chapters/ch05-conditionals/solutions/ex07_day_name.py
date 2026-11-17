# file: solutions/ex07_day_name.py
day = int(input("Din ka number (1-7): "))

match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6:
        name = "Saturday"
    case 7:
        name = "Sunday"
    case _:
        name = None

if name is None:
    print("1 se 7 ke beech number dein.")
else:
    label = " (Weekend)" if day in (6, 7) else ""
    print(name + label)
