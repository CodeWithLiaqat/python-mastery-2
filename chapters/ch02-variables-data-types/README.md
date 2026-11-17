# Chapter 2 — Variables, Data Types Aur Input/Output

> **PYTHON MASTERY** · Roman Urdu Edition · MIAVRO Systems · Part 1: Absolute Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:**
- Variable kya hai aur Python memory mein values ko kaise rakhta hai
- Variables ke naam rakhne ke rules aur professional conventions
- Python ke bunyadi data types: `int`, `float`, `str`, `bool`, `None`
- `type()` aur `id()` se objects ko pehchanna
- Aik type se doosri type mein conversion
- `input()` se user ki baat sunna
- `print()` aur f-strings se professional output banana
- Multiple assignment, swapping aur constants
- Mutable aur immutable ka pehla ta'aruf

**Prerequisites:** Chapter 1 (`print()`, comments, script chalana)
**Andaazan study time:** 3–4 ghante

---

## 2.1 Variable Kya Hai?

**Yeh kya hai?**
Variable aik **named reference** hota hai. Iske zariye hum apne program mein kisi value ko store aur access kar sakte hain. Python mein variable khud value nahi hota. Woh aik **naam** hai jo memory mein rakhe gaye kisi **object** ki taraf ishara karta hai.

Ise aik **label** ki tarah samjhein. Aap ke paas aik dabba (object) hai jis mein `25` rakha hai. Aap us dabbe par "umar" ka sticker laga dete hain. Ab aap "umar" keh kar us dabbe tak pohanch sakte hain.

**Zaroorat kyun?** Chapter 1 ki chai dhaba receipt yaad karein. Wahan `80` (chai ki qeemat) kai jagah likha tha. Agar qeemat badle to har jagah badalna parta. Variable ke saath qeemat **aik jagah** likhi jati hai aur har jagah naam se istemal hoti hai.

**Kaise kaam karta hai?**
```
umar = 25

 naam            object (memory mein)
 ┌──────┐        ┌─────────────┐
 │ umar │ ─────► │ int: 25     │
 └──────┘        └─────────────┘
```
1. Python pehle **daayein** taraf ki value (`25`) ka object memory mein banata hai.
2. Phir **baayein** taraf ke naam (`umar`) ko us object se jor deta hai.

`=` ko **assignment operator** kehte hain. Math mein `=` ka matlab "barabar hai" hota hai, lekin Python mein iska matlab hai: **"daayein wali value ko baayein wale naam se jor do."**

**Syntax:**
```text
variable_ka_naam = value
```

**Example:**

```python
# file: examples/01_variables.py
# Variables banana aur istemal karna
naam = "Ahmed"
umar = 25
shehar = "Lahore"

print(naam)
print(umar)
print("Naam:", naam, "| Umar:", umar, "| Shehar:", shehar)

# Variable ki value badalna (reassignment)
umar = 26
print("Saalgirah ke baad umar:", umar)
```

**Output:**
```
Ahmed
25
Naam: Ahmed | Umar: 25 | Shehar: Lahore
Saalgirah ke baad umar: 26
```

**Line-by-line:**
| Line | Purpose |
|---|---|
| `naam = "Ahmed"` | `"Ahmed"` string object bana aur `naam` us se jur gaya |
| `print(naam)` | Quotes ke **baghair** `naam` likha, is liye Python ne variable ki value dikhayi |
| `umar = 26` | **Reassignment**: `umar` ab naye object `26` ki taraf ishara karta hai. Purana `25` ab kisi kaam ka nahi |

**Kab use karein?** Jab bhi koi value aik se zyada dafa istemal ho, badal sakti ho, ya uska koi **matlab** ho (e.g. `tax_rate` likhna `0.18` likhne se zyada wazeh hai).

**⚠ Aam Ghaltiyan**
- `print("naam")` likh dena jab variable ki value chahiye thi. Quotes ke andar `naam` sirf text hai.
- Variable banane se pehle istemal karna: `print(total)` likha aur `total` kabhi banaya hi nahi → `NameError`.
- `25 = umar` ulta likhna → `SyntaxError`. Naam hamesha **baayein** hota hai.

**💡 Ghalat Fehmi:** *"Variable aik dabba hai jis mein value rakhi hoti hai."* Python mein variable dabba nahi, **label** hai. Yeh farq section 2.9 aur Chapter 7 (lists copy karna) mein bohat ahem ho jata hai.

---

## 2.2 Naming Rules, PEP 8 Conventions Aur Reserved Keywords

