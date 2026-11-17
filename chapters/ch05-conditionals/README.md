# Chapter 5 — Faislay Karna: Conditional Statements

> **PYTHON MASTERY** · Roman Urdu Edition · MIAVRO Systems · Part 2: Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:** `if`, `elif`, `else` · indentation aur code blocks · nested conditions aur unhe flat karna · truthy aur falsy values · ternary expression · `match-case` · input validation patterns
**Prerequisites:** Chapters 3–4 (comparison, logical operators, string methods)
**Andaazan study time:** 3 ghante

---

## 5.1 `if`, `elif`, `else` — Indentation Ki Ahmiyat

**Yeh kya hai?** Ab tak hamare programs har line upar se neeche chalate thay. **Conditional statements** program ko faisla karne dete hain: "agar yeh sach hai to yeh karo, warna woh karo."

**Zaroorat kyun?** ATM: agar PIN sahi hai to menu dikhao, warna error. Online store: agar order 5,000 se zyada hai to delivery free. Har asal program faislon se bhara hota hai.

**Syntax:**
```text
if condition:
    # condition True ho to yeh block chalega
elif doosri_condition:
    # pehli False aur yeh True ho to
else:
    # koi bhi True na ho to
```

**Kaise kaam karta hai?**
1. Python upar se har condition check karta hai.
2. **Pehli** `True` condition ka block chalata hai aur baqi sab **skip** kar deta hai.
3. Koi bhi `True` na ho to `else` chalta hai (agar maujood ho).
4. `elif` aur `else` dono optional hain. `elif` jitne chahein ho sakte hain.

**Indentation:** Python mein `:` ke baad wali lines **indent** (4 spaces) karna lazmi hai. Yahi indentation batata hai ke kaunsi lines us block ka hissa hain. Doosri languages `{ }` braces istemal karti hain, Python sirf spaces se block pehchanta hai.

```python
# file: examples/01_if_basic.py
temperature = 38

if temperature > 35:
    print("Bohat garmi hai!")
    print("Pani zyada piyein.")    # yeh bhi if ka hissa hai
print("Weather check mukammal.")   # yeh hamesha chalegi

order_total = 4200
if order_total >= 5000:
    print("Delivery FREE")
else:
    shortfall = 5000 - order_total
    print(f"Free delivery ke liye {shortfall} PKR ki aur shopping karein.")
```

**Output:**
```
Bohat garmi hai!
Pani zyada piyein.
Weather check mukammal.
Free delivery ke liye 800 PKR ki aur shopping karein.
```

### `elif` ke saath

<!-- stdin: 76 -->
```python
# file: examples/02_grades.py
marks = int(input("Marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

**Output** (marks `76`):
```
Marks (0-100): 76
Grade: B
```

**Line-by-line:** `76 >= 90` False → `76 >= 80` False → `76 >= 70` **True** → `grade = "B"`, aur baqi tamam `elif` aur `else` skip ho gaye. Isi liye `elif marks >= 70` mein `marks < 80` likhne ki zaroorat nahi. Pichli condition pehle hi yeh yaqeeni bana chuki hai.

**⚠ Aam Ghaltiyan**

```python
# file: examples/03_indent_error.py
age = 20
if age >= 18:
print("Vote de sakte hain")
```
```
  File ".../03_indent_error.py", line 4
    print("Vote de sakte hain")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 3
```

- `:` lagana bhool jana → `SyntaxError: expected ':'`.
- Tabs aur spaces mix karna. Hamesha **4 spaces** istemal karein. VS Code Tab key dabane par khud 4 spaces daal deta hai.
- Conditions ki **ghalat tarteeb**: agar `marks >= 50` sab se pehle likhein to 95 marks wale ko bhi "D" mil jayega. Sab se sakht condition pehle likhein.
- Kai alag `if` likhna jab `elif` chahiye tha. Alag `if` har dafa check hote hain, aur aik se zyada block chal sakte hain.

**💡 Ghalat Fehmi:** *"`else` ke saath bhi condition likhni parti hai."* Nahi. `else:` akela hota hai: "baqi har surat mein".

---

## 5.2 Nested Conditions Aur Unhe Flat Karna

**Nested** ka matlab hai `if` ke andar `if`.

<!-- stdin: 1234 | 15000 -->
```python
# file: examples/04_nested_atm.py
CORRECT_PIN = "1234"
balance = 25_000

