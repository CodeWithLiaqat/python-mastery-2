# Chapter 3 — Operators Aur Expressions

> **PYTHON MASTERY** · Roman Urdu Edition · MIAVRO Systems · Part 1: Absolute Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:** arithmetic, assignment, comparison, logical, membership aur identity operators · operator precedence · float precision ke masle aur `round()`, `abs()`, `divmod()`
**Prerequisites:** Chapter 2 (variables, types, f-strings)
**Andaazan study time:** 3 ghante
**Mini Project 1:** Bill Splitter + Tip Calculator

**Bunyadi istilahat:**
- **Operator** woh symbol hai jo values par koi kaam karta hai (`+`, `>`, `and`).
- **Operand** woh value hai jis par kaam hota hai. `7 + 3` mein `7` aur `3` operands hain.
- **Expression** values aur operators ka woh majmua hai jo aik natija deta hai. `price * qty` aik expression hai.

---

## 3.1 Arithmetic Operators

**Yeh kya hai?** Hisaab-kitaab ke operators.

| Operator | Kaam | Misaal | Natija |
|---|---|---|---|
| `+` | Jama | `7 + 3` | `10` |
| `-` | Tafreeq | `7 - 3` | `4` |
| `*` | Zarb | `7 * 3` | `21` |
| `/` | Taqseem (hamesha float) | `7 / 2` | `3.5` |
| `//` | Floor division (neeche wala poora number) | `7 // 2` | `3` |
| `%` | Modulus (baqi/remainder) | `7 % 2` | `1` |
| `**` | Power (exponent) | `2 ** 10` | `1024` |

```python
# file: examples/01_arithmetic.py
a = 17
b = 5

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** 2 = {a ** 2}")
print(f"10 / 2 = {10 / 2}")      # / hamesha float deta hai
print(f"2 ** 0.5 = {2 ** 0.5}")  # square root
```

**Output:**
```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 2 = 289
10 / 2 = 5.0
2 ** 0.5 = 1.4142135623730951
```

**Line-by-line:**
- `17 / 5 = 3.4`: asal taqseem.
- `17 // 5 = 3`: 17 mein 5 poore **3** dafa aata hai.
- `17 % 5 = 2`: 3 dafa ke baad **2** bach jata hai. Hamesha yeh rishta sach hota hai: `(a // b) * b + (a % b) == a`, yaani `3 * 5 + 2 = 17`.
- `10 / 2 = 5.0`: poora jawab ho tab bhi `/` float deta hai.
- `2 ** 0.5`: kisi number ki power `0.5` uska square root hoti hai.

### `//` aur `%` kab kaam aate hain?
| Kaam | Code |
|---|---|
| Number even hai ya odd? | `n % 2 == 0` → even |
| Aakhri digit | `n % 10` |
| Aakhri digit hatana | `n // 10` |
| Minutes se ghante | `mins // 60`, baqi minutes `mins % 60` |
| Har teesra item | `i % 3 == 0` |

### Negative numbers ke saath `//` aur `%`
Yahan bohat se beginners (aur experienced log bhi) phans jate hain. `//` hamesha **neeche ki taraf** (minus infinity ki taraf) round karta hai, zero ki taraf nahi.

```python
# file: examples/02_negative_floor.py
print(7 // 2, 7 % 2)
print(-7 // 2, -7 % 2)
print(7 // -2, 7 % -2)
print(int(-7 / 2))   # int() zero ki taraf katta hai
```

**Output:**
```
3 1
-4 1
-4 -1
-3
```

- `-7 / 2 = -3.5`. Is se neeche wala poora number `-4` hai, `-3` nahi.
- Rishta qaim rehta hai: `-4 * 2 + 1 = -7`. Is liye `-7 % 2 = 1`.
- Python mein `%` ka natija hamesha **divisor (b) ke sign** wala hota hai.
- `int(-3.5)` → `-3`, kyun ke `int()` zero ki taraf kaat-ta hai. `//` aur `int(a / b)` negative numbers mein mukhtalif jawab dete hain.

