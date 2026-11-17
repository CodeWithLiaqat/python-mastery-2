# file: solutions/ex09_seconds.py
total_seconds = int(input("Seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} ghante, {minutes} minute, {seconds} second")