pin = input("PIN: ")
if pin == CORRECT_PIN:
    amount = int(input("Kitni raqam? "))
    if amount <= balance:
        if amount % 500 == 0:
            balance -= amount
            print(f"{amount} nikal liye. Baqi: {balance}")
        else:
            print("Raqam 500 ke multiple mein honi chahiye.")
    else:
        print("Balance kaafi nahi.")
else:
    print("Ghalat PIN.")
```

**Output:**
```
PIN: 1234
Kitni raqam? 15000
15000 nikal liye. Baqi: 10000
```

Yeh kaam to karta hai, lekin teen level ki gehrai parhna mushkil hai. Isay **"arrow code"** kehte hain, kyun ke code daayein taraf teer ki tarah barhta jata hai.

### Flat karna: logical operators aur "pehle ghalat cases"
Wahi logic, behtar shakal mein:

<!-- stdin: 1234 | 15000 -->
```python
# file: examples/05_flat_atm.py
CORRECT_PIN = "1234"
balance = 25_000

pin = input("PIN: ")
amount = int(input("Kitni raqam? ")) if pin == CORRECT_PIN else 0

if pin != CORRECT_PIN:
    print("Ghalat PIN.")
elif amount > balance:
    print("Balance kaafi nahi.")
elif amount % 500 != 0:
    print("Raqam 500 ke multiple mein honi chahiye.")
else:
    balance -= amount
    print(f"{amount} nikal liye. Baqi: {balance}")
```

**Output:**
```
PIN: 1234
Kitni raqam? 15000
15000 nikal liye. Baqi: 10000
```

**Usool:** pehle **ghalat ya khaas cases** check karein, aur kamyabi wala kaam aakhir mein ho. Chapter 9 mein functions ke saath yeh pattern **early return** ban jata hai. Pehli line mein ternary expression hai, jo 5.4 mein aa raha hai.

---

## 5.3 Truthy Aur Falsy Values

**Yeh kya hai?** `if` ke baad sirf `True`/`False` hi nahi, **koi bhi value** likhi ja sakti hai. Python use `bool()` ki tarah parkhta hai.

**Falsy** (False samjhi jati hain): `False`, `None`, `0`, `0.0`, `""` (khaali string), `[]`, `()`, `{}`, `set()`, yaani khaali collections.
**Truthy:** baqi sab kuch, jaise `"0"`, `" "`, `-1`, `[0]`.

```python
# file: examples/06_truthiness.py
name = ""
items = []
discount = 0
user = None

if name:
    print(f"Hello {name}")
else:
    print("Naam khaali hai")

if not items:
    print("Cart khaali hai")

if discount:
    print("Discount laga")
else:
    print("Koi discount nahi")

if user is None:
    print("Login nahi hua")
```

**Output:**
```
Naam khaali hai
Cart khaali hai
Koi discount nahi
Login nahi hua
```

**Pythonic style:** `if name != "":` ke bajaye `if name:` likhein. `if len(items) == 0:` ke bajaye `if not items:`.

**⚠ Ahem ehtiyat:** Jab `0` aik **jaiz value** ho, to truthiness se dhoka ho sakta hai. Agar `discount = 0` ka matlab "zero discount" hai aur `None` ka matlab "abhi tay nahi", to `if discount:` dono ko aik samjhega. Aise mein wazeh likhein: `if discount is not None:`.

---

## 5.4 Conditional Expression (Ternary)

**Yeh kya hai?** Aik line mein `if/else` se **value** chunna.

**Syntax:** `value_agar_true if condition else value_agar_false`

```python
# file: examples/07_ternary.py
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)

marks = 45
print(f"Natija: {'Pass' if marks >= 50 else 'Fail'}")

items = 1
print(f"{items} item{'s' if items != 1 else ''}")

fee = 0 if age < 12 else (500 if age < 60 else 250)
print("Ticket:", fee)
```

**Output:**
```
Minor
Natija: Fail
1 item
Ticket: 500
```

**Kab use karein?** Jab sirf aik **value** chunni ho. Agar har shakh mein kai kaam karne hon to normal `if/else` likhein. Nested ternary (aakhri misaal) jaldi samajh se bahar ho jati hai, is liye sirf bohat saada cases mein istemal karein.

---

## 5.5 `match-case` — Structural Pattern Matching (Python 3.10+)

**Yeh kya hai?** Aik value ko kai **patterns** se milane ka saaf tareeqa. Jab aik hi variable ko bohat si fixed values se compare karna ho, to lambi `elif` chain ke bajaye `match` behtar parhta hai.

**Syntax:**
```text
match value:
    case pattern1:
        ...
    case pattern2 | pattern3:     # "ya"
        ...
    case _:                       # baqi sab (default)
        ...
