# file: solutions/ex02_sum_n.py
n = int(input("N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Loop se:", total)
print("Formula se:", n * (n + 1) // 2)
