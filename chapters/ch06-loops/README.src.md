# Chapter 6 — Loops: Kaam Ko Dohrana

> **PYTHON MASTERY** · Roman Urdu Edition · MIAVRO Systems · Part 2: Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:** `while` loop aur infinite loops · `for` loop, iterables aur `range()` · `break`, `continue`, `pass` aur loop ka `else` · nested loops · `enumerate()` aur `zip()` · loop patterns (counter, accumulator, max/min, search, flag) · `sum`, `min`, `max`, `any`, `all`
**Prerequisites:** Chapter 5
**Andaazan study time:** 4 ghante
**Mini Project 2:** Number Guessing Game

**Loop kya hai?** Loop code ke aik block ko **bar bar** chalata hai. 1 se 1000 tak numbers print karne hon to 1000 `print()` likhna pagalpan hai. Loop yeh kaam 2 lines mein kar deta hai. Har aik chakkar ko **iteration** kehte hain.

---

## 6.1 `while` Loop

**Yeh kya hai?** `while` loop tab tak chalta rehta hai **jab tak** condition `True` ho.

**Kab use karein?** Jab pehle se **maloom na ho** ke kitni dafa chalana hai: "jab tak user sahi password na de", "jab tak balance khatam na ho".

**Syntax:**
```text
while condition:
    # body
    # condition ko kabhi na kabhi False karne wala kaam
```

```python
# file: examples/01_while_count.py
count = 1                    # 1. shuruati value
while count <= 5:            # 2. condition
    print(f"Iteration {count}")
    count += 1               # 3. update: is ke baghair loop kabhi khatam nahi hoga
print("Loop khatam, count ab:", count)
```

**Output:**
```
@@OUT examples/01_while_count.py@@
```

**Har `while` loop ke 3 hisse:** (1) initialization, (2) condition, (3) update. Teesra bhool jayein to **infinite loop** ban jata hai.

**Input validation, jab tak sahi na mile:**

<!-- stdin: abc | 150 | 28 -->
```python
# file: examples/02_while_validation.py
age_text = input("Umar (1-120): ")
while not (age_text.isdigit() and 1 <= int(age_text) <= 120):
    print("  Ghalat input, dobara koshish karein.")
    age_text = input("Umar (1-120): ")

age = int(age_text)
print(f"Shukriya! Umar: {age}")
```

**Output** (user ne pehle `abc`, phir `150`, phir `28` likha):
```
@@OUT examples/02_while_validation.py@@
```

Short-circuiting ka kamaal: agar `isdigit()` `False` ho to `int(age_text)` chalta hi nahi, is liye `ValueError` nahi aata.

### Infinite loop se bachna
```text
x = 1
while x > 0:
    print(x)        # x kabhi kam nahi hota -> hamesha chalega
```
Agar program atak jaye to terminal mein **`Ctrl + C`** dabayein. Yeh `KeyboardInterrupt` bhej kar program rok deta hai.

**Jaan boojh kar infinite loop** `while True:` aur `break` (6.3) ke saath bohat aam pattern hai: menus, games, servers.

---

## 6.2 `for` Loop, Iterables Aur `range()`

**Yeh kya hai?** `for` loop kisi **iterable** ki har cheez par aik dafa chalta hai. **Iterable** woh object hai jis ki cheezein aik aik karke nikali ja sakti hain: string, list, tuple, `range`, dictionary, file.

**Kab use karein?** Jab cheezon ka majmua maujood ho, ya ginti pehle se maloom ho.

```python
# file: examples/03_for_basic.py
for letter in "PAK":
    print(letter)

cities = ["Lahore", "Karachi", "Peshawar"]
for city in cities:
    print(f"{city} mein {len(city)} huroof hain")
```

**Output:**
```
@@OUT examples/03_for_basic.py@@
```

Har iteration mein `letter` (ya `city`) **loop variable** agli cheez ki value le leta hai.

### `range(start, stop, step)`
`range()` numbers ka sequence banata hai. Slicing ki tarah **`stop` shamil nahi**.

| Code | Numbers |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 20, 5)` | 0, 5, 10, 15 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |

```python
# file: examples/04_range.py
for i in range(5):
    print(i, end=" ")
print()

for i in range(1, 11, 3):
    print(i, end=" ")
print()

for i in range(5, 0, -1):
    print(i, end="... ")
print("Liftoff!")

