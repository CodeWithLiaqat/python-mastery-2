# file: examples/09_precedence.py
print(2 + 3 * 4)          # 3*4 pehle
print((2 + 3) * 4)        # parentheses pehle
print(2 ** 3 ** 2)        # 3**2 = 9 pehle, phir 2**9
print(-3 ** 2)            # ** pehle, phir minus: -(3**2)
print((-3) ** 2)
print(10 - 4 - 3)         # baayein se daayein: (10-4)-3
print(True or False and False)   # and pehle: True or (False)

# Average ka mashhoor bug
a, b = 80, 90
print("Ghalat average:", a + b / 2)
print("Sahi average:", (a + b) / 2)
