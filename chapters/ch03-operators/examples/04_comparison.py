# file: examples/04_comparison.py
marks = 72
passing = 50

print(marks > passing)
print(marks == 100)
print(marks != 0)
print(marks >= 72)

# Chained comparison: Python ki khaas khoobi
print(60 <= marks < 80)          # matlab: 60 <= marks AND marks < 80

# Strings ka muqabla (alphabetical / Unicode order)
print("apple" < "banana")
print("Zebra" < "apple")          # capital letters pehle aate hain
print("10" < "9")                 # text muqabla: pehla character '1' < '9'

# int aur float
print(5 == 5.0)
