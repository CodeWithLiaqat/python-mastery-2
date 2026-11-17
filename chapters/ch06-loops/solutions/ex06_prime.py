# file: solutions/ex06_prime.py
n = int(input("Number: "))

if n < 2:
    print(f"{n} prime nahi hai.")
else:
    divisor = 2
    while divisor * divisor <= n:          # divisor <= sqrt(n)
        if n % divisor == 0:
            print(f"{n} prime nahi; {divisor} se divide hota hai.")
            break
        divisor += 1
    else:
        print(f"{n} prime hai.")