print(list(range(2, 12, 2)))
```

**Output:**
```
@@OUT examples/04_range.py@@
```

`list(range(...))` sirf dekhne ke liye hai. `range` khud numbers memory mein jama nahi karta, zaroorat ke waqt aik aik banata hai, is liye `range(1_000_000_000)` bhi foran ban jata hai.

**⚠ Aam Ghaltiyan**
- `range(1, 10)` se 10 ki ummeed rakhna. 10 shamil nahi. 1 se 10 tak chahiye to `range(1, 11)`.
- Loop ke andar list ko badalna jis par loop chal raha ho. Is se items skip ho jate hain (Chapter 7).
- `for i in 10:` → `TypeError: 'int' object is not iterable`. Sahi: `range(10)`.

**`while` vs `for`:**
| `for` | `while` |
|---|---|
| Iterations ki tadaad maloom ho, ya collection ho | Kisi shart par ruke |
| Infinite loop ka khatra kam | Update bhoolne ka khatra |

---

## 6.3 `break`, `continue`, `pass` Aur Loop Ka `else`

| Keyword | Kaam |
|---|---|
| `break` | Loop ko **foran khatam** kar do |
| `continue` | Is iteration ka baqi hissa chhoro, **agli iteration** par jao |
| `pass` | Kuch mat karo (khaali block ki jagah) |

```python
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
```

**Output:**
```
@@OUT examples/05_break_continue.py@@
```

### Loop ka `else` clause
Python ki aik kam-maloom khoobi. `for`/`while` ke saath `else` tab chalta hai jab loop **`break` ke baghair** poora ho jaye. Search karte waqt yeh bohat kaam aata hai.

```python
# file: examples/06_loop_else.py
roll_numbers = [101, 104, 108, 112]
target = 109

for roll in roll_numbers:
    if roll == target:
        print(f"Roll {target} mil gaya!")
        break
else:
    print(f"Roll {target} list mein nahi hai.")
```

**Output:**
```
@@OUT examples/06_loop_else.py@@
```

**💡 Ghalat Fehmi:** *"Loop ka `else` tab chalta hai jab loop aik dafa bhi na chale."* Nahi. Yeh tab chalta hai jab loop **`break` ke baghair** khatam ho, chahe zero dafa chala ho ya sau dafa. Isay **"no break"** samjhein.

---

## 6.4 Nested Loops

**Yeh kya hai?** Loop ke andar loop. Har bahar wali iteration ke liye andar wala loop **poora** chalta hai.

```python
# file: examples/07_nested.py
# Multiplication table (1-4) ka grid
for row in range(1, 5):
    for col in range(1, 5):
        print(f"{row * col:4}", end="")
    print()

print()
# Star pattern
for i in range(1, 5):
    print("*" * i)
```

**Output:**
```
@@OUT examples/07_nested.py@@
```

**Kul iterations:** bahar wala `n` dafa × andar wala `m` dafa = `n × m`. 1,000 × 1,000 = 1,000,000 iterations. Nested loops jaldi dheemay ho jate hain (Big-O, Chapter 15).

**⚠ Aam Ghalti:** `break` sirf **andar wale** loop ko todta hai, dono ko nahi. Dono loops se nikalna ho to flag variable istemal karein, ya code ko function mein rakh kar `return` karein (Chapter 9).

---

## 6.5 `enumerate()` Aur `zip()`

### `enumerate()`: index aur value aik saath
```python
# file: examples/08_enumerate.py
toppers = ["Ayesha", "Bilal", "Hira"]

# Purana tareeqa (kam Pythonic)
for i in range(len(toppers)):
    print(i, toppers[i])

# Pythonic tareeqa
for position, name in enumerate(toppers, start=1):
    print(f"#{position}: {name}")
```

**Output:**
```
@@OUT examples/08_enumerate.py@@
```

### `zip()`: kai sequences ko saath chalana
```python
# file: examples/09_zip.py
names = ["Ali", "Sara", "Usman"]
marks = [88, 92, 79]
cities = ["Lahore", "Karachi", "Multan"]

for name, mark, city in zip(names, marks, cities):
    print(f"{name:<6} {mark:>3}  {city}")

print(list(zip([1, 2, 3], ["a", "b"])))    # chhoti list par ruk jata hai
```

**Output:**
```
@@OUT examples/09_zip.py@@
```

`zip()` sab se chhoti sequence khatam hote hi ruk jata hai. Python 3.10+ mein `zip(a, b, strict=True)` lambai mukhtalif hone par error deta hai, jo data bugs pakarne mein madadgaar hai.

---

## 6.6 Loop Patterns

Taqreeban har loop in panch patterns mein se kisi aik par mabni hota hai.

```python
# file: examples/10_patterns.py
sales = [1200, 4500, 800, 4500, 3100, 650, 2900]