**Lazmi rules** (in ko toorne par `SyntaxError`):
1. Naam letter (a–z, A–Z) ya underscore (`_`) se shuru ho. Number se nahi.
2. Sirf letters, numbers aur `_` allowed hain. Space, `-`, `@`, `$` nahi.
3. Python ka **reserved keyword** naam nahi ban sakta.
4. Python **case-sensitive** hai: `Naam`, `naam` aur `NAAM` teen alag variables hain.

| ✅ Sahi | ❌ Ghalat | Wajah |
|---|---|---|
| `student_name` | `student name` | Space allowed nahi |
| `marks2` | `2marks` | Number se shuru nahi ho sakta |
| `_total` | `total-amount` | `-` minus operator hai |
| `class_name` | `class` | `class` reserved keyword hai |

**PEP 8 conventions** (yeh rules nahi balkay **professional adat** hain): PEP 8 Python ka official style guide hai.
- Variables ke liye **`snake_case`**: chhote huroof, alfaaz ke beech `_` (`monthly_salary`, `total_marks`)
- Wazeh, maani-khez naam rakhein: `x` ke bajaye `price`
- Constants ke liye `UPPER_CASE` (section 2.8)

**Reserved keywords** dekhne ke liye:

```python
# file: examples/02_keywords.py
import keyword

print("Kul keywords:", len(keyword.kwlist))
print(keyword.kwlist)
```

**Output:**
```
Kul keywords: 35
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

`import keyword` built-in `keyword` module laata hai (modules Chapter 10 mein). `len()` cheezon ki ginti batata hai. In naamon ko kabhi variable ke tor par istemal na karein.

**⚠ Aam Ghalti: built-in naamon ko overwrite karna.** `print`, `input`, `list`, `str`, `sum` keywords nahi hain, is liye Python aap ko inhe variable banane se nahi rokega. Lekin agar aap ne `print = 5` likh diya to us ke baad `print()` kaam nahi karega:

```python
# file: examples/03_shadow_error.py
print = "Hello"
print("Yeh nahi chalega")
```

**Output:**
```
Traceback (most recent call last):
  File ".../03_shadow_error.py", line 3, in <module>
    print("Yeh nahi chalega")
    ~~~~~^^^^^^^^^^^^^^^^^^^^
TypeError: 'str' object is not callable
```

`print` ab function nahi raha, ek string ban gaya hai, aur string ko call `()` nahi kiya ja sakta. Isay **shadowing** kehte hain. Hal: aisa naam rakhein hi nahi. REPL mein ho jaye to REPL restart karein.

---

## 2.3 Python Ke Core Data Types

**Yeh kya hai?** Har value ki aik **type** hoti hai. Type batati hai ke value kis qisam ki hai aur us par kaunse operations ho sakte hain. Number jama ho sakte hain, text ko capital kiya ja sakta hai, magar text ko taqseem nahi kiya ja sakta.

| Type | Naam | Misaal | Kab istemal |
|---|---|---|---|
| `int` | Integer (poore number) | `25`, `-7`, `0`, `1_000_000` | Ginti, umar, quantity |
| `float` | Floating point (decimal) | `3.14`, `-0.5`, `2.0`, `1.5e3` | Qeemat, percentage, measurement |
| `str` | String (text) | `"Lahore"`, `'A'`, `""` | Naam, pata, message |
| `bool` | Boolean | `True`, `False` | Haan/nahi, on/off |
| `NoneType` | None | `None` | "Abhi koi value nahi" |

```python
# file: examples/04_data_types.py
# Python ke bunyadi data types
students = 45                 # int
population = 1_250_000        # int: underscore sirf parhne mein asaani ke liye
petrol_price = 272.89         # float
distance = 1.5e3              # float: 1.5 x 10^3 = 1500.0
city = "Karachi"              # str
is_open = True                # bool
discount = None               # NoneType: abhi koi discount tay nahi