**⚠ Aam Ghaltiyan**
- `/` ki jagah `//` chahiye tha (ya ulta). Saman ki ginti ke liye `//`, qeemat ke liye `/`.
- `^` ko power samajhna. `2 ^ 3` Python mein `1` deta hai (XOR operator). Power ke liye `**` hai.
- Zero se taqseem: `x / 0`, `x // 0` aur `x % 0` teeno `ZeroDivisionError` dete hain.

**💡 Ghalat Fehmi:** *"`//` decimal hissa hata deta hai."* Positive numbers ke liye aisa lagta hai, magar asal mein yeh **floor** leta hai. Negative numbers par farq saaf nazar aata hai.

---

## 3.2 Assignment Aur Augmented Assignment Operators

**Yeh kya hai?** `x = x + 5` itna aam hai ke iska shortcut maujood hai: `x += 5`. Isay **augmented assignment** kehte hain.

| Operator | Barabar hai | | Operator | Barabar hai |
|---|---|---|---|---|
| `x += 5` | `x = x + 5` | | `x //= 5` | `x = x // 5` |
| `x -= 5` | `x = x - 5` | | `x %= 5` | `x = x % 5` |
| `x *= 5` | `x = x * 5` | | `x **= 5` | `x = x ** 5` |
| `x /= 5` | `x = x / 5` | | | |

```python
# file: examples/03_augmented.py
balance = 10_000
print("Shuru:", balance)

balance += 2_500     # salary aayi
print("Deposit ke baad:", balance)

balance -= 4_000     # bill diya
print("Bill ke baad:", balance)

balance *= 2         # double
print("Double:", balance)

balance /= 4         # / ki wajah se float ban gaya
print("Chaar hisson mein:", balance)

name = "Ali"
name += " Khan"      # strings par bhi kaam karta hai
print(name)
```

**Output:**
```
Shuru: 10000
Deposit ke baad: 12500
Bill ke baad: 8500
Double: 17000
Chaar hisson mein: 4250.0
Ali Khan
```

**⚠ Aam Ghaltiyan**
- `x =+ 5` likhna. Yeh `x = +5` ban jata hai, yaani sirf `5` assign hota hai. Ghalti chhupi rehti hai, koi error nahi aata.
- `x++` likhna (C/JavaScript ki adat) → `SyntaxError`. Python mein `x += 1` likhein.
- Jo variable bana hi nahi us par `+=` → `NameError`. Pehle `count = 0` likhna zaroori hai.

---

## 3.3 Comparison Operators

**Yeh kya hai?** Do values ka muqabla karte hain aur jawab hamesha `bool` (`True` ya `False`) hota hai. Yahi Chapter 5 ke faislon ki bunyad hai.

| Operator | Matlab |
|---|---|
| `==` | Barabar hai |
| `!=` | Barabar nahi |
| `>`, `<` | Bara, chhota |
| `>=`, `<=` | Bara ya barabar, chhota ya barabar |

```python
# file: examples/04_comparison.py
marks = 72
passing = 50

print(marks > passing)
print(marks == 100)
print(marks != 0)
print(marks >= 72)

# Chained comparison: Python ki khaas khoobi
print(60 <= marks < 80)          # matlab: 60 <= marks AND marks < 80

# Strings ka muqabla (alphabetical / Unicode order)
print("apple" < "banana")
print("Zebra" < "apple")          # capital letters pehle aate hain
print("10" < "9")                 # text muqabla: pehla character '1' < '9'

# int aur float
print(5 == 5.0)
```

**Output:**
```
True
False
True
True
True
True
True
True
True
```

**Line-by-line:**
- `60 <= marks < 80`: math jaisa likhne ka tareeqa. Doosri languages mein `marks >= 60 and marks < 80` likhna parta.
- `"Zebra" < "apple"` → `True`: strings character-by-character **Unicode code** se compare hoti hain, aur capital letters ke codes chhote huroof se kam hain.
- `"10" < "9"` → `True`: yeh numbers nahi, text hain. Numbers ki tarah compare karna ho to pehle `int()` karein. Yeh `input()` ke saath bohat aam bug hai.

**⚠ Aam Ghalti:** `=` aur `==` mein farq. `=` assign karta hai, `==` compare karta hai. `if marks = 50:` → `SyntaxError`.