# 1. Counter: kitne items shart poori karte hain
big_sales = 0
for s in sales:
    if s > 3000:
        big_sales += 1
print("3000 se bari sales:", big_sales)

# 2. Accumulator: majmua jama karna
total = 0
for s in sales:
    total += s
print("Total:", total)

# 3. Max/Min tracking
highest = sales[0]
for s in sales:
    if s > highest:
        highest = s
print("Sab se bari:", highest)

# 4. Search: pehla match dhoondna
first_small = None
for s in sales:
    if s < 1000:
        first_small = s
        break
print("Pehli 1000 se kam sale:", first_small)

# 5. Flag: koi shart kabhi poori hui ya nahi
has_zero = False
for s in sales:
    if s == 0:
        has_zero = True
        break
print("Koi zero sale?", has_zero)
```

**Output:**
```
@@OUT examples/10_patterns.py@@
```

**⚠ Aam Ghaltiyan**
- Accumulator ko loop ke **andar** `total = 0` karna. Har iteration mein reset ho jayega.
- Max tracking ko `highest = 0` se shuru karna. Agar tamam values negative hon to natija ghalat aayega. Pehli value se shuru karein.

---

## 6.7 Built-ins: `sum`, `min`, `max`, `any`, `all`

Upar ke patterns itne aam hain ke Python ne inhe built-in functions bana diya:

```python
# file: examples/11_builtins.py
sales = [1200, 4500, 800, 4500, 3100, 650, 2900]

print("sum:", sum(sales))
print("min:", min(sales), "| max:", max(sales))
print("average:", round(sum(sales) / len(sales), 2))
print("koi 4000+?", any(s > 4000 for s in sales))
print("sab 500+?", all(s > 500 for s in sales))
print("min of words:", min(["Quetta", "Lahore", "Multan"]))
print("longest:", max(["Quetta", "Lahore", "Islamabad"], key=len))
```

**Output:**
```
@@OUT examples/11_builtins.py@@
```

- `any()`: koi aik bhi `True` ho to `True`. `all()`: sab `True` hon to `True`. Dono short-circuit karte hain.
- `s > 4000 for s in sales` aik **generator expression** hai (Chapter 14). Abhi itna samjhein: "har `s` ke liye yeh condition".
- `key=len`: lambai ke hisaab se muqabla karo (Chapter 9 mein `key` functions).

**Professional usool:** Pattern samajhne ke liye loop khud likhna seekhein, magar production code mein built-ins istemal karein. Woh tez hain aur ghaltiyan kam hoti hain.

---

## 🛠 Mini Project 2 — Number Guessing Game

**Requirements:**
1. Computer 1–100 ke beech random number chune
2. User ko 7 koshishein milein
3. Har ghalat guess par "Zyada" ya "Kam" ka hint
4. Ghalat input (number na ho, ya range se bahar) koshish **zaya na kare**
5. Jeetne par koshishon ki tadaad, haarne par asal number batayein

<!-- stdin: 50 | abc | 25 | 37 | 43 | 40 | 42 -->
```python
# file: examples/12_guessing_game.py
# Mini Project 2: Number Guessing Game
import random

random.seed(7)                 # sirf kitab ke output ko fix rakhne ke liye; asal game mein hata dein
MAX_ATTEMPTS = 7
secret = random.randint(1, 100)

print("=== NUMBER GUESSING GAME ===")
print(f"Maine 1 se 100 ke beech aik number socha hai. Aap ke paas {MAX_ATTEMPTS} koshishein hain.")

attempts = 0
while attempts < MAX_ATTEMPTS:
    guess_text = input(f"Koshish {attempts + 1}: ").strip()

    if not guess_text.isdigit() or not 1 <= int(guess_text) <= 100:
        print("  1 se 100 ke beech number likhein (yeh koshish gini nahi gayi).")
        continue

    guess = int(guess_text)
    attempts += 1

    if guess == secret:
        print(f"Mubarak ho! {attempts} koshishon mein sahi jawab: {secret}")
        break
    elif guess < secret:
        print("  Zyada socho ↑")
    else:
        print("  Kam socho ↓")
else:
    print(f"Koshishein khatam! Number tha: {secret}")