print(students, population, petrol_price, distance)
print(city, is_open, discount)
```

**Output:**
```
45 1250000 272.89 1500.0
Karachi True None
```

**Ahem nukaat:**
- **`int`** ki koi had nahi. Python bohat bare numbers bhi sambhal leta hai (`2 ** 100` try karein).
- **`1_250_000`**: underscore sirf insaan ki asaani ke liye hai. Python ise `1250000` hi samajhta hai.
- **`float`** mein decimal point zaroori hai: `2` int hai, `2.0` float hai.
- **`bool`** ki sirf do values hain: `True` aur `False`. Pehla harf **capital** hona lazmi hai.
- **`None`** ka matlab "khaali" ya "abhi maloom nahi" hai. Yeh `0` ya `""` se mukhtalif hai. `0` aik value hai, `None` value ki **ghair maujoodgi** hai.

**⚠ Aam Ghaltiyan**
- `true` ya `false` chhote huroof mein likhna → `NameError`.
- `"25"` aur `25` ko aik samajhna. Pehla text hai, doosra number.
- `none` ya `null` likhna. Python mein sirf `None` hai.

**💡 Ghalat Fehmi:** *"`2.0` aur `2` bilkul aik hi cheez hain."* Value barabar hai (`2 == 2.0` → `True`), lekin type alag hai, aur float ki precision ke apne masle hain (Chapter 3).

---

## 2.4 `type()` Aur `id()` — Dynamic Typing

**`type()`** batata hai ke kisi value ya variable ki type kya hai.
**`id()`** object ki aik unique pehchan (identity number) deta hai. Aap ise memory mein us object ka "address" samajh sakte hain.

**Dynamic typing** ka matlab hai ke Python mein variable ki koi pakki type nahi hoti. Type **value** ki hoti hai, naam ki nahi. Aik hi naam pehle number aur baad mein text ki taraf ishara kar sakta hai. Java ya C jaisi languages mein aap ko pehle batana parta hai: `int umar = 25;`. Python khud samajh leta hai.

```python
# file: examples/05_type_id.py
# type() aur dynamic typing
value = 100
print(value, type(value))

value = "sau"
print(value, type(value))

value = 99.5
print(value, type(value))

# id(): do naam aik hi object ki taraf
a = "Pakistan"
b = a
print("a aur b aik hi object?", id(a) == id(b))
print("is se bhi check:", a is b)
```

**Output:**
```
100 <class 'int'>
sau <class 'str'>
99.5 <class 'float'>
a aur b aik hi object? True
is se bhi check: True
```

**Line-by-line:**
- `<class 'int'>`: Python mein har type aik **class** hai. Classes ko Chapter 13 mein samjhenge. Abhi itna kaafi hai ke `int` type hai.
- `value` ne teen dafa type badli. Yahi dynamic typing hai.
- `b = a` **koi copy nahi banata**. `b` usi object se jur jata hai jis se `a` jura hai, is liye dono ke `id` barabar hain.
- `is` operator check karta hai ke do naam **bilkul aik hi object** ki taraf hain ya nahi (Chapter 3).

> `id()` ka asal number har dafa aur har computer par mukhtalif hota hai. Is liye hum ne number print karne ke bajaye sirf comparison print kiya hai.

**⚠ Aam Ghalti:** Dynamic typing ki azadi ka ghalat istemal. Aik hi variable mein kabhi number aur kabhi text rakhna code ko confusing bana deta hai. Achi adat: aik variable ka aik hi maqsad.

**💡 Ghalat Fehmi:** *"Dynamic typing ka matlab hai Python mein types hoti hi nahi."* Types bilkul hoti hain aur sakht hain. Python `"5" + 5` nahi karne dega (`TypeError`). Bas type **chalte waqt** check hoti hai, pehle se declare nahi karni parti.

---

## 2.5 Type Conversion (Type Casting)

**Yeh kya hai?** Aik type ki value se doosri type ki value banana. Is ke liye built-in functions hain: `int()`, `float()`, `str()`, `bool()`.

**Zaroorat kyun?** `input()` hamesha text deta hai (2.6). Files aur websites se aane wala data aksar text hota hai. Hisaab karne ke liye use number mein badalna parta hai.

**Do qisam:**
- **Implicit conversion:** Python khud karta hai. `int + float` ka natija `float`, taake decimal zaya na ho.
- **Explicit conversion:** aap khud function laga kar karte hain.

```python
# file: examples/06_conversion.py
# Implicit conversion
total = 10 + 2.5
print(total, type(total))

# Explicit conversion
print(int("42") + 8)        # text -> int
print(float("99.99"))       # text -> float
print(int(9.99))            # float -> int: decimal KAT jata hai, round nahi hota
print(round(9.99))          # round karna ho to round()
print(str(2025) + " mein")  # int -> text, taake text ke saath jor sakein
print(float(7))             # int -> float