---

## 3.4 Logical Operators: `and`, `or`, `not`

**Yeh kya hai?** Kai conditions ko jorne ke operators.

| Operator | Kab `True` | Misaal |
|---|---|---|
| `and` | **Dono** conditions `True` hon | `age >= 18 and has_cnic` |
| `or` | **Koi aik** condition `True` ho | `is_weekend or is_holiday` |
| `not` | Condition ko ulat deta hai | `not is_blocked` |

**Truth table:**
| A | B | A `and` B | A `or` B | `not` A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

```python
# file: examples/05_logical.py
age = 20
has_cnic = True
balance = 0

can_open_account = age >= 18 and has_cnic
print("Account khul sakta hai?", can_open_account)

is_weekend = False
is_holiday = True
print("Chhutti?", is_weekend or is_holiday)

print("Balance khaali nahi?", not balance == 0)

# Short-circuit evaluation
x = 0
print(x != 0 and 10 / x > 1)   # pehli condition False, doosri chali hi nahi
```

**Output:**
```
Account khul sakta hai? True
Chhutti? True
Balance khaali nahi? False
False
```

### Short-circuiting
- `and`: agar pehli condition `False` hai to Python doosri **check hi nahi karta**, kyun ke jawab `False` hi hoga.
- `or`: agar pehli `True` hai to doosri skip.

Aakhri line mein `10 / x` kabhi chala hi nahi, is liye `ZeroDivisionError` nahi aaya. Yeh aik **guard** pattern hai: pehle check karo, phir khatarnak kaam karo.

### `and`/`or` hamesha `True`/`False` nahi dete
```python
# file: examples/06_and_or_values.py
print(0 or "default")
print("Ali" or "default")
print("" and "kuch")
print(5 and 10)

name = ""
display = name or "Mehmaan"
print(f"Khush aamdeed, {display}!")
```

**Output:**
```
default
Ali

10
Khush aamdeed, Mehmaan!
```

`or` pehli **truthy** value wapas deta hai (ya aakhri value). `and` pehli **falsy** value wapas deta hai (ya aakhri value). `name or "Mehmaan"` aik mashhoor idiom hai: agar naam khaali ho to default istemal karo. Truthiness Chapter 5 mein tafseel se hai.

**⚠ Aam Ghalti:** `if city == "Lahore" or "Karachi":` hamesha `True` hota hai, kyun ke `"Karachi"` khud truthy hai. Sahi: `city == "Lahore" or city == "Karachi"`, ya behtar `city in ("Lahore", "Karachi")` (agla section).

---

## 3.5 Membership (`in`, `not in`) Aur Identity (`is`, `is not`)

### Membership
`in` check karta hai ke koi cheez kisi **collection** (string, list, tuple, etc.) ke andar hai ya nahi.

```python
# file: examples/07_membership.py
email = "sana@example.com"
print("@" in email)
print(" " not in email)

big_cities = ("Karachi", "Lahore", "Faisalabad")
city = "Lahore"
print(city in big_cities)
print("lahore" in big_cities)     # case-sensitive
```

**Output:**
```
True
True
True
False
```

`("Karachi", "Lahore", "Faisalabad")` aik **tuple** hai, yaani values ka majmua (Chapter 7).

### Identity: `is` vs `==`
- `==` check karta hai ke **values barabar** hain ya nahi.
- `is` check karta hai ke dono naam **bilkul aik hi object** ki taraf ishara kar rahe hain ya nahi (yaani `id()` barabar hai).

```python
# file: examples/08_is_vs_equal.py
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # values barabar
print(a is b)    # do alag objects
print(a is c)    # c aur a aik hi object

result = None
print(result is None)   # None check ka sahi tareeqa
```

**Output:**
```
True
False
True
True
```

`[1, 2, 3]` aik **list** hai (Chapter 7). `a` aur `b` ki values aik jaisi hain, magar woh do alag objects hain.

**Kab kya istemal karein?**
- Values ka muqabla: **hamesha `==`**
- `None` check: **`is None`** / **`is not None`** (PEP 8 ki hidayat)

