# file: examples/08_enumerate.py
toppers = ["Ayesha", "Bilal", "Hira"]

# Purana tareeqa (kam Pythonic)
for i in range(len(toppers)):
    print(i, toppers[i])

# Pythonic tareeqa
for position, name in enumerate(toppers, start=1):
    print(f"#{position}: {name}")