# bool() conversion: "khaali" cheezein False hain
print(bool(0), bool(0.0), bool(""), bool(None))
print(bool(5), bool(-1), bool("0"), bool(" "))
```

**Output:**
```
12.5 <class 'float'>
50
99.99
9
10
2025 mein
7.0
False False False False
True True True True
```

**Line-by-line:**
| Code | Natija | Wazahat |
|---|---|---|
| `10 + 2.5` | `12.5` (float) | Implicit: int ko float mein badal kar jama kiya |
| `int("42") + 8` | `50` | Text `"42"` number ban gaya |
| `int(9.99)` | `9` | **Truncation**: decimal hissa kat jata hai |
| `round(9.99)` | `10` | Qareebi poora number |
| `bool("0")` | `True` | `"0"` khaali string nahi, aik character hai |

**Galat conversion par error:**

```python
# file: examples/07_conversion_error.py
age_text = "pachees"
age = int(age_text)
```

**Output:**
```
Traceback (most recent call last):
  File ".../07_conversion_error.py", line 3, in <module>
    age = int(age_text)
ValueError: invalid literal for int() with base 10: 'pachees'
```

`int()` sirf woh text badal sakta hai jo number jaisa dikhe. `"pachees"`, `"12.5"` ya `"1,000"` jaise text par `ValueError` aata hai. Exceptions ko sambhalna Chapter 12 mein seekhenge.

**⚠ Aam Ghaltiyan**
- `int("12.5")` → `ValueError`. Pehle `float("12.5")`, phir zaroorat ho to `int()`.
- Samajhna ke `int()` round karta hai. Woh sirf kaat-ta hai: `int(-3.7)` → `-3`.
- `"Umar: " + 25` → `TypeError`. Text aur number ko `+` se nahi jora ja sakta. `str(25)` karein ya f-string use karein (2.7).

**💡 Ghalat Fehmi:** *"`bool("False")` ka jawab `False` hoga."* Nahi, `True` aayega. Koi bhi **non-empty** string `True` hoti hai, chahe us mein "False" hi likha ho.

---

## 2.6 `input()` — User Se Baat Karna

**Yeh kya hai?** `input()` built-in function hai jo program ko rok kar user ke type karne aur **Enter** dabane ka intezar karta hai. Jo user ne likha woh **string** ki shakal mein wapas deta hai.

**Syntax:**
```text
variable = input("Sawal ya prompt: ")
```

<!-- stdin: Fatima | 21 -->
```python
# file: examples/08_input.py
# User se maloomat lena
name = input("Aap ka naam kya hai? ")
age_text = input("Aap ki umar kitni hai? ")

print("Khush aamdeed,", name)
print("age_text ki type:", type(age_text))

age = int(age_text)          # hisaab se pehle conversion zaroori
print("Agle saal aap", age + 1, "saal ke ho jayenge.")
```

**Output** (user ne `Fatima` aur `21` type kiya):
```
Aap ka naam kya hai? Fatima
Aap ki umar kitni hai? 21
Khush aamdeed, Fatima
age_text ki type: <class 'str'>
Agle saal aap 22 saal ke ho jayenge.
```

**Line-by-line:**
- `input("Aap ka naam kya hai? ")`: prompt dikhaya, intezar kiya, aur user ka jawab `name` mein rakha.
- Prompt ke aakhir mein space rakhein taake user ka jawab chipak na jaye.
- `type(age_text)` → `<class 'str'>`: user ne `21` likha, phir bhi woh **text** hai.
- `int(age_text)` ke baad hi `+ 1` mumkin hua.

**Short-cut:** aksar conversion aur input aik hi line mein likhe jate hain:
```text
age = int(input("Umar: "))
price = float(input("Qeemat: "))
```

**⚠ Sab se aam ghalti:**

<!-- stdin: 2000 -->
```python
# file: examples/09_input_error.py
salary = input("Monthly salary? ")
bonus = salary + 5000
print(bonus)
```

**Output:**
```
Monthly salary? 2000
Traceback (most recent call last):
  File ".../09_input_error.py", line 3, in <module>
    bonus = salary + 5000
            ~~~~~~~^~~~~~