```

<!-- stdin: 2 -->
```python
# file: examples/08_match_menu.py
print("1. Balance  2. Deposit  3. Withdraw  0. Exit")
choice = input("Option: ")

match choice:
    case "1":
        print("Aap ka balance: 25,000")
    case "2" | "3":
        action = "Deposit" if choice == "2" else "Withdraw"
        print(f"{action} screen khul rahi hai...")
    case "0":
        print("Allah Hafiz!")
    case _:
        print("Ghalat option")
```

**Output:**
```
1. Balance  2. Deposit  3. Withdraw  0. Exit
Option: 2
Deposit screen khul rahi hai...
```

### Guards aur unpacking
`match` sirf barabari nahi, **shakal (structure)** bhi match karta hai:

```python
# file: examples/09_match_patterns.py
command = "move 10 20"

match command.split():
    case ["quit"]:
        print("Band ho raha hai")
    case ["move", x, y]:
        print(f"x={x}, y={y} par ja rahe hain")
    case ["say", *words]:
        print(" ".join(words))
    case _:
        print("Command samajh nahi aayi")

temperature = 42
match temperature:
    case t if t >= 40:
        print(f"{t}°C: shadeed garmi ka alert")
    case t if t <= 0:
        print(f"{t}°C: paala")
    case t:
        print(f"{t}°C: normal")
```

**Output:**
```
x=10, y=20 par ja rahe hain
42°C: shadeed garmi ka alert
```

- `["move", x, y]`: list mein 3 cheezein hon aur pehli `"move"` ho, to baqi do `x` aur `y` mein aa jati hain.
- `*words`: baqi sab cheezein list mein.
- `case t if t >= 40`: **guard**, yaani pattern ke saath aik extra condition.

**⚠ Aam Ghaltiyan**
- Python 3.9 ya purane version par `match` → `SyntaxError`.
- `case _:` bhool jana. Phir koi pattern na mile to kuch bhi nahi hota, aur koi error bhi nahi aata.
- `case name:` likh kar samajhna ke yeh `name` variable ki value se compare karega. Asal mein aisa **har cheez match** kar leta hai aur value ko `name` mein rakh deta hai (capture pattern). Constants ko compare karna ho to dotted naam (`Color.RED`) ya literal istemal karein.

**💡 Ghalat Fehmi:** *"`match` doosri languages ke `switch` jaisa hai."* Usse bohat zyada taqatwar hai, kyun ke yeh structure aur types bhi match karta hai. Is mein fall-through bhi nahi hota: aik `case` chalne ke baad `match` khatam.

---

## 5.6 Input Validation Patterns

User hamesha woh nahi likhta jo hum chahte hain. **Validation** ka matlab hai input ko istemal se pehle jaanchna.

<!-- stdin: 25abc -->
```python
# file: examples/10_validation.py
raw = input("Umar likhein: ").strip()

if not raw:
    print("Kuch to likhein!")
elif not raw.isdigit():
    print(f"'{raw}' number nahi hai.")
else:
    age = int(raw)
    if not 1 <= age <= 120:
        print("Umar 1 se 120 ke beech honi chahiye.")
    else:
        print(f"Shukriya! Aap ki umar {age} saal hai.")
```

**Output** (user ne `25abc` likha):
```
Umar likhein: 25abc
'25abc' number nahi hai.
```

**Validation checklist:**
1. **Khaali to nahi?** `if not raw:`
2. **Sahi format?** `isdigit()`, `"@" in email`, `len()`
3. **Sahi range?** `1 <= age <= 120`
4. **Conversion sirf validation ke baad.**

Jab tak user sahi input na de, dobara poochna loops (Chapter 6) se hota hai. Har qisam ki ghalti ko sambhalna `try/except` (Chapter 12) se.

---

## Solved Example — Electricity Bill Slabs

**Masla:** Units ke hisaab se slab rate: pehle 100 units 10 PKR, agle 100 (101–200) 15 PKR, us se upar 22 PKR. 300 se zyada units par 5% surcharge.

<!-- stdin: 350 -->
```python
# file: examples/11_electricity_slabs.py
units = int(input("Units istemal: "))

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = 100 * 10 + (units - 100) * 15
else:
    bill = 100 * 10 + 100 * 15 + (units - 200) * 22

