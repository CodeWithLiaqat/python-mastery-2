# file: solutions/ex07_digit_sum.py
n = int(input("Number: "))
original = n
total = 0
while n > 0:
    total += n % 10      # aakhri digit
    n //= 10             # aakhri digit hatao
print(f"{original} ke digits ka majmua: {total}")