TypeError: can only concatenate str (not "int") to str
```

`salary` text hai (`"2000"`), aur text mein number jama nahi ho sakta. Hal: `salary = int(input("Monthly salary? "))`.

**💡 Ghalat Fehmi:** *"Agar user number likhe to `input()` number deta hai."* Kabhi nahi. `input()` **hamesha** `str` deta hai.

---

## 2.7 Output: `print()` Ke Options Aur f-strings

### `sep` aur `end`
`print()` ke do khaas **keyword arguments** hain:
- `sep`: values ke beech kya aaye (default: aik space `" "`)
- `end`: aakhir mein kya aaye (default: nayi line `"\n"`)

```python
# file: examples/10_sep_end.py
print("2025", "11", "17", sep="-")
print("Lahore", "Karachi", "Islamabad", sep=" | ")
print("Loading", end="")
print("...", end=" ")
print("Done!")
```

**Output:**
```
2025-11-17
Lahore | Karachi | Islamabad
Loading... Done!
```

`end=""` ki wajah se agla `print()` usi line par jari raha. `\n` ka matlab "new line" hai (escape characters Chapter 4 mein).

### f-strings — Modern Python ka tareeqa
**Yeh kya hai?** **f-string** (formatted string literal) woh string hai jis ke shuru mein `f` lagta hai. Is ke andar `{}` braces mein aap variables ya expressions seedha likh sakte hain.

**Zaroorat kyun?** Commas aur `str()` ke saath strings jorna mushkil aur ghaltiyon se bhara hai. f-string saaf, tez aur parhne mein asaan hai.

**Syntax:** `f"Text {variable} text {expression}"`

```python
# file: examples/11_fstrings.py
name = "Bilal"
price = 1499.5
quantity = 3
salary = 185000
score = 0.8765

print(f"Customer: {name}")
print(f"Total: {price * quantity} PKR")              # expression bhi chalta hai
print(f"Qeemat: {price:.2f} PKR")                     # 2 decimal places
print(f"Salary: {salary:,} PKR")                      # hazaron ka comma
print(f"Score: {score:.1%}")                          # percentage
print(f"Bara naam: {name.upper()}")                    # method call bhi ho sakti hai
print(f"{price = }")                                  # debugging shortcut (3.8+)
```

**Output:**
```
Customer: Bilal
Total: 4498.5 PKR
Qeemat: 1499.50 PKR
Salary: 185,000 PKR
Score: 87.6%
Bara naam: BILAL
price = 1499.5
```

**Format specifiers** (`:` ke baad):
| Specifier | Matlab | Misaal |
|---|---|---|
| `:.2f` | 2 decimal places tak float | `1499.50` |
| `:,` | Hazaron mein comma | `185,000` |
| `:,.2f` | Dono aik saath | `1,499.50` |
| `:.1%` | Percentage, 1 decimal | `87.6%` |
| `{x = }` | Variable ka naam aur value dono (debugging) | `price = 1499.5` |

Alignment aur padding (`:<10`, `:>10`, `:^10`) Chapter 4 mein seekhenge.

**⚠ Aam Ghaltiyan**
- `f` lagana bhool jana: `"Total: {price}"` bilkul waisa hi `{price}` print kar dega.
- `{}` ke andar quotes ka takrao: `f"{"name"}"` purane versions mein error deta hai. Andar aur bahar mukhtalif quotes istemal karein.

**💡 Ghalat Fehmi:** *"`:.2f` asal value ko badal deta hai."* Nahi. Yeh sirf **dikhane** ka tareeqa hai. Variable ki value waisi hi rehti hai.

---

## 2.8 Multiple Assignment, Swapping Aur Constants

```python
# file: examples/12_multiple_assignment.py
# Aik line mein kai variables
x, y, z = 10, 20, 30
print(x, y, z)

# Sab ko aik hi value
a = b = c = 0
print(a, b, c)

# Swapping: Python ka khoobsurat tareeqa
first = "Chai"
second = "Coffee"
first, second = second, first
print(f"first = {first}, second = {second}")

# Constants: UPPER_CASE convention
GST_RATE = 0.18
MAX_STUDENTS = 40
bill = 5000
print(f"GST: {bill * GST_RATE} PKR")
```

**Output:**
```
10 20 30
0 0 0
first = Coffee, second = Chai
GST: 900.0 PKR
```

**Line-by-line:**
- `x, y, z = 10, 20, 30`: values aur naam **tarteeb** se jurte hain. Ginti barabar honi chahiye, warna `ValueError`.
- `first, second = second, first`: Python pehle daayein taraf ki dono values utha leta hai, phir naye naamon se jorta hai. Doosri languages mein swap ke liye aik teesra temporary variable chahiye hota hai.
- **Constants:** Python mein asal "constant" nahi hota. `GST_RATE` ko bhi badla ja sakta hai. `UPPER_CASE` naam sirf aik **convention** hai jo doosre programmers ko batata hai: "ise mat badlo".

**⚠ Aam Ghalti:** `x, y = 1, 2, 3` → `ValueError: too many values to unpack`.

---

## 2.9 Mutable vs Immutable — Pehla Ta'aruf

**Yeh kya hai?**
- **Immutable** object ko banne ke baad **badla nahi ja sakta**. Ab tak ki tamam types (`int`, `float`, `str`, `bool`, `None`) immutable hain.
- **Mutable** object ko jagah par badla ja sakta hai. Misaal: `list`, `dict`, `set` (Chapters 7–8).

**To phir `umar = umar + 1` kaise kaam karta hai?** Purana object nahi badalta. Python **naya object** banata hai aur naam ko us se jor deta hai.

```python
# file: examples/13_immutable.py
score = 50
old_id = id(score)