**💡 Ghalat Fehmi:** *"`is` aur `==` aik hi cheez hain, kyun ke `x = 5; x is 5` `True` deta hai."* Python chhote integers aur kuch strings ko memory bachane ke liye **reuse** karta hai (caching). Is liye kabhi kabhi `is` ittefaq se `True` deta hai. Yeh implementation detail hai, rule nahi. Naya Python is par `SyntaxWarning` bhi deta hai.

---

## 3.6 Operator Precedence

**Yeh kya hai?** Jab aik expression mein kai operators hon, to precedence tay karti hai ke kaunsa pehle chalega. Bilkul math ke BODMAS ki tarah.

| Tarteeb (upar = pehle) | Operators |
|---|---|
| 1 | `()` parentheses |
| 2 | `**` |
| 3 | `+x`, `-x` (unary) |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `is` |
| 7 | `not` |
| 8 | `and` |
| 9 | `or` |

Aik hi level ke operators **baayein se daayein** chalte hain. Sirf `**` **daayein se baayein** chalta hai.

```python
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
```

**Output:**
```
14
20
512
-9
9
3
True
Ghalat average: 125.0
Sahi average: 85.0
```

**Professional adat:** Agar zara bhi shak ho to **parentheses lagayein**. `(a + b) / 2` har parhne wale ke liye wazeh hai.

---

## 3.7 Float Precision, `round()`, `abs()`, `divmod()`

### `0.1 + 0.2` ka mashhoor masla

```python
# file: examples/10_float_precision.py
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

# Sahi tareeqa 1: display ke liye format
print(f"{0.1 + 0.2:.2f}")

# Sahi tareeqa 2: muqable ke liye math.isclose
import math
print(math.isclose(0.1 + 0.2, 0.3))

# round(): banker's rounding
print(round(3.14159, 2))
print(round(2.5), round(3.5), round(0.5))
print(round(1234567, -3))        # hazar tak round
```

**Output:**
```
0.30000000000000004
False
0.30
True
3.14
2 4 0
1235000
```

**Kyun hota hai?** Computer numbers ko **binary** (0 aur 1) mein rakhta hai. Jaise `1/3` decimal mein `0.3333...` kabhi khatam nahi hota, waise hi `0.1` binary mein kabhi khatam nahi hota. Computer use qareebi value par rok deta hai, aur yeh chhota sa farq jama ho kar `0.30000000000000004` ban jata hai. Yeh Python ka bug nahi. Har language (JavaScript, Java, C) mein yahi hota hai.

**`round()` ka raaz:** `round(2.5)` → `2`, magar `round(3.5)` → `4`. Python **banker's rounding** (round half to even) istemal karta hai: jab value bilkul beech mein ho to qareebi **even** number chuna jata hai. Is se bare datasets mein rounding ka jhukao (bias) khatam hota hai.

**Paise ka hisaab:** asal financial software mein `decimal.Decimal` ya paise ko poore number (paisa/cents) mein rakha jata hai. Is kitab ke examples mein display ke liye `:.2f` kaafi hai.

### `abs()` aur `divmod()`

```python
# file: examples/11_abs_divmod.py
temperature_change = -7.5
print(abs(temperature_change))           # sign hata deta hai

minutes = 135
hours, mins = divmod(minutes, 60)        # (//, %) aik saath
print(f"{minutes} minutes = {hours} ghante {mins} minute")
print(divmod(17, 5))
```

**Output:**
```
7.5
135 minutes = 2 ghante 15 minute
(3, 2)
```

`divmod(a, b)` aik saath `(a // b, a % b)` deta hai. Natija tuple hai, jise hum ne seedha do variables mein unpack kar liya (Chapter 2.8).

**⚠ Aam Ghaltiyan**
- Floats ko `==` se compare karna. `math.isclose()` istemal karein.
- `round()` ko hamesha "aadha upar" samajhna.
- Display ke liye `round()` lagana jab `:.2f` chahiye tha. `round(2.50, 2)` → `2.5` dikhata hai, jab ke `f"{2.5:.2f}"` → `2.50`.

---

## 🛠 Mini Project 1 — Bill Splitter + Tip Calculator

