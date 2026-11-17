# file: examples/13_unicode.py
greeting = "Assalam o Alaikum"
print(len(greeting))
print("Alaikum" in greeting)

emoji = "Pakistan 🇵🇰"
print(len(emoji))                 # flag do code points se banta hai

print(ord("A"), ord("a"))         # character -> Unicode number
print(chr(66), chr(9731))         # number -> character
print("café".upper())