score = score + 10
print("Nayi value:", score)
print("Kya wahi object hai?", id(score) == old_id)

city = "lahore"
city.upper()                 # naya string banata hai, city ko nahi badalta
print("city abhi bhi:", city)
city = city.upper()          # natija wapas usi naam ko assign kiya
print("city ab:", city)
```

**Output:**
```
Nayi value: 60
Kya wahi object hai? False
city abhi bhi: lahore
city ab: LAHORE
```

**Line-by-line:**
- `score + 10` ne naya object `60` banaya. Is liye `id` mukhtalif hai.
- `city.upper()` naya string `"LAHORE"` banata hai, lekin hum ne use kahin rakha nahi, is liye woh zaya ho gaya.
- Natija chahiye to use assign karna lazmi hai: `city = city.upper()`.

**💡 Ghalat Fehmi:** *"`.upper()` string ko badal deta hai."* Strings immutable hain. Tamam string methods **nayi** string wapas dete hain. Mutable objects ke saath yeh kahani bilkul badal jati hai, aur yeh Chapter 7 ka ahem mauzu hai.

---

## Solved Example — Age Calculator

**Masla:** User se naam aur paidaish ka saal lein, aur batayein ke 2026 mein woh kitne saal ke honge aur 100 saal ke kab honge.

<!-- stdin: Hamza | 2001 -->
```python
# file: examples/14_age_calculator.py
# Age Calculator
CURRENT_YEAR = 2026

name = input("Naam: ")
birth_year = int(input("Paidaish ka saal: "))

age = CURRENT_YEAR - birth_year
year_of_100 = birth_year + 100

