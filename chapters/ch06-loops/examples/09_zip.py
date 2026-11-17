# file: examples/09_zip.py
names = ["Ali", "Sara", "Usman"]
marks = [88, 92, 79]
cities = ["Lahore", "Karachi", "Multan"]

for name, mark, city in zip(names, marks, cities):
    print(f"{name:<6} {mark:>3}  {city}")

print(list(zip([1, 2, 3], ["a", "b"])))    # chhoti list par ruk jata hai
