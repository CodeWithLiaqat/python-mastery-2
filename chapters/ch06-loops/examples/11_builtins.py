# file: examples/11_builtins.py
sales = [1200, 4500, 800, 4500, 3100, 650, 2900]

print("sum:", sum(sales))
print("min:", min(sales), "| max:", max(sales))
print("average:", round(sum(sales) / len(sales), 2))
print("koi 4000+?", any(s > 4000 for s in sales))
print("sab 500+?", all(s > 500 for s in sales))
print("min of words:", min(["Quetta", "Lahore", "Multan"]))
print("longest:", max(["Quetta", "Lahore", "Islamabad"], key=len))