print("-" * 35)
print(f"{name}, {CURRENT_YEAR} mein aap ki umar {age} saal hai.")
print(f"Aap {year_of_100} mein 100 saal ke honge.")
print(f"Yaani abhi {year_of_100 - CURRENT_YEAR} saal baqi hain.")
```

**Output:**
```
Naam: Hamza
Paidaish ka saal: 2001
-----------------------------------
Hamza, 2026 mein aap ki umar 25 saal hai.
Aap 2101 mein 100 saal ke honge.
Yaani abhi 75 saal baqi hain.
```

**Steps ki wazahat:**
1. `CURRENT_YEAR` constant hai, taake agle saal sirf aik jagah badalna pare.
2. `int(input(...))`: input aur conversion aik saath.
3. `"-" * 35`: string ko 35 dafa dohraya. Yeh string repetition hai (Chapter 4).
4. f-strings ke andar seedha hisaab bhi kiya: `{year_of_100 - CURRENT_YEAR}`.

**Limitation:** Agar user `"do hazaar"` likhe to program `ValueError` de kar band ho jayega. Is ka hal Chapter 5 (validation) aur Chapter 12 (exceptions) mein aayega.

---

## 🌍 Real World
- **E-commerce:** `product_price`, `quantity`, `discount` jaise variables har checkout system ki bunyad hain.
- **Banking apps:** amount ko hamesha numeric type mein convert karke hisaab hota hai. Text mein hisaab karna bhari ghalti hai.
- **Data Science:** CSV files se aane wale "numbers" aksar text hote hain. Pandas mein bhi yahi conversion (`astype`, `to_numeric`) karni parti hai (Chapter 18).
- **Reports:** f-strings se `PKR 1,250,000.00` jaisa professional format banta hai.

---

## Chapter Summary
1. **Variable** aik naam hai jo memory mein kisi **object** ki taraf ishara karta hai. `=` assignment hai, barabari nahi.
2. Naam letter ya `_` se shuru hon, keywords na hon. Python case-sensitive hai. `snake_case` istemal karein.
3. Bunyadi types: `int`, `float`, `str`, `bool`, `NoneType`.
4. `type()` type batata hai. `id()` object ki pehchan deta hai. Python **dynamically typed** hai: type value ki hoti hai, naam ki nahi.
5. `int()`, `float()`, `str()`, `bool()` se conversion hoti hai. `int()` decimal kaat-ta hai, round nahi karta.
6. `input()` **hamesha string** deta hai. Hisaab se pehle convert karein.
7. f-strings: `f"{value:.2f}"`, `{value:,}`, `{value:.1%}`. `print()` ke `sep` aur `end`.
8. `a, b = b, a` se swap hota hai. Constants `UPPER_CASE` mein likhe jate hain (sirf convention).
9. `int`, `float`, `str`, `bool` **immutable** hain. "Badalna" darasal naya object banana hai.

---

## Exercises

### 🟢 Exercise 1 — Personal card
`name`, `city`, `age` aur `height_m` (meters mein, float) ke variables banayein aur f-string se aik line mein print karein.

### 🟢 Exercise 2 — Type pehchanein
In values ki type predict karein, phir `type()` se check karein: `7`, `7.0`, `"7"`, `True`, `None`, `3e2`.

### 🟢 Exercise 3 — Sahi ya ghalat naam?
Batayein kaunse naam valid hain: `total_marks`, `2nd_place`, `my-name`, `_temp`, `for`, `Class`, `user name`, `price2`. Phir check karne ke liye har valid naam ko value assign karke dekhein.

### 🟢 Exercise 4 — Swap
`morning = "Chai"` aur `evening = "Lassi"` ko teesra variable istemal kiye baghair aapas mein badlein.

### 🟡 Exercise 5 — Rectangle calculator
User se length aur width (decimal mein ho sakti hain) lein aur area aur perimeter 2 decimal places tak print karein.
**Hint:** `float(input(...))`, area = l × w, perimeter = 2 × (l + w).

### 🟡 Exercise 6 — Temperature converter
User se Celsius mein temperature lein aur Fahrenheit mein badlein: `F = C × 9/5 + 32`. Natija 1 decimal tak dikhayein.

### 🟡 Exercise 7 — Bug hunter
Is program mein 3 ghaltiyan hain. Theek karein:
```text
Item Price = input("Qeemat: ")
total = Item Price * 2
print("Total: {total}")
```

### 🔴 Exercise 8 — Chai dhaba receipt 2.0
Chapter 1 ki receipt dobara banayein: chai 80, paratha 60, omelette 150 ki qeematein **constants** mein rakhein. Quantities user se lein. Har line aur kul bill f-string aur `:,` format ke saath dikhayein, aur 5% service charge bhi shamil karein.

### 🔴 Exercise 9 — Seconds converter
User se seconds ki ginti lein (e.g. `7384`) aur use hours, minutes aur seconds mein badlein.
**Hint:** `//` (floor division) aur `%` (remainder). `3600` seconds = 1 ghanta. Yeh operators Chapter 3 mein tafseel se hain.

### 🔴 Exercise 10 — Predict karein
Chalane se pehle har line ka output likhein:
```text
a = "5"
b = 5
print(a * 3)
print(b * 3)
print(int(a) + b)
print(str(b) + a)
print(bool(""), bool(" "), bool(0.0))
```

---

## Complete Solutions

### Solution 1
```python
# file: solutions/ex01_personal_card.py
name = "Zainab"
city = "Multan"
age = 19
height_m = 1.63

print(f"{name} | {city} | {age} saal | {height_m} m")
```
```
Zainab | Multan | 19 saal | 1.63 m
```