**Masla:** Doston ka group restaurant gaya. Program bill ki raqam, tip ka percentage aur logon ki ginti le, aur bataye ke har aik ne kitna dena hai.

**Requirements:**
1. Inputs: bill amount (PKR), tip %, logon ki ginti
2. Tip, total aur per-person hissa calculate ho
3. Per-person raqam ko **poore rupee mein upar** round karein (koi kam na de), aur batayein ke is tarah kitne rupee extra jama honge
4. Professional, aligned output

<!-- stdin: 7850 | 10 | 4 -->
```python
# file: examples/12_bill_splitter.py
# Mini Project 1: Bill Splitter + Tip Calculator
import math

print("=" * 38)
print("      BILL SPLITTER + TIP CALCULATOR")
print("=" * 38)

bill = float(input("Bill ki raqam (PKR): "))
tip_percent = float(input("Tip kitne percent? "))
people = int(input("Kitne log? "))

tip = bill * tip_percent / 100
total = bill + tip
exact_share = total / people
rounded_share = math.ceil(exact_share)         # upar ki taraf round
collected = rounded_share * people
extra = collected - total

print("-" * 38)
print(f"Bill          : PKR {bill:>12,.2f}")
print(f"Tip ({tip_percent:.0f}%)     : PKR {tip:>12,.2f}")
print(f"Total         : PKR {total:>12,.2f}")
print("-" * 38)
print(f"Har aik ka hissa (exact) : {exact_share:,.2f}")
print(f"Har aik dega (rounded)   : {rounded_share:,}")
print(f"Jama hoga                : {collected:,}")
print(f"Extra (waiter ke liye)   : {extra:,.2f}")
print("=" * 38)
```

**Output** (bill `7850`, tip `10`%, `4` log):
```
======================================
      BILL SPLITTER + TIP CALCULATOR
======================================
Bill ki raqam (PKR): 7850
Tip kitne percent? 10
Kitne log? 4
--------------------------------------
Bill          : PKR     7,850.00
Tip (10%)     : PKR       785.00
Total         : PKR     8,635.00
--------------------------------------
Har aik ka hissa (exact) : 2,158.75
Har aik dega (rounded)   : 2,159
Jama hoga                : 8,636
Extra (waiter ke liye)   : 1.00
======================================
```

**Code ki wazahat:**
| Line | Purpose |
|---|---|
| `import math` | `math.ceil()` ke liye: yeh hamesha **upar** wala poora number deta hai |
| `tip = bill * tip_percent / 100` | Percentage formula. Precedence: `*` aur `/` baayein se daayein |
| `math.ceil(exact_share)` | `2158.75` → `2159`. `round()` yahan ghalat hota, kyun ke woh neeche bhi ja sakta hai |
| `extra = collected - total` | Rounding se kitna zyada jama hua |
| `{bill:>12,.2f}` | `>12`: 12 characters ki jagah mein **daayein** align. `,`: comma. `.2f`: 2 decimals |

**Extensions (khud try karein):**
1. Sales tax (e.g. 16%) bhi shamil karein.
2. Agar koi aik dost dawat de raha ho to `people - 1` mein taqseem karein.
3. Validation (zero log) Chapter 5 ke baad shamil karein.

---

## 🌍 Real World
- **`%` operator:** pagination (har page par 10 items), even/odd rows ki coloring, aur time conversion.
- **Short-circuit guards:** `user is not None and user.is_active` web apps mein har jagah milta hai.
- **Float precision:** financial apps `Decimal` istemal karti hain. Data Science mein `np.isclose()` (Chapter 17).
- **`math.ceil`:** kitni buses chahiye (`ceil(students / 50)`), kitne pages print honge, wagaira.

---

## Chapter Summary
1. `/` hamesha float deta hai. `//` floor (neeche) leta hai. `%` baqi deta hai, aur us ka sign divisor jaisa hota hai.
2. `x += 1` shortcut hai. `x++` Python mein nahi hai.
3. Comparisons `bool` dete hain. Chained comparison `a < x < b` istemal karein. String comparison text ki tarah hoti hai.
4. `and`/`or` short-circuit karte hain aur asal operand wapas dete hain (`name or "default"`).
5. `in` membership check karta hai. Values ke liye `==`, `None` ke liye `is`.
6. Precedence: `()` → `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`. Shak ho to parentheses.
7. `0.1 + 0.2 != 0.3`. `math.isclose()` aur formatting istemal karein. `round()` banker's rounding karta hai.

