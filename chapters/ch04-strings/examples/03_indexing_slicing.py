# file: examples/03_indexing_slicing.py
word = "PYTHON"

print(word[0], word[5])       # pehla, aakhri
print(word[-1], word[-2])     # negative: aakhir se
print(word[0:3])              # 0,1,2 -> PYT
print(word[2:])               # index 2 se aakhir tak
print(word[:4])               # shuru se index 3 tak
print(word[::2])              # har doosra character
print(word[::-1])             # ulta (reverse)
print(word[1:100])            # slicing mein bari stop bhi chalti hai

cnic = "35202-1234567-1"
print("Area code:", cnic[:5])
print("Aakhri digit:", cnic[-1])
