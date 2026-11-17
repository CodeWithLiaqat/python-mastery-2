# file: solutions/ex08_time_formatter.py
total_minutes = int(input("Total minutes: "))
days, remaining = divmod(total_minutes, 24 * 60)
hours, minutes = divmod(remaining, 60)
print(f"{total_minutes} minutes = {days} din, {hours} ghante, {minutes} minute")
