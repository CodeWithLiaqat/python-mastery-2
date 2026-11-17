# file: solutions/ex01_name_parts.py
full_name = "muhammad ali jinnah"
proper = full_name.title()
parts = proper.split()
print(proper)
print("Pehla naam:", parts[0])
print("Aakhri naam:", parts[-1])