---

## Exercises

### 🟢 Exercise 1 — Calculator
Do numbers user se lein aur saton arithmetic operators ke natije f-string mein print karein.

### 🟢 Exercise 2 — Even ya odd
User se number lein aur `%` se check karke `True`/`False` print karein ke number even hai ya nahi.

### 🟢 Exercise 3 — Predict
Chalane se pehle natije likhein: `15 // 4`, `15 % 4`, `-15 // 4`, `2 ** 3 ** 2`, `10 - 2 * 3`, `not 5 > 3`.

### 🟢 Exercise 4 — Savings tracker
`savings = 0` se shuru karein. Augmented operators se: 15,000 jama karein, 3,500 nikalein, 10% munafa (`*=`) shamil karein. Har step print karein.

### 🟡 Exercise 5 — Digits ka khel
User se 3-digit number lein (e.g. `472`). `//` aur `%` se teeno digits alag karein aur un ka majmua (sum) nikalein.

### 🟡 Exercise 6 — Eligibility checker
Scholarship ke liye: umar 16 se 25 ke beech **aur** marks 80 ya zyada **ya** sports quota (`True`/`False`). User se teeno lein aur eligibility print karein. Parentheses ka khayal rakhein.

### 🟡 Exercise 7 — Bug hunter
```text
total_marks = 450
obtained = 380
percentage = obtained / total_marks * 100
print(f"Percentage: {percentage}")
print(percentage == 84.44)
city = "Quetta"
print(city == "Lahore" or "Karachi")
```
Do logical/float masle dhoondein aur theek karein.

### 🔴 Exercise 8 — Time formatter
User se total minutes lein (e.g. `2895`) aur `divmod` istemal karke din, ghante aur minute nikalein.

### 🔴 Exercise 9 — Leap year (sirf operators se)
Saal leap year hai agar woh 4 se divide ho **aur** 100 se na ho, **ya** 400 se divide ho. `if` istemal kiye baghair sirf aik boolean expression likhein aur 2024, 1900, 2000, 2026 test karein.

### 🔴 Exercise 10 — Electricity unit cost
Bill = units × rate + 17% tax. Units aur rate user se lein. Total ko `math.ceil` se upar round karein aur batayein ke 500 ke notes mein kitne note lagenge aur kitna baqi bachega (`divmod`).

---

## Complete Solutions

### Solution 1
<!-- stdin: 23 | 4 -->
```python
# file: solutions/ex01_calculator.py
a = int(input("Pehla number: "))
b = int(input("Doosra number: "))
print(f"+ : {a + b}")
print(f"- : {a - b}")
print(f"* : {a * b}")
print(f"/ : {a / b:.2f}")
print(f"//: {a // b}")
print(f"% : {a % b}")
print(f"**: {a ** b}")
```
```
Pehla number: 23
Doosra number: 4
+ : 27
- : 19
* : 92
/ : 5.75
//: 5
% : 3
**: 279841
```

### Solution 2
<!-- stdin: 47 -->
```python
# file: solutions/ex02_even_odd.py
n = int(input("Number: "))
is_even = n % 2 == 0
print(f"{n} even hai? {is_even}")
```
```
Number: 47
47 even hai? False
```
Precedence: `%` pehle chalta hai, phir `==`.

### Solution 3
```python
# file: solutions/ex03_predict.py
print(15 // 4, 15 % 4, -15 // 4, 2 ** 3 ** 2, 10 - 2 * 3, not 5 > 3)
```
```
3 3 -4 512 4 False
```
`-15 / 4 = -3.75`, aur us se neeche ka poora number `-4` hai. `2 ** 9 = 512`, kyun ke `**` daayein se chalta hai. `not` comparison ke **baad** chalta hai: `not (5 > 3)`.

