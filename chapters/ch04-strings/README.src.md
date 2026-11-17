# Chapter 4 — Strings Gehrai Se

> **PYTHON MASTERY** · Roman Urdu Edition · MIAVRO Systems · Part 2: Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:** strings banane ke tareeqe · escape characters aur raw strings · indexing aur slicing · immutability · aham string methods · `join()` vs `+` · f-string formatting mini-language · `len()`, `in` aur Unicode
**Prerequisites:** Chapters 2–3
**Andaazan study time:** 3–4 ghante

---

## 4.1 Strings Banana: Single, Double, Triple Quotes

**Yeh kya hai?** **String** characters (huroof, numbers, symbols, spaces) ka aik **tarteeb-war sequence** hai. Python mein text ki har cheez string hai: naam, pata, CNIC, poora paragraph.

| Tareeqa | Misaal | Kab |
|---|---|---|
| Single quotes | `'Lahore'` | Aam text |
| Double quotes | `"Ali's book"` | Jab text mein `'` ho |
| Triple quotes | `"""Kai\nlines"""` | Multi-line text, docstrings |

```python
# file: examples/01_creating_strings.py
city = 'Lahore'
book = "Ali's book"
quote = 'Usne kaha "Shukriya"'
address = """House 12, Street 5
Gulberg III
Lahore"""
empty = ""

print(city)
print(book)
print(quote)
print(address)
print("Khaali string ki lambai:", len(empty))
```

**Output:**
```
@@OUT examples/01_creating_strings.py@@
```

Single aur double quotes mein koi farq nahi. Bas aik hi string mein shuru aur aakhir mein aik jaise quotes hon. PEP 8 kisi aik ko lazmi nahi karta, magar poore project mein aik style rakhein. Is kitab mein double quotes istemal ho rahe hain.

---

## 4.2 Escape Characters Aur Raw Strings

