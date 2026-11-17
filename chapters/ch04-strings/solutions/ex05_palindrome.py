# file: solutions/ex05_palindrome.py
word = input("Lafz: ")
normalized = word.lower()
print(f"'{word}' palindrome hai?", normalized == normalized[::-1])