surcharge = bill * 0.05 if units > 300 else 0
total = bill + surcharge

print(f"Bill     : {bill:,.2f}")
print(f"Surcharge: {surcharge:,.2f}")
print(f"Total    : {total:,.2f}")
```

**Output** (350 units):
```
Units istemal: 350
Bill     : 5,800.00
Surcharge: 290.00
Total    : 6,090.00
```

Hisaab: 100×10 = 1,000 + 100×15 = 1,500 + 150×22 = 3,300 → 5,800. 5% surcharge = 290.

---

## 🌍 Real World
- **E-commerce:** coupon validity, free delivery, stock check
- **Banking:** transaction limits, fraud rules (`amount > 100_000 and new_device`)
- **Data Science:** Pandas mein `np.where(cond, a, b)`, jo ternary ka vectorized roop hai (Chapter 17–18)
- **APIs:** `match` se HTTP status codes ya JSON message types ko handle karna

---

## Chapter Summary
1. `if / elif / else`: pehli `True` condition ka block chalta hai, baqi skip. `:` aur 4-space indentation lazmi hain.
2. Sakht condition pehle likhein. Kai `if` aur `if/elif` mein farq samjhein.
3. Nesting kam karein: pehle ghalat cases check karein aur `and`/`or` istemal karein.
4. Falsy: `False, None, 0, 0.0, "", [], (), {}`. `if items:` Pythonic hai, magar jahan 0 jaiz value ho wahan `is not None` likhein.
5. Ternary: `a if cond else b`, sirf value chunne ke liye.
6. `match-case` (3.10+): literals, `|`, unpacking, guards, aur `case _`.
7. Validation: khaali → format → range → conversion.

---

## Exercises

### 🟢 Exercise 1 — Positive, negative ya zero
User se number lein aur batayein ke woh positive, negative ya zero hai.

### 🟢 Exercise 2 — Even/odd message
`%` aur ternary se aik line mein "Even" ya "Odd" print karein.

### 🟢 Exercise 3 — Bara number
Teen numbers lein aur `if/elif` se sab se bara number batayein. `max()` istemal na karein.

### 🟢 Exercise 4 — Login check
Username `"admin"` aur password `"miavro123"` hon to "Login kamyab" print karein, warna batayein ke username ghalat hai ya password.

### 🟡 Exercise 5 — Leap year
Saal lein aur `if/elif/else` se batayein ke leap year hai ya nahi (Chapter 3 Exercise 9 ka rule).

### 🟡 Exercise 6 — Ticket price
Umar ke hisaab se cinema ticket: 0–3 free, 4–12: 400, 13–59: 800, 60+: 500. Weekend par tamam paid tickets par 20% izafa.

### 🟡 Exercise 7 — Day name with match
1–7 ka number lein aur `match` se din ka naam batayein (1 = Monday). 6 aur 7 par "Weekend" bhi likhein.

### 🔴 Exercise 8 — BMI category
Wazan (kg) aur qad (m) lein. BMI = wazan / qad². Categories: < 18.5 Underweight, < 25 Normal, < 30 Overweight, baqi Obese. Ghalat (zero ya negative) input par message dein.

### 🔴 Exercise 9 — Triangle classifier
Teen sides lein. Pehle check karein ke triangle ban sakta hai ya nahi (har do sides ka majmua teesri se bara ho). Phir batayein: Equilateral, Isosceles ya Scalene.

### 🔴 Exercise 10 — Simple calculator with match
`"12 * 4"` jaisa input lein, `split()` karein aur `match` se `+ - * /` handle karein. Zero se taqseem aur ghalat operator par wazeh message dein.

---

## Complete Solutions

### Solution 1
<!-- stdin: -15 -->
```python
# file: solutions/ex01_sign.py
n = float(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
```
Number: -15
Negative
```

### Solution 2
<!-- stdin: 8 -->
```python
# file: solutions/ex02_even_odd.py
n = int(input("Number: "))
print("Even" if n % 2 == 0 else "Odd")
```
```
Number: 8
Even
```

### Solution 3
<!-- stdin: 45 | 92 | 67 -->
```python
# file: solutions/ex03_largest.py
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print("Sab se bara:", largest)
```
```
a: 45
b: 92
c: 67
Sab se bara: 92.0
```
`elif b >= c` mein `b >= a` dobara check karne ki zaroorat nahi. Agar `a` sab se bara nahi, to faisla sirf `b` aur `c` ke beech hai.

### Solution 4
<!-- stdin: admin | 12345 -->
```python
# file: solutions/ex04_login.py
USERNAME = "admin"
PASSWORD = "miavro123"

user = input("Username: ").strip()
pwd = input("Password: ")

if user != USERNAME:
    print("Username ghalat hai.")
elif pwd != PASSWORD:
    print("Password ghalat hai.")
else:
    print("Login kamyab!")
```
```
Username: admin
Password: 12345
Password ghalat hai.
```
> **Security note:** Asal apps mein yeh nahi bataya jata ke username ghalat hai ya password, sirf "Invalid credentials". Is tarah hackers ko yeh pata nahi chalta ke kaunse usernames maujood hain. Aur passwords kabhi code mein nahi likhe jate.

### Solution 5
<!-- stdin: 1900 -->
```python
# file: solutions/ex05_leap_year.py
year = int(input("Saal: "))
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False
print(f"{year} leap year hai? {is_leap}")
```
```
Saal: 1900
1900 leap year hai? False
```

### Solution 6
<!-- stdin: 35 | haan -->
```python
# file: solutions/ex06_ticket.py
age = int(input("Umar: "))
is_weekend = input("Weekend hai? (haan/nahi): ").strip().lower() == "haan"

if age <= 3:
    price = 0
elif age <= 12:
    price = 400
elif age <= 59:
    price = 800
else:
    price = 500

if is_weekend and price > 0:
    price *= 1.20

print(f"Ticket: {price:,.0f} PKR")
```
```
Umar: 35
Weekend hai? (haan/nahi): haan
Ticket: 960 PKR
```

### Solution 7
<!-- stdin: 6 -->
```python
# file: solutions/ex07_day_name.py
day = int(input("Din ka number (1-7): "))

match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6:
        name = "Saturday"
    case 7:
        name = "Sunday"
    case _:
        name = None

if name is None:
    print("1 se 7 ke beech number dein.")
else:
    label = " (Weekend)" if day in (6, 7) else ""
    print(name + label)
```
```
Din ka number (1-7): 6
Saturday (Weekend)
```

### Solution 8
<!-- stdin: 72 | 1.75 -->
```python
# file: solutions/ex08_bmi.py
weight = float(input("Wazan (kg): "))
height = float(input("Qad (m): "))

if weight <= 0 or height <= 0:
    print("Wazan aur qad zero se zyada hone chahiye.")
else:
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"BMI: {bmi:.1f} ({category})")
```
```
Wazan (kg): 72
Qad (m): 1.75
BMI: 23.5 (Normal)
```
`height ** 2` pehle chalta hai (precedence), is liye parentheses ki zaroorat nahi. Validation pehle hai, is liye zero se taqseem ka khatra nahi.

### Solution 9
<!-- stdin: 5 | 5 | 8 -->
```python
# file: solutions/ex09_triangle.py
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Yeh triangle nahi ban sakta.")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
```
```
Side a: 5
Side b: 5
Side c: 8
Isosceles
```

### Solution 10
<!-- stdin: 12 / 0 -->
```python
# file: solutions/ex10_calculator.py
expression = input("Expression (e.g. 12 * 4): ")

match expression.split():
    case [a, "+", b]:
        print(float(a) + float(b))
    case [a, "-", b]:
        print(float(a) - float(b))
    case [a, "*", b]:
        print(float(a) * float(b))
    case [a, "/", b]:
        if float(b) == 0:
            print("Zero se taqseem mumkin nahi.")
        else:
            print(float(a) / float(b))
    case [_, op, _]:
        print(f"'{op}' operator support nahi hota.")
    case _:
        print("Format: number operator number (spaces ke saath)")
```
```
Expression (e.g. 12 * 4): 12 / 0
Zero se taqseem mumkin nahi.
```
`case [_, op, _]` tab chalta hai jab teen hisse hon magar operator pehchana na jaye. `_` ka matlab hai "kuch bhi, mujhe parwah nahi".

---

## Agla Qadam
Chapter 6 mein **loops** seekhenge: kaam ko dohrana, user se tab tak input lena jab tak sahi na mile, aur **Mini Project 2: Number Guessing Game**.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
