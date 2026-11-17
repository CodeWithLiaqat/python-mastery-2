# file: examples/05_break_continue.py
# break: pehla negative number milte hi ruk jao
readings = [12, 7, 9, -3, 15, 4]
for r in readings:
    if r < 0:
        print(f"Ghalat reading {r} mili. Ruk rahe hain.")
        break
    print("Reading OK:", r)

# continue: odd numbers chhor do
for n in range(1, 11):
    if n % 2 != 0:
        continue
    print(n, end=" ")
print()

# pass: abhi implement nahi kiya
for n in range(3):
    pass
print("pass ne kuch nahi kiya, magar SyntaxError bhi nahi aaya")
