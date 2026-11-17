# file: examples/11_concat_join.py
first = "Sana"
last = "Malik"
print(first + " " + last)          # + se jorna
print("=" * 20)                    # * se dohrana

cities = ["Lahore", "Karachi", "Peshawar", "Quetta"]

# + loop ke saath (dheema tareeqa)
result = ""
for c in cities:
    result += c + ", "
print(result)

# join (tez aur saaf)
print(", ".join(cities))