```

**Output:**
```
@@OUT examples/12_guessing_game.py@@
```

**Code ki wazahat:**
| Hissa | Purpose |
|---|---|
| `random.randint(1, 100)` | 1 aur 100 **dono shamil** (yahan `range` jaisa rule nahi) |
| `random.seed(7)` | Har dafa wahi "random" number. Testing aur kitab ke output ke liye |
| `continue` | Ghalat input par `attempts += 1` tak pohanche baghair dobara poocho |
| `break` | Jeetne par loop khatam, aur loop ka `else` **nahi** chalega |
| `while ... else` | 7 koshishein `break` ke baghair khatam hon to "Koshishein khatam" |

**Strategy tip:** Har dafa baqi range ka **beech** guess karein (50, phir 75...). Isay **binary search** kehte hain. 1–100 mein yeh zyada se zyada 7 koshishon mein jawab dhoond leta hai (2⁷ = 128 > 100).

**Extensions:** difficulty levels (easy 10 koshishein, hard 5), dobara khelne ka option (bahar aik aur `while` loop), best score yaad rakhna.

---

## 🌍 Real World
- **Data processing:** har row, har file, har transaction par loop. Pandas andar yahi karta hai, bohat tez shakal mein.
- **Retry logic:** "3 dafa koshish karo, phir error do". APIs aur network calls mein aam hai.
- **Menus aur games:** `while True` + `break`.
- **Reports:** `enumerate` se numbered lists, `zip` se columns jorna.

---

## Chapter Summary
1. `while`: shart par mabni. Init → condition → update. `Ctrl+C` se atka hua program rokein.
2. `for`: iterable par chalta hai. `range(start, stop, step)` mein `stop` shamil nahi.
3. `break` loop khatam karta hai, `continue` agli iteration par jata hai, `pass` kuch nahi karta. Loop ka `else` = "break nahi hua".
4. Nested loops: iterations `n × m`. `break` sirf andar wala loop todta hai.
5. `enumerate(seq, start=1)` index aur value deta hai, `zip(a, b)` sequences ko saath chalata hai.
6. Patterns: counter, accumulator, max/min, search, flag.
7. Built-ins: `sum`, `min`, `max(key=...)`, `any`, `all`.

---

## Exercises

### 🟢 Exercise 1 — Multiplication table
User se number lein aur us ka table 1 se 10 tak `7 x 1 = 7` format mein print karein.

### 🟢 Exercise 2 — Sum 1 to N
User se N lein aur 1 se N tak ka majmua loop se nikalein. Phir formula `N × (N + 1) / 2` se check karein.

### 🟢 Exercise 3 — Countdown
`while` loop se 10 se 1 tak ulti ginti, aur aakhir mein "Pakistan Zindabad!".

### 🟢 Exercise 4 — Vowel counter
User ke sentence mein vowels (a, e, i, o, u, chhote aur bare dono) ginein.

### 🟡 Exercise 5 — FizzBuzz
1 se 20 tak: 3 se divide ho to "Fizz", 5 se ho to "Buzz", dono se ho to "FizzBuzz", warna number.

### 🟡 Exercise 6 — Prime check
User se number lein aur batayein ke prime hai ya nahi. Loop ka `else` istemal karein, aur sirf `√n` tak check karein.

### 🟡 Exercise 7 — Digit sum
`while` aur `%`/`//` se kisi bhi lambai ke number ke digits ka majmua nikalein (e.g. `98765` → 35).

### 🔴 Exercise 8 — Password attempts
Sahi password `"pak@1947"` hai. User ko 3 koshishein dein. Har ghalti par baqi koshishein batayein. 3 ghaltiyon ke baad "Account locked".

### 🔴 Exercise 9 — Pyramid
User se height lein aur centered pyramid banayein (height 4):
```text
   *
  ***
 *****
*******
```

### 🔴 Exercise 10 — Sales analysis (zip + enumerate)
`months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]` aur `revenue = [120, 95, 150, 170, 80, 160]` (hazar PKR mein). Har mahina numbering ke saath print karein, sab se acha aur sab se bura mahina batayein, aur un mahinon ki ginti karein jin mein revenue pichle mahine se barha.

---

## Complete Solutions

### Solution 1
<!-- stdin: 7 -->
```python
# file: solutions/ex01_table.py
n = int(input("Number: "))
for i in range(1, 11):
    print(f"{n} x {i:>2} = {n * i:>3}")
```
```
@@OUT solutions/ex01_table.py@@
```