### Solution 2
```python
# file: solutions/ex02_types.py
print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))
print(type(None))
print(type(3e2), 3e2)
```
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
<class 'float'> 300.0
```
`3e2` scientific notation hai (3 × 10²). Is mein `e` ki wajah se yeh hamesha float hota hai, chahe jawab poora number ho.

### Solution 3
**Valid:** `total_marks`, `_temp`, `Class` (capital C ki wajah se keyword `class` se alag hai), `price2`.
**Invalid:** `2nd_place` (number se shuru), `my-name` (`-`), `for` (keyword), `user name` (space).
```python
# file: solutions/ex03_names.py
total_marks = 450
_temp = 36.6
Class = "10th"
price2 = 99
print(total_marks, _temp, Class, price2)
```
```
450 36.6 10th 99
```
> `Class` technically valid hai, lekin PEP 8 ke mutabiq variable ke naam chhote huroof mein hone chahiye. Capital naam classes ke liye hote hain (Chapter 13).

### Solution 4
```python
# file: solutions/ex04_swap.py
morning = "Chai"
evening = "Lassi"
morning, evening = evening, morning
print(f"Subah: {morning}, Shaam: {evening}")
```
```
Subah: Lassi, Shaam: Chai
```

### Solution 5
<!-- stdin: 12.5 | 8 -->
```python
# file: solutions/ex05_rectangle.py
length = float(input("Length (m): "))
width = float(input("Width (m): "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area:.2f} sq m")
print(f"Perimeter: {perimeter:.2f} m")
```
```
Length (m): 12.5
Width (m): 8
Area: 100.00 sq m
Perimeter: 41.00 m
```
User ne `8` likha, magar `float()` ki wajah se woh `8.0` bana. Is liye decimal wali lengths bhi chal jati hain.

### Solution 6
<!-- stdin: 37 -->
```python
# file: solutions/ex06_temperature.py
celsius = float(input("Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
```
```
Celsius: 37
37.0°C = 98.6°F
```

### Solution 7
**Ghaltiyan:** (1) `Item Price` mein space hai, (2) `input()` string deta hai, is liye `* 2` text ko dohra dega (`"500500"`), (3) `print` mein `f` nahi laga.
<!-- stdin: 500 -->
```python
# file: solutions/ex07_fixed.py
item_price = float(input("Qeemat: "))
total = item_price * 2
print(f"Total: {total}")
```
```
Qeemat: 500
Total: 1000.0
```

### Solution 8
<!-- stdin: 3 | 2 | 1 -->
```python
# file: solutions/ex08_receipt_v2.py
# Chai Dhaba Receipt 2.0
CHAI_PRICE = 80
PARATHA_PRICE = 60
OMELETTE_PRICE = 150
SERVICE_RATE = 0.05

chai_qty = int(input("Chai kitni? "))
paratha_qty = int(input("Paratha kitne? "))
omelette_qty = int(input("Omelette kitne? "))

chai_total = chai_qty * CHAI_PRICE
paratha_total = paratha_qty * PARATHA_PRICE
omelette_total = omelette_qty * OMELETTE_PRICE
subtotal = chai_total + paratha_total + omelette_total
service = subtotal * SERVICE_RATE
grand_total = subtotal + service

print("===== Bismillah Chai Dhaba =====")
print(f"Chai     x{chai_qty} : {chai_total:,} PKR")
print(f"Paratha  x{paratha_qty} : {paratha_total:,} PKR")
print(f"Omelette x{omelette_qty} : {omelette_total:,} PKR")
print("--------------------------------")
print(f"Subtotal    : {subtotal:,} PKR")
print(f"Service 5%  : {service:,.2f} PKR")
print(f"Kul Bill    : {grand_total:,.2f} PKR")
```
```
Chai kitni? 3
Paratha kitne? 2
Omelette kitne? 1
===== Bismillah Chai Dhaba =====
Chai     x3 : 240 PKR
Paratha  x2 : 120 PKR
Omelette x1 : 150 PKR
--------------------------------
Subtotal    : 510 PKR
Service 5%  : 25.50 PKR
Kul Bill    : 535.50 PKR
```
**Chapter 1 se behtari:** qeematein aik jagah hain, quantities user se aati hain, aur har hisaab ka aik maani-khez naam hai.

### Solution 9
<!-- stdin: 7384 -->
```python
# file: solutions/ex09_seconds.py
total_seconds = int(input("Seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} ghante, {minutes} minute, {seconds} second")
```
```
Seconds: 7384
7384 seconds = 2 ghante, 3 minute, 4 second
```
`7384 // 3600 = 2` poore ghante. `7384 % 3600 = 184` seconds bache. `184 // 60 = 3` minute aur `184 % 60 = 4` second.

### Solution 10
```python
# file: solutions/ex10_predict.py
a = "5"
b = 5
print(a * 3)
print(b * 3)
print(int(a) + b)
print(str(b) + a)
print(bool(""), bool(" "), bool(0.0))
```
```
555
15
10
55
False True False
```
- `"5" * 3` → text ko 3 dafa dohraya: `555`
- `5 * 3` → math: `15`
- `int("5") + 5` → `10`
- `"5" + "5"` → text jora: `55`
- `""` khaali hai (`False`), `" "` mein space hai (`True`), `0.0` zero hai (`False`)

---

## Agla Qadam
Chapter 3 mein hum **operators** ko gehrai se dekhenge: `//` aur `%` ka asal raaz, comparisons, `and`/`or`/`not`, `is` vs `==`, precedence, aur float precision ka mashhoor `0.1 + 0.2` masla. Akhir mein **Mini Project 1: Bill Splitter + Tip Calculator** banayenge.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