### Solution 4
```python
# file: solutions/ex04_savings.py
savings = 0
savings += 15_000
print("Jama ke baad:", savings)
savings -= 3_500
print("Nikalne ke baad:", savings)
savings *= 1.10
print(f"10% munafa ke baad: {savings:,.2f}")
```
```
Jama ke baad: 15000
Nikalne ke baad: 11500
10% munafa ke baad: 12,650.00
```

### Solution 5
<!-- stdin: 472 -->
```python
# file: solutions/ex05_digits.py
n = int(input("3-digit number: "))
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
print(f"Digits: {hundreds}, {tens}, {ones}")
print(f"Majmua: {hundreds + tens + ones}")
```
```
3-digit number: 472
Digits: 4, 7, 2
Majmua: 13
```
`472 // 10 = 47`, aur `47 % 10 = 7`. Is tarah beech wala digit milta hai.

### Solution 6
<!-- stdin: 19 | 72 | True -->
```python
# file: solutions/ex06_eligibility.py
age = int(input("Umar: "))
marks = int(input("Marks: "))
sports_quota = input("Sports quota? (True/False): ") == "True"

eligible = (16 <= age <= 25) and (marks >= 80 or sports_quota)
print("Eligible:", eligible)
```
```
Umar: 19
Marks: 72
Sports quota? (True/False): True
Eligible: True
```
- `input(...) == "True"`: user ke text ko boolean mein badalne ka saaf tareeqa. `bool("False")` `True` deta, is liye woh yahan kaam nahi karta.
- Parentheses ke baghair `and` pehle chalta: `age-condition and marks >= 80`, aur `or sports_quota` alag ho jata. Is tarah 40 saal ka sports quota wala bhi eligible ho jata.

### Solution 7
**Masla 1:** `percentage` asal mein `84.444...` hai, is liye `== 84.44` `False` hai. Round karke compare karein, ya `math.isclose` mein tolerance dein.
**Masla 2:** `city == "Lahore" or "Karachi"` hamesha truthy hai.
```python
# file: solutions/ex07_fixed.py
import math

total_marks = 450
obtained = 380
percentage = obtained / total_marks * 100
print(f"Percentage: {percentage:.2f}")
print(round(percentage, 2) == 84.44)
print(math.isclose(percentage, 84.44, abs_tol=0.01))

city = "Quetta"
print(city in ("Lahore", "Karachi"))
```
```
Percentage: 84.44
True
True
False
```

### Solution 8
<!-- stdin: 2895 -->
```python
# file: solutions/ex08_time_formatter.py
total_minutes = int(input("Total minutes: "))
days, remaining = divmod(total_minutes, 24 * 60)
hours, minutes = divmod(remaining, 60)
print(f"{total_minutes} minutes = {days} din, {hours} ghante, {minutes} minute")
```
```
Total minutes: 2895
2895 minutes = 2 din, 0 ghante, 15 minute
```

### Solution 9
```python
# file: solutions/ex09_leap_year.py
year = 2024
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 1900
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 2000
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
year = 2026
print(year, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
```
```
2024 True
1900 False
2000 True
2026 False
```
Aik hi expression bar bar likhna parha. Chapter 6 ke loops aur Chapter 9 ke functions is takrar ko khatam karenge.

### Solution 10
<!-- stdin: 350 | 42.5 -->
```python
# file: solutions/ex10_electricity.py
import math

TAX_RATE = 0.17
units = int(input("Units: "))
rate = float(input("Rate per unit (PKR): "))

base = units * rate
total = math.ceil(base * (1 + TAX_RATE))
notes, change = divmod(total, 500)

print(f"Base bill   : {base:,.2f}")
print(f"Tax ke saath: {total:,}")
print(f"500 ke {notes} note, baqi {change} PKR")
```
```
Units: 350
Rate per unit (PKR): 42.5
Base bill   : 14,875.00
Tax ke saath: 17,404
500 ke 34 note, baqi 404 PKR
```

---

## Agla Qadam
**Part 2** shuru hota hai. Chapter 4 mein hum **strings** ko gehrai se seekhenge: indexing, slicing, methods, aur f-string ki alignment, jo Mini Project 1 mein `>12` ke tor par dekhi.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
