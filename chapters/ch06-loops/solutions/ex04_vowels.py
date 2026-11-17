# file: solutions/ex04_vowels.py
sentence = input("Sentence: ")
count = 0
for ch in sentence.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