**Yeh kya hai?** **Backslash (`\`)** ke baad aane wala character khaas matlab rakhta hai. Isay **escape sequence** kehte hain.

| Escape | Matlab |
|---|---|
| `\n` | Nayi line |
| `\t` | Tab (spacing) |
| `\\` | Asal backslash |
| `\'`, `\"` | Quote ko string ke andar rakhna |

```python
# file: examples/02_escape.py
print("Naam:\tAhmed\nShehar:\tKarachi")
print("Usne kaha \"Allah Hafiz\"")
print("Folder: C:\\Users\\Ali")

# Raw string: backslash ko as-is rakhta hai
print(r"C:\new\test")
print("C:\new\test")       # yahan \n aur \t escape ban gaye!
```

**Output:**
```
@@OUT examples/02_escape.py@@
```

**Raw string (`r"..."`)** mein backslash ka koi khaas matlab nahi hota. Windows file paths aur **regular expressions** (Chapter 14) ke liye yeh bohat kaam aata hai. Aakhri line mein `\n` ne nayi line bana di aur `\t` ne tab: yeh Windows paths ka mashhoor bug hai.

**⚠ Aam Ghalti:** Raw string ke aakhir mein akela backslash: `r"C:\folder\"` → `SyntaxError`. Paths ke liye behtar hal `pathlib` hai (Chapter 11).

---

## 4.3 Indexing Aur Slicing

**Yeh kya hai?** String ka har character aik **position (index)** par hai. Python mein ginti **0** se shuru hoti hai.

```
 String:   P   Y   T   H   O   N
 Index:    0   1   2   3   4   5
 Negative:-6  -5  -4  -3  -2  -1
```

**Indexing** aik character nikalta hai: `s[0]`. **Slicing** aik hissa nikalta hai: `s[start:stop:step]`.
- `start` **shamil** hota hai, `stop` **shamil nahi** hota.
- Koi hissa chhor dein to default lagta hai: `start=0`, `stop=aakhir tak`, `step=1`.

```python
# file: examples/03_indexing_slicing.py
word = "PYTHON"

print(word[0], word[5])       # pehla, aakhri
print(word[-1], word[-2])     # negative: aakhir se
print(word[0:3])              # 0,1,2 -> PYT
print(word[2:])               # index 2 se aakhir tak
print(word[:4])               # shuru se index 3 tak
print(word[::2])              # har doosra character
print(word[::-1])             # ulta (reverse)
print(word[1:100])            # slicing mein bari stop bhi chalti hai

cnic = "35202-1234567-1"
print("Area code:", cnic[:5])
print("Aakhri digit:", cnic[-1])
```

**Output:**
```
@@OUT examples/03_indexing_slicing.py@@
```

**Slicing ka formula:** `word[a:b]` mein `b - a` characters milte hain. `word[0:3]` = 3 characters.

**Out-of-range index par error:**
```python
# file: examples/04_index_error.py
word = "PYTHON"
print(word[6])
```
```
@@OUT examples/04_index_error.py@@
```
6 characters ka aakhri index **5** hai. Lekin slicing (`word[1:100]`) error nahi deti, woh jitna hai utna de deti hai.

**⚠ Aam Ghaltiyan**
- Ginti 1 se shuru karna: `word[1]` pehla nahi, **doosra** character hai.
- Samajhna ke `stop` shamil hai: `word[0:3]` mein index 3 shamil nahi.

---

## 4.4 Immutability — String Badalti Kyun Nahi?

```python
# file: examples/05_immutable_error.py
name = "Hamid"
name[0] = "Z"
```
```
@@OUT examples/05_immutable_error.py@@
```

Strings **immutable** hain (Chapter 2.9). Ek character bhi jagah par nahi badla ja sakta. Hal yeh hai ke **nayi string** banayi jaye:

```python
# file: examples/06_new_string.py
name = "Hamid"
name = "Z" + name[1:]
print(name)
print("Hamid".replace("H", "Z"))
```
```
@@OUT examples/06_new_string.py@@
```

**Immutability ka faida:** strings ko safely share kiya ja sakta hai, koi aur hissa unhein chupke se badal nahi sakta, aur woh dictionary keys ban sakti hain (Chapter 8).

---

## 4.5 Aham String Methods

**Method** woh function hai jo kisi object ke saath **dot (`.`)** laga kar call hota hai: `text.upper()`. Yaad rahe, string methods hamesha **nayi string** dete hain.

### Case aur safai
```python
# file: examples/07_methods_case.py
raw = "   pAKistan zINDABAD   "
print(f"[{raw.strip()}]")          # dono taraf ke spaces hatao
print(f"[{raw.lstrip()}]")         # sirf baayein
print(f"[{raw.rstrip()}]")         # sirf daayein
clean = raw.strip()
print(clean.upper())
print(clean.lower())
print(clean.title())               # har lafz ka pehla harf capital
print(clean.capitalize())          # sirf pehla harf capital
print(clean.swapcase())
```
```
@@OUT examples/07_methods_case.py@@
```

### Dhoondna aur ginna
```python
# file: examples/08_methods_search.py
sentence = "Python seekhna asaan hai aur Python mazedaar hai"
print(sentence.find("Python"))        # pehla index
print(sentence.find("Java"))          # na mile to -1
print(sentence.rfind("Python"))       # aakhri occurrence
print(sentence.count("hai"))
print(sentence.startswith("Python"))
print(sentence.endswith("hai"))
print("Python" in sentence)
```
```
@@OUT examples/08_methods_search.py@@
```

`.find()` na milne par `-1` deta hai. `.index()` bhi yahi karta hai lekin na milne par `ValueError` deta hai.

### Badalna, todna aur jorna
```python
# file: examples/09_methods_split_join.py
phone = "0300-123-4567"
print(phone.replace("-", ""))
print(phone.replace("-", " ", 1))     # sirf pehli dafa

csv_line = "Ali,Lahore,25,Engineer"
parts = csv_line.split(",")
print(parts)
print(parts[1])

words = "  Python   is   fun  ".split()     # baghair argument: kisi bhi whitespace par
print(words)

print(" | ".join(["Karachi", "Lahore", "Quetta"]))
print("-".join("ABC"))
```
```
@@OUT examples/09_methods_split_join.py@@
```

- `.split(",")` string ko tod kar **list** deti hai (lists Chapter 7 mein).
- `.split()` baghair argument ke spaces, tabs aur kai spaces ko aik samajhti hai, aur khaali hisse nikal deti hai.
- `separator.join(list)` ulta kaam karta hai. **Separator pehle** likha jata hai, yeh beginners ko ajeeb lagta hai.

### Validation methods
```python
# file: examples/10_methods_validate.py
print("12345".isdigit())
print("12.5".isdigit())        # point digit nahi
print("Ali".isalpha())
print("Ali Khan".isalpha())    # space alpha nahi
print("Room101".isalnum())
print("   ".isspace())
print("LAHORE".isupper(), "lahore".islower())
```
```
@@OUT examples/10_methods_validate.py@@
```

**Method reference:**
| Method | Kaam |
|---|---|
| `strip/lstrip/rstrip()` | Kinaron se whitespace (ya diye gaye characters) hatana |
| `upper/lower/title/capitalize/swapcase()` | Case badalna |
| `find/rfind/index()` | Position dhoondna |
| `count()` | Ginti |
| `startswith/endswith()` | Shuru/aakhir check |
| `replace(old, new[, count])` | Badalna |
| `split(sep)` / `sep.join(items)` | Todna / jorna |
| `isdigit/isalpha/isalnum/isspace/isupper/islower()` | Check (`bool`) |
| `zfill(n)` | Aage zero lagana: `"7".zfill(3)` → `"007"` |

**⚠ Aam Ghaltiyan**
- `text.upper` likhna, `()` ke baghair. Is se method khud milta hai, natija nahi.
- Natija assign na karna: `name.strip()` likh kar samajhna ke `name` saaf ho gaya.
- `"-12".isdigit()` → `False`. Minus sign digit nahi. Negative numbers ki validation ke liye `int()` aur exceptions (Chapter 12) behtar hain.

---

## 4.6 Concatenation vs `join()`

```python
# file: examples/11_concat_join.py
first = "Sana"
last = "Malik"
print(first + " " + last)          # + se jorna
print("=" * 20)                    # * se dohrana

cities = ["Lahore", "Karachi", "Peshawar", "Quetta"]

# + loop ke saath (dheema tareeqa)
result = ""
for c in cities:
    result += c + ", "
print(result)

# join (tez aur saaf)
print(", ".join(cities))
```
```
@@OUT examples/11_concat_join.py@@
```

**Kyun `join()` behtar hai?** Strings immutable hain, is liye har `+=` aik **poori nayi string** banata hai. Hazaron items par yeh bohat dheema ho jata hai. `join()` sab ko aik hi dafa jorta hai. Saath mein loop wale tareeqe mein aakhir par aik faltu `", "` bhi bacha, jo `join()` mein nahi hota. (`for` loop Chapter 6 mein seekhenge.)

---

## 4.7 f-string Formatting Mini-Language

Format spec ki poori shakal: `{value:[fill][align][width][,][.precision][type]}`

| Hissa | Values | Misaal |
|---|---|---|
| align | `<` baayein, `>` daayein, `^` beech | `{name:<10}` |
| fill | koi bhi character (align se pehle) | `{name:*^10}` |
| width | kul jagah | `{x:8}` |
| `,` / `_` | hazaron ka separator | `{n:,}` |
| precision | decimals | `{x:.2f}` |
| type | `f` float, `d` int, `%`, `e` scientific, `b` binary, `x` hex | `{n:b}` |

```python
# file: examples/12_fstring_format.py
items = [("Chai", 80, 3), ("Biryani", 450, 2), ("Kheer", 150, 1)]

print(f"{'Item':<10}{'Rate':>8}{'Qty':>5}{'Total':>10}")
print("-" * 33)
for name, rate, qty in items:
    print(f"{name:<10}{rate:>8,}{qty:>5}{rate * qty:>10,.2f}")
print("-" * 33)

print(f"[{'MIAVRO':^14}]")
print(f"[{'MIAVRO':*^14}]")
print(f"Invoice #{7:05d}")
print(f"{0.4567:.1%} | {1234567.891:,.2f} | {255:b} | {255:x} | {0.000123:.2e}")

width = 12
print(f"[{'dynamic':>{width}}]")      # width bhi variable se
```
```
@@OUT examples/12_fstring_format.py@@
```

Is mein `for` loop aur list of tuples aage ke chapters ka hissa hain. Yahan sirf formatting par dhyan dein. **Report aur receipts ke liye yeh alignment bohat kaam aati hai.**

---

## 4.8 `len()`, `in` Aur Unicode Basics

```python
# file: examples/13_unicode.py
greeting = "Assalam o Alaikum"
print(len(greeting))
print("Alaikum" in greeting)

emoji = "Pakistan 🇵🇰"
print(len(emoji))                 # flag do code points se banta hai

print(ord("A"), ord("a"))         # character -> Unicode number
print(chr(66), chr(9731))         # number -> character
print("café".upper())
```
```
@@OUT examples/13_unicode.py@@
```

**Unicode** duniya ki har zaban aur emoji ke characters ka aik standard hai, aur har character ka aik number (**code point**) hota hai. Python 3 ki har string Unicode hai. `len()` code points ginta hai, jo nazar aane wale characters se mukhtalif ho sakte hain (jaise flag emoji 2 code points hai). Files ke saath kaam karte waqt hamesha `encoding="utf-8"` istemal karein (Chapter 11).

---

## 🌍 Real World
- **Form validation:** `email.strip().lower()`, `"@" in email`, `phone.isdigit()`.
- **Data cleaning:** Pandas ke `.str.strip()`, `.str.lower()`, `.str.replace()` bilkul inhi methods par mabni hain (Chapter 18).
- **Reports:** aligned columns wale invoices aur receipts.
- **URLs/slugs:** `"Mera Pehla Blog".lower().replace(" ", "-")` → `mera-pehla-blog`.

---

## Chapter Summary
1. Strings `'`, `"` ya `"""` se banti hain. Escape `\n`, `\t`, `\\` hote hain. Raw string `r"..."`.
2. Indexing 0 se shuru hoti hai, negative index aakhir se. Slicing `[start:stop:step]` mein `stop` shamil nahi. `[::-1]` string ulat deta hai.
3. Strings **immutable** hain. Methods nayi string dete hain, is liye natija assign karein.
4. Ahem methods: `strip`, `lower/upper/title`, `find/count`, `replace`, `split/join`, `startswith/endswith`, `is...()`.
5. Bohat si strings jorni hon to `join()` istemal karein, loop mein `+=` nahi.
6. f-string spec: `{x:<10}`, `{x:>8,.2f}`, `{x:^12}`, `{n:05d}`, `{p:.1%}`.
7. Python 3 strings Unicode hain. `len()` code points ginta hai. `ord()`/`chr()`.

---

## Exercises

### 🟢 Exercise 1 — Naam ke hisse
`full_name = "muhammad ali jinnah"`. Ise title case mein print karein, aur pehla naam aur aakhri naam alag print karein (`split`).

### 🟢 Exercise 2 — Slicing practice
`s = "MIAVROSYSTEMS"`. Slicing se nikaalein: `MIAVRO`, `SYSTEMS`, aakhri 3 characters, ulti string, har teesra character.

### 🟢 Exercise 3 — Initials
User se poora naam lein aur initials print karein (e.g. `Sana Ahmed Malik` → `S.A.M.`).

### 🟢 Exercise 4 — Safai
`"   ALI@Example.COM  "` ko saaf, lowercase email mein badlein aur check karein ke us mein `@` hai aur woh `.com` par khatam hota hai.

### 🟡 Exercise 5 — Palindrome
User se lafz lein aur batayein ke woh palindrome hai ya nahi (ulta aur seedha aik jaisa, e.g. `Madam`). Case ko ignore karein.

### 🟡 Exercise 6 — Word counter
Aik sentence mein kitne alfaaz hain, kitne characters hain (spaces ke baghair), aur lafz `"hai"` kitni dafa aaya?

### 🟡 Exercise 7 — Phone format
User se 11-digit mobile number lein (e.g. `03001234567`). Check karein ke sab digits hain, lambai 11 hai aur `03` se shuru hota hai, phir use `0300-1234567` format mein print karein.

### 🔴 Exercise 8 — CNIC validator
User se CNIC lein (e.g. `35202-1234567-1`). Check karein: kul lambai 15, index 5 aur 13 par `-`, aur dash hatane ke baad 13 digits. Natija `True`/`False` mein, aur valid ho to province code (pehla digit) bhi batayein.

### 🔴 Exercise 9 — URL slug
Blog ka title lein (e.g. `"  Python Seekhein: Zero Se Hero!  "`) aur slug banayein: lowercase, `:` aur `!` hatayein, spaces ko `-` mein badlein, aur extra spaces na hon → `python-seekhein-zero-se-hero`.

### 🔴 Exercise 10 — Formatted price list
Teen products (naam, qeemat) ki aik aligned table print karein: naam baayein 15 characters, qeemat daayein 12 characters comma aur 2 decimals ke saath, aur aakhir mein total. Table ka title `=` ki border ke saath centered ho.

---

## Complete Solutions

### Solution 1
```python
# file: solutions/ex01_name_parts.py
full_name = "muhammad ali jinnah"
proper = full_name.title()
parts = proper.split()
print(proper)
print("Pehla naam:", parts[0])
print("Aakhri naam:", parts[-1])
```
```
@@OUT solutions/ex01_name_parts.py@@
```

### Solution 2
```python
# file: solutions/ex02_slicing.py
s = "MIAVROSYSTEMS"
print(s[:6])
print(s[6:])
print(s[-3:])
print(s[::-1])
print(s[::3])
```
```
@@OUT solutions/ex02_slicing.py@@
```

### Solution 3
<!-- stdin: Sana Ahmed Malik -->
```python
# file: solutions/ex03_initials.py
name = input("Poora naam: ")
words = name.split()
initials = ".".join(w[0].upper() for w in words) + "."
print(initials)
```
```
@@OUT solutions/ex03_initials.py@@
```
`w[0].upper() for w in words` aik **generator expression** hai: har lafz ka pehla harf. Yeh Chapter 14 mein tafseel se aayega. Isay is tarah bhi likh sakte hain: `words[0][0] + "." + words[1][0] + "." + ...`, magar woh sirf teen alfaaz ke liye chalega.

### Solution 4
```python
# file: solutions/ex04_email_clean.py
raw = "   ALI@Example.COM  "
email = raw.strip().lower()
print(email)
print("@ hai?", "@" in email)
print(".com par khatam?", email.endswith(".com"))
```
```
@@OUT solutions/ex04_email_clean.py@@
```
**Method chaining:** `raw.strip().lower()` mein pehle `strip()` chala, phir us ke natije par `lower()`.

### Solution 5
<!-- stdin: Madam -->
```python
# file: solutions/ex05_palindrome.py
word = input("Lafz: ")
normalized = word.lower()
print(f"'{word}' palindrome hai?", normalized == normalized[::-1])
```
```
@@OUT solutions/ex05_palindrome.py@@
```

### Solution 6
```python
# file: solutions/ex06_word_counter.py
sentence = "Python asaan hai aur Python ki community bari hai"
words = sentence.split()
print("Alfaaz:", len(words))
print("Characters (spaces ke baghair):", len(sentence.replace(" ", "")))
print("'hai' ki ginti:", words.count("hai"))
```
```
@@OUT solutions/ex06_word_counter.py@@
```
`sentence.count("hai")` ke bajaye `words.count("hai")` istemal kiya. String par `count` lafz ke andar chhupe "hai" (jaise "hairat") ko bhi gin leta. List ka `count` sirf poore alfaaz ginta hai.

### Solution 7
<!-- stdin: 03001234567 -->
```python
# file: solutions/ex07_phone.py
phone = input("Mobile number: ").strip()
is_valid = phone.isdigit() and len(phone) == 11 and phone.startswith("03")
print("Valid:", is_valid)
print("Formatted:", phone[:4] + "-" + phone[4:])
```
```
@@OUT solutions/ex07_phone.py@@
```
Invalid number par formatting ko rokna `if` ke saath Chapter 5 mein seekhenge.

### Solution 8
<!-- stdin: 35202-1234567-1 -->
```python
# file: solutions/ex08_cnic.py
cnic = input("CNIC: ").strip()
digits = cnic.replace("-", "")
is_valid = (len(cnic) == 15 and cnic[5] == "-" and cnic[13] == "-"
            and digits.isdigit() and len(digits) == 13)
print("Valid:", is_valid)
print("Province code:", cnic[0])
```
```
@@OUT solutions/ex08_cnic.py@@
```
Parentheses `( ... )` ki wajah se lambi condition do lines mein likhi ja saki. Yeh PEP 8 ka pasandeeda tareeqa hai. Short-circuiting ki wajah se agar lambai ghalat ho to `cnic[13]` check hi nahi hota, is liye `IndexError` nahi aata.

### Solution 9
```python
# file: solutions/ex09_slug.py
title = "  Python Seekhein: Zero Se Hero!  "
cleaned = title.strip().lower().replace(":", "").replace("!", "")
slug = "-".join(cleaned.split())
print(slug)
```
```
@@OUT solutions/ex09_slug.py@@
```
`split()` phir `join()` ka jora extra spaces khatam karne ka mashhoor tareeqa hai.

### Solution 10
```python
# file: solutions/ex10_price_list.py
p1, price1 = "Basmati Rice", 1850.0
p2, price2 = "Cooking Oil", 2675.5
p3, price3 = "Tea 950g", 1399.0
total = price1 + price2 + price3

print("=" * 27)
print(f"{'PRICE LIST':^27}")
print("=" * 27)
print(f"{p1:<15}{price1:>12,.2f}")
print(f"{p2:<15}{price2:>12,.2f}")
print(f"{p3:<15}{price3:>12,.2f}")
print("-" * 27)
print(f"{'TOTAL':<15}{total:>12,.2f}")
```
```
@@OUT solutions/ex10_price_list.py@@
```

---

## Agla Qadam
Chapter 5 mein program **faislay** karna seekhega: `if`, `elif`, `else`, truthiness, ternary expression aur modern `match-case`. Phir Exercise 7 aur 8 ki validation sahi tareeqe se ho sakegi.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