### Solution 2
<!-- stdin: 100 -->
```python
# file: solutions/ex02_sum_n.py
n = int(input("N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Loop se:", total)
print("Formula se:", n * (n + 1) // 2)
```
```
@@OUT solutions/ex02_sum_n.py@@
```
`n + 1` is liye kyun ke `range` ka `stop` shamil nahi. Formula mein `//` is liye ke `n × (n+1)` hamesha even hota hai, aur natija int rehna chahiye.

### Solution 3
```python
# file: solutions/ex03_countdown.py
n = 10
while n >= 1:
    print(n, end=" ")
    n -= 1
print("\nPakistan Zindabad!")
```
```
@@OUT solutions/ex03_countdown.py@@
```

### Solution 4
<!-- stdin: Allama Iqbal Ek Azeem Shayar Thay -->
```python
# file: solutions/ex04_vowels.py
sentence = input("Sentence: ")
count = 0
for ch in sentence.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
```
```
@@OUT solutions/ex04_vowels.py@@
```

### Solution 5
```python
# file: solutions/ex05_fizzbuzz.py
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz", end=" ")
    elif n % 3 == 0:
        print("Fizz", end=" ")
    elif n % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(n, end=" ")
print()
```
```
@@OUT solutions/ex05_fizzbuzz.py@@
```
`n % 15` sab se **pehle** check karna lazmi hai. Warna 15 par "Fizz" print ho kar ruk jata.

### Solution 6
<!-- stdin: 97 -->
```python
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
```
```
@@OUT solutions/ex06_prime.py@@
```
**`√n` tak kyun?** Agar `n = a × b` ho to `a` aur `b` mein se aik zaroor `√n` se chhota ya barabar hoga. 97 ke liye sirf 2 se 9 tak check karna para, 96 numbers nahi.

### Solution 7
<!-- stdin: 98765 -->
```python
# file: solutions/ex07_digit_sum.py
n = int(input("Number: "))
original = n
total = 0
while n > 0:
    total += n % 10      # aakhri digit
    n //= 10             # aakhri digit hatao
print(f"{original} ke digits ka majmua: {total}")
```
```
@@OUT solutions/ex07_digit_sum.py@@
```

### Solution 8
<!-- stdin: pakistan | Pak@1947 | 1947 -->
```python
# file: solutions/ex08_password.py
CORRECT = "pak@1947"
MAX_TRIES = 3

for attempt in range(1, MAX_TRIES + 1):
    pwd = input("Password: ")
    if pwd == CORRECT:
        print("Login kamyab!")
        break
    remaining = MAX_TRIES - attempt
    if remaining:
        print(f"  Ghalat. {remaining} koshish baqi.")
else:
    print("Account locked. Customer support se rabta karein.")
```
```
@@OUT solutions/ex08_password.py@@
```
`"Pak@1947"` capital P ki wajah se ghalat hai, kyun ke comparison case-sensitive hai.

### Solution 9
<!-- stdin: 4 -->
```python
# file: solutions/ex09_pyramid.py
height = int(input("Height: "))
for row in range(1, height + 1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
```
```
@@OUT solutions/ex09_pyramid.py@@
```
Har row mein stars `1, 3, 5, 7` (yaani `2 × row - 1`) aur spaces `3, 2, 1, 0` hote hain.

### Solution 10
```python
# file: solutions/ex10_sales_analysis.py
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [120, 95, 150, 170, 80, 160]

for i, (month, rev) in enumerate(zip(months, revenue), start=1):
    print(f"{i}. {month}: {rev}k")

best = max(zip(revenue, months))
worst = min(zip(revenue, months))
print(f"Best: {best[1]} ({best[0]}k), Worst: {worst[1]} ({worst[0]}k)")

growth_months = 0
for prev, curr in zip(revenue, revenue[1:]):
    if curr > prev:
        growth_months += 1
print("Growth wale mahine:", growth_months)
```
```
@@OUT solutions/ex10_sales_analysis.py@@
```
**Do tricks:**
- `max(zip(revenue, months))`: tuples pehli value (revenue) se compare hote hain, is liye mahina bhi saath mil jata hai.
- `zip(revenue, revenue[1:])`: list ko aik qadam aage wali apni hi copy ke saath jorna. Is tarah har `(pichla, mojooda)` jora milta hai: (120,95), (95,150), (150,170), (170,80), (80,160), aur in mein se 3 mein izafa hai.

---

## Agla Qadam
Chapter 7 mein **lists aur tuples** gehrai se: methods, slicing, copying ka bara raaz (`=` vs `.copy()` vs `deepcopy`), sorting aur list comprehensions.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
