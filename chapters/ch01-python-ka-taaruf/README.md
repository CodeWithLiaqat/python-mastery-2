# Chapter 1 — Programming Aur Python Ka Ta'aruf

> **PYTHON MASTERY — Zero Se Advanced Python Programming Aur Data Science Tak**
> Roman Urdu Edition · MIAVRO Systems · https://miavrosystems.com
> Part 1: Absolute Beginner

---

## Chapter Opener

**Is chapter mein aap seekhenge:**
- Program aur programming language asal mein kya hote hain
- Python kyun itni popular hai aur kahan kahan istemal hoti hai
- Compiled aur interpreted languages ka farq, aur Python interpreter kaise kaam karta hai
- Apne computer par Python aur VS Code install karna
- REPL (interactive mode) aur `.py` script ka farq
- Apna pehla program likhna aur chalana
- Comments likhna
- Errors ko darne ke bajaye parhna aur samajhna

**Prerequisites:** Koi nahi. Bas computer chalana aana chahiye: file save karna, folder banana aur software install karna.

**Andaazan study time:** 2–3 ghante (install samait)

**Companion code:** `chapters/ch01-python-ka-taaruf/` — https://github.com/CodeWithLiaqat/python-mastery-2

---

## 1.1 Program Aur Programming Language Kya Hai?

### Yeh concept kya hai?
**Program** instructions ka aik set hota hai jo computer ko step-by-step batata hai ke kya karna hai. **Programming language** woh zaban hai jis mein hum yeh instructions likhte hain.

Ise aik recipe ki tarah samjhein. Recipe mein likha hota hai: "pehle pani garam karein, phir chai patti daalein, phir doodh daalein." Agar steps ghalat tarteeb mein hon, ya koi step ghayab ho, to chai sahi nahi banegi. Computer bhi bilkul yahi karta hai: jo likha hai, usi tarteeb mein, bilkul waisa hi karta hai. Woh khud se andaza nahi lagata.

### Iski zaroorat kyun hoti hai?
Computer andar se sirf **machine code** samajhta hai, yaani 0 aur 1 ke patterns. Insaan ke liye machine code mein likhna taqreeban na-mumkin hai. Programming language beech ka pul hai: hum insaan ke samajhne layak instructions likhte hain, aur aik software (compiler ya interpreter) unhein computer ki zaban mein badal deta hai.

### Yeh kaise kaam karta hai?
```
Aap ka code (Python)  →  Interpreter  →  Machine instructions  →  Result
```

### Real World
Har cheez jo aap phone ya computer par istemal karte hain, program hai: WhatsApp, banking app, Daraz ki website, ATM machine ka software, traffic signals ka system.

### 💡 Ghalat Fehmi
> "Programming sirf math ke maahir log kar sakte hain."

Ghalat. Programming ka asal hunar **masle ko chhote steps mein todna** hai. Data Science mein math zaroor kaam aata hai, lekin woh hum zaroorat ke mutabiq step-by-step seekhenge.

---

## 1.2 Python Kyun?

### Yeh kya hai?
Python aik **high-level, general-purpose** programming language hai. Ise Guido van Rossum ne banaya aur pehla version 1991 mein release hua.

- **High-level** ka matlab hai ke yeh insaani zaban ke qareeb hai. Memory jaisi technical cheezein Python khud sambhalta hai.
- **General-purpose** ka matlab hai ke yeh kisi aik kaam tak mehdood nahi.

### Iski zaroorat kyun hai? Python hi kyun?
| Khoobi | Faida |
|---|---|
| Saaf aur parhne mein asaan syntax | Beginners jaldi seekhte hain |
| Bohat bari standard library | Bohat se kaam ke liye tools pehle se maujood |
| Third-party packages (NumPy, Pandas, Django…) | Har field ke liye ready-made tools |
| Bara community support | Har sawal ka jawab online mil jata hai |
| Free aur open source | Koi license fee nahi |

### Python kahan istemal hoti hai?
- **Data Science aur Analytics:** Pandas, NumPy, Matplotlib (is kitab ka Part 5)
- **Artificial Intelligence / Machine Learning:** Scikit-learn, TensorFlow, PyTorch
- **Web Development:** Django, Flask, FastAPI
- **Automation:** Excel reports banana, files arrange karna, emails bhejna
- **Scripting aur DevOps:** servers aur deployment ka kaam

### Kab use karein?
Data analysis, automation, AI aur backend ke liye Python behtareen choice hai. Mobile apps ya bohat high-performance games ke liye doosri languages (Kotlin, Swift, C++) zyada behtar hain. Har tool ki apni jagah hai.

---

## 1.3 Compiled vs Interpreted Language — Python Interpreter Kaise Kaam Karta Hai

### Yeh concept kya hai?
Code ko machine tak pohanchane ke do bunyadi tareeqe hain:

| | Compiled (e.g. C, C++) | Interpreted (e.g. Python) |
|---|---|---|
| Tareeqa | Poora code pehle machine code mein convert hota hai, phir chalta hai | Code ko aik program (interpreter) parh kar chalata hai |
| Natija | Alag executable file (`.exe`) banti hai | `.py` file seedhi interpreter se chalti hai |
| Speed | Aam tor par zyada tez | Nisbatan dheema, magar likhna aur test karna tez |

### Python asal mein kaise kaam karta hai?
Python "sirf interpreted" nahi hai. Andar teen steps hote hain:

```
hello.py  →  [1] Bytecode mein compile  →  [2] Python Virtual Machine (PVM)  →  [3] Output
```

1. Jab aap `python hello.py` chalate hain, Python aap ke code ko pehle **bytecode** mein badalta hai. Bytecode aik darmiyani, simplified instruction set hai.
2. Phir **Python Virtual Machine (PVM)** us bytecode ko line-by-line chalati hai.
3. Imported modules ka bytecode `__pycache__` folder mein `.pyc` files ki shakal mein save ho jata hai, taake agli dafa tez chale.

Yeh sab automatic hota hai. Aap ko sirf `.py` file likhni hai.

### 💡 Ghalat Fehmi
> "Interpreted ka matlab hai Python har line ko alag alag, error ke baad bhi chalata rehta hai."

Ghalat. Section 1.9 mein aap dekhenge ke agar file mein **syntax error** ho to Python aik line bhi nahi chalata, kyun ke bytecode banane ka step hi fail ho jata hai.

---

## 1.4 Python Install Karna

> ⚠ **Pehle se maloom rukawatein:**
> 1. Windows par "Add python.exe to PATH" ka checkbox na lagana. Yeh sab se aam masla hai.
> 2. Windows par `python` likhne se Microsoft Store khul jana (App Execution Aliases).
> 3. macOS par `python` command na milna. Wahan `python3` likhna hota hai.
> 4. Python install karne ke baad purana terminal khula rehna. Naya terminal kholein.

### Windows
1. https://www.python.org/downloads/ par jayein.
2. **"Download Python 3.x.x"** (latest stable, 3.12 ya us se naya) par click karein.
3. Installer chalayein. Pehli screen par:
   - ✅ **"Add python.exe to PATH"** zaroor tick karein
   - **"Install Now"** par click karein
4. Install hone ke baad **naya** Command Prompt ya PowerShell kholein aur likhein:
   ```
   python --version
   ```
   **Expected output** (aap ka number mukhtalif ho sakta hai):
   ```
   Python 3.12.7
   ```
5. Agar Microsoft Store khul jaye: **Settings → Apps → Advanced app settings → App execution aliases** mein `python.exe` aur `python3.exe` ke aliases **Off** kar dein. Phir naya terminal kholein.

### macOS
1. python.org se macOS installer download karke install karein.
2. **Terminal** kholein aur likhein:
   ```
   python3 --version
   ```
   macOS par is kitab mein jahan `python` likha ho, wahan `python3` likhein.

### Linux (Ubuntu/Debian)
Aksar Python pehle se install hota hai:
```
python3 --version
```
Agar na ho: `sudo apt update && sudo apt install python3 python3-pip python3-venv`

### PATH kya hai?
**PATH** operating system ki aik list hai jis mein woh folders hote hain jahan system commands dhoondta hai. Agar Python ka folder PATH mein na ho to terminal ko `python` command milti hi nahi, aur yeh error aata hai:
```
'python' is not recognized as an internal or external command
```
**Hal:** Installer dobara chalayein → **Modify** → "Add Python to environment variables" tick karein. Ya uninstall karke PATH wale checkbox ke saath dobara install karein.

---

## 1.5 Coding Ka Mahol: VS Code, Jupyter Aur Google Colab

### VS Code (Part 1–4 ke liye mukhya tool)
**Visual Studio Code** aik free **code editor** hai. Is mein code likhna, chalana aur errors dhoondna (debugging) asaan hai.

**Setup steps:**
1. https://code.visualstudio.com se download karke install karein.
2. VS Code kholein → baayein taraf **Extensions** icon (ya `Ctrl+Shift+X`).
3. Search karein **"Python"** → Microsoft wala extension → **Install**.
4. Apne computer par aik folder banayein, misaal ke tor par `python-mastery`.
5. VS Code mein **File → Open Folder** → yeh folder chunein.
6. **New File** → naam `hello.py` → save.
7. Neeche-daayein kone mein Python version nazar aana chahiye. Agar na aaye: `Ctrl+Shift+P` → **"Python: Select Interpreter"** → apna installed Python chunein.

### Jupyter Notebook aur Google Colab (Part 5 ke liye)
**Jupyter Notebook** mein code chhote hisson (**cells**) mein likha aur chalaya jata hai, aur output har cell ke neeche foran nazar aata hai. Data Science mein yeh standard tool hai. Hum Chapter 16 mein ise tafseel se seekhenge.

**Google Colab** (https://colab.research.google.com) browser mein chalne wala free Jupyter notebook hai. Kuch install karne ki zaroorat nahi, sirf Google account chahiye. Agar aap ke computer par install mein masla aaye to Part 1–4 ke examples bhi Colab mein chal sakte hain.

| Tool | Kab use karein |
|---|---|
| VS Code + `.py` files | Programs, projects, automation, apps |
| Jupyter / Colab | Data exploration, charts, analysis, experiments |

---

## 1.6 REPL (Interactive Mode) vs `.py` Script

### Yeh concept kya hai?
Python code chalane ke do bunyadi tareeqe hain:

**1. REPL — Read, Evaluate, Print, Loop**
Terminal mein sirf `python` (macOS/Linux par `python3`) likhein. Python aap ki aik line **parhta** (Read) hai, use **chalata** (Evaluate) hai, result **dikhata** (Print) hai, aur agli line ka intezar karta hai (Loop).

```
>>> 7 * 6
42
>>> "Pakistan"
'Pakistan'
>>> exit()
```
- `>>>` **prompt** hai, yaani Python aap ki input ka intezar kar raha hai. Ise khud type nahi karna.
- REPL se nikalne ke liye `exit()` likhein, ya Windows par `Ctrl+Z` phir Enter, aur macOS/Linux par `Ctrl+D`.

**2. Script — `.py` file**
Code file mein likha jata hai, save hota hai, aur poori file aik saath chalti hai:
```
python hello.py
```

### Kab kya use karein?
| REPL | Script (`.py`) |
|---|---|
| Chhoti cheez foran test karni ho | Asal program likhna ho |
| Calculator ki tarah istemal | Code save, share aur dobara chalana ho |
| Code band karte hi khatam ho jata hai | File hamesha mehfooz rehti hai |

### ⚠ Aam Ghalti: REPL aur script ka farq
REPL har expression ka result **khud** dikha deta hai. Script aisa **nahi** karti.

`ex10_repl_vs_script.py`:
```python
6 * 7
```
REPL mein `6 * 7` likhne se `42` nazar aata hai, lekin isi line ko script mein chalane se **kuch bhi nazar nahi aata**. Python ne hisaab to kiya, magar dikhane ka hukm nahi diya gaya. Script mein output ke liye `print()` lazmi hai.

### ⚠ Aam Ghalti: `>>>` copy kar lena
Kitabon ya websites se code copy karte waqt beginners `>>> print("Hi")` poora copy kar lete hain. `>>>` code ka hissa nahi, sirf REPL ka prompt hai.

---

## 1.7 Pehla Program: `print()`

### Yeh concept kya hai?
`print()` Python ka aik **built-in function** hai. **Built-in** ka matlab hai ke yeh Python ke andar pehle se maujood hai. Is ka kaam hai jo cheez is ke parentheses `()` ke andar di jaye, use screen par dikhana. Functions ko hum Chapter 9 mein gehrai se seekhenge. Abhi itna samajh lein ke function aik "kaam karne wali mashin" hai, aur `()` ke andar hum use input dete hain.

### Zaroorat kyun?
Program jo kuch bhi kare, user ko result dikhana zaroori hai. `print()` output ka sab se bunyadi tareeqa hai, aur debugging mein bhi sab se zyada istemal hota hai.

### Syntax
```python
print(value)
print(value1, value2, value3)
print()
```

### Example 1 — Hello Python
`examples/01_hello.py`:
```python
# Mera pehla Python program
print("Assalam o Alaikum, Python!")
```
**Chalayein:** VS Code mein file save karein aur upar-daayein ▶ (Run) button dabayein, ya terminal mein:
```
python 01_hello.py
```
**Output:**
```
Assalam o Alaikum, Python!
```
**Line-by-line:**
| Line | Purpose |
|---|---|
| `# Mera pehla Python program` | Comment (1.8 mein). Python ise ignore karta hai |
| `print(...)` | Built-in function ko call kiya |
| `"Assalam o Alaikum, Python!"` | **String**, yaani quotes ke andar text. Strings Chapter 2 aur 4 mein |

### Example 2 — Kai lines
`examples/02_multiple_prints.py`:
```python
# Har print() apni alag line mein output deta hai
print("Mera naam Ahmed hai.")
print("Main Lahore se hoon.")
print("Main Python seekh raha hoon.")
```
**Output:**
```
Mera naam Ahmed hai.
Main Lahore se hoon.
Main Python seekh raha hoon.
```
Python upar se neeche, aik line ke baad doosri chalata hai. Isay **sequential execution** kehte hain. Har `print()` khatam hone par agli line par chala jata hai.

### Example 3 — Text aur number ka farq
`examples/03_print_values.py`:
```python
# Text (string) aur number mein farq
print("2 + 3")      # quotes ke andar: yeh sirf text hai
print(2 + 3)        # quotes ke baghair: Python hisaab karta hai
print("Kul students:", 45)   # comma se multiple values, beech mein space
print()                      # khaali print() aik khaali line deta hai
print("Program khatam.")
```
**Output:**
```
2 + 3
5
Kul students: 45

Program khatam.
```
**Line-by-line:**
| Line | Kya hua aur kyun |
|---|---|
| `print("2 + 3")` | Quotes ke andar sab kuch text hai, is liye Python ne hisaab nahi kiya |
| `print(2 + 3)` | Quotes nahi hain, is liye Python ne `2 + 3` ko expression samjha, hisaab kiya aur `5` dikhaya |
| `print("Kul students:", 45)` | Comma (`,`) se kai values di ja sakti hain. Python khud beech mein aik **space** daal deta hai |
| `print()` | Kuch nahi diya gaya, is liye sirf aik khaali line aayi |

> Operators (`+`, `-`, `*`, `/`) ki poori tafseel Chapter 3 mein hai. Yahan sirf yeh dekhna hai ke quotes ka hona ya na hona kitna farq daalta hai.

### ⚠ Aam Ghaltiyan
| Ghalti | Kya hoga | Sahi |
|---|---|---|
| `Print("Hi")` | `NameError`. Python **case-sensitive** hai | `print("Hi")` |
| `print("Hi)` | `SyntaxError`. Quote band nahi hua | `print("Hi")` |
| `print "Hi"` | `SyntaxError`. Yeh purane Python 2 ka style hai | `print("Hi")` |
| `print(“Hi”)` | `SyntaxError`. Word processor ke "curly quotes" | Seedhe quotes `"` ya `'` |
| `print("Hi')` | `SyntaxError`. Shuru aur khatam ke quotes mukhtalif hain | Dono taraf aik jaise quotes |

> 💡 **Tip:** Code kabhi MS Word ya WhatsApp mein na likhein. Woh quotes ko curly bana dete hain. Hamesha code editor (VS Code) istemal karein.

### 💡 Ghalat Fehmi
> "`print()` value ko save kar leta hai."

Nahi. `print()` sirf screen par **dikhata** hai. Value ko yaad rakhne ke liye **variables** chahiye hote hain (Chapter 2).

---

## 1.8 Comments Aur Code Readability

### Yeh concept kya hai?
**Comment** code mein likha gaya woh note hai jo **insaanon ke liye** hota hai. Python use bilkul ignore karta hai. Python mein comment `#` se shuru hota hai, aur `#` ke baad line ke aakhir tak sab kuch comment hai.

### Zaroorat kyun?
- Code **likha** aik dafa jata hai, magar **parha** bar bar jata hai, aap ki taraf se bhi aur team ki taraf se bhi.
- Chhe mahine baad aap khud bhool jayenge ke yeh code kyun likha tha.
- Testing ke dauran kisi line ko waqti tor par band karne ke liye ("commenting out").

### Syntax
```python
# Poori line ka comment
print("Hi")  # Line ke aakhir mein comment (inline comment)
```

### Example
`examples/04_comments.py`:
```python
# ==========================================
# Program: Dukaan ka welcome message
# Likhne wala: Ali
# ==========================================

# Customer ko welcome karna
print("Ali General Store mein khush aamdeed!")

print("Aaj ki special offer: Doodh 10% discount")  # yeh line offer dikhati hai

# print("Yeh line nahi chalegi kyun ke yeh comment hai")
print("Shukriya!")
```
**Output:**
```
Ali General Store mein khush aamdeed!
Aaj ki special offer: Doodh 10% discount
Shukriya!
```
**Line-by-line:**
- Pehli 4 lines **header comment** hain: program ka maqsad aur likhne wala.
- Inline comment (`# yeh line offer dikhati hai`) code ke saath hi wazahat hai.
- `# print("Yeh line nahi chalegi...")` **commented out** code hai, is liye output mein nazar nahi aaya.

> ⌨ **VS Code shortcut:** Lines select karke `Ctrl+/` (macOS: `Cmd+/`) dabayein. Sab lines aik saath comment/uncomment ho jayengi.

### Achay comments ke usool
| ❌ Bekaar comment | ✅ Faidemand comment |
|---|---|
| `print("Hi")  # Hi print karo` (code khud yahi keh raha hai) | `# GST 18% hai — FBR ke 2024 rules ke mutabiq` (**kyun** batata hai) |

**Usool:** Code batata hai **kya** ho raha hai. Comment batata hai **kyun**.

### ⚠ Aam Ghaltiyan
- Har line par comment likh dena. Is se code parhna mushkil ho jata hai.
- Code badal dena magar purana comment na badalna. Ghalat comment, comment na hone se bhi bura hai.
- Comment ko `//` se shuru karna (JavaScript/C style). Python mein `//` floor division operator hai, comment nahi.

### 💡 Ghalat Fehmi
> "Triple quotes `"""..."""` Python ke multi-line comments hain."

Technically nahi. Triple quotes ek **string** banate hain. Agar woh kisi variable mein na rakhi jaye to Python use istemal nahi karta, is liye comment jaisa lagta hai. Function ke shuru mein yeh **docstring** kehlata hai (Chapter 9). Asal comment ka tareeqa sirf `#` hai.

---

## 1.9 Errors: Syntax Error vs Runtime Error — Traceback Parhna

### Yeh concept kya hai?
Error ka matlab hai ke Python aap ka code samajh ya chala nahi saka. **Errors programming ka normal hissa hain.** Professional developers rozana errors dekhte hain. Farq sirf yeh hai ke woh error **parhna** jaante hain.

Do bunyadi qisam:
| | Syntax Error | Runtime Error (Exception) |
|---|---|---|
| Kya hai | Code Python ki grammar ke mutabiq nahi | Grammar theek hai magar chalte waqt masla aaya |
| Kab pakra jata hai | Chalne **se pehle** (bytecode banate waqt) | Chalne ke **dauran**, us line par pohanch kar |
| Natija | **Aik line bhi nahi chalti** | Error wali line se **pehle** ki lines chal jati hain |
| Misaal | Bracket band na karna | Ghalat naam, zero se taqseem |

### Example 1 — Syntax Error
`examples/05_syntax_error.py`:
```python
print("Hello")
print("Python"
print("World")
```
**Output:**
```
  File ".../05_syntax_error.py", line 2
    print("Python"
         ^
SyntaxError: '(' was never closed
```
**Isay kaise parhein:**
| Hissa | Matlab |
|---|---|
| `File ".../05_syntax_error.py", line 2` | Masla **kis file** aur **kis line** mein hai |
| `print("Python"` | Masle wali line |
| `^` | Taqreeban kis jagah masla hai |
| `SyntaxError: '(' was never closed` | Error ki qisam aur wazahat: bracket khula reh gaya |

**Ahem baat:** `print("Hello")` line 1 par hai aur bilkul theek hai, phir bhi **"Hello" print nahi hua.** Wajah yeh hai ke syntax error poori file ko chalne se pehle hi rok deta hai (yaad karein section 1.3 ka bytecode step).

> **Note:** File ka poora path (`...`) aap ke computer ke hisaab se mukhtalif hoga. Error ke `^` / `~` markers Python ke version ke mutabiq thore mukhtalif ho sakte hain. Is kitab ke outputs Python 3.12+ ke hain.

### Example 2 — Runtime Error (NameError)
`examples/06_runtime_error.py`:
```python
print("Line 1 chal gayi")
print("Line 2 chal gayi")
prnt("Line 3")
print("Line 4")
```
**Output:**
```
Line 1 chal gayi
Line 2 chal gayi
Traceback (most recent call last):
  File ".../06_runtime_error.py", line 3, in <module>
    prnt("Line 3")
    ^^^^
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```
**Line-by-line:**
- Line 1 aur 2 **chal gayin**. Grammar ke lihaz se poori file theek thi, is liye program shuru ho gaya.
- Line 3 par Python ko `prnt` naam ki koi cheez nahi mili, is liye **`NameError`** aaya.
- Line 4 **nahi chali**. Error aate hi program ruk jata hai.
- `Did you mean: 'print'?`: naya Python khud sahi lafz ka mashwara bhi deta hai.

### Example 3 — Runtime Error (ZeroDivisionError)
`examples/07_zero_division.py`:
```python
print("Total rupees: 1000")
print("Har dost ka hissa:", 1000 / 0)
```
**Output:**
```
Total rupees: 1000
Traceback (most recent call last):
  File ".../07_zero_division.py", line 2, in <module>
    print("Har dost ka hissa:", 1000 / 0)
                                ~~~~~^~~
ZeroDivisionError: division by zero
```
Math mein zero se taqseem mumkin nahi, is liye Python bhi yeh nahi kar sakta. `~~~~~^~~` exact hissa dikhata hai jahan masla hai.

### Traceback parhne ka 4-step formula
1. **Sab se aakhri line pehle parhein.** Error ki qisam aur wazahat wahin hoti hai (`NameError: ...`).
2. **Line number dekhein.** `line 3` jaisa hissa batata hai ke kahan dekhna hai.
3. **Markers dekhein.** `^` ya `~` exact jagah ki taraf ishara karte hain.
4. **Masla theek karein aur dobara chalayein.** Aik waqt mein aik error.

> Traceback **neeche se upar** parhi jati hai. Bare programs mein yeh kai functions se guzarti hai. Is ka tafseeli tareeqa Chapter 12 mein hai.

### ⚠ Aam Ghaltiyan
- Error dekh kar ghabra jana aur poora code mita dena. Error aap ka **madadgaar** hai, woh masle ki jagah bata raha hai.
- Sirf pehli line parh kar ruk jana. Asal wazahat **aakhri** line mein hai.
- Aik saath kai changes karke chalana. Aik cheez theek karein, phir chalayein.

### 💡 Ghalat Fehmi
> "Error aane ka matlab hai mera program bekaar hai."

Bilkul nahi. Error sirf yeh batata hai ke aik khaas jagah aik chhoti si cheez theek karni hai. Experienced developers bhi har roz errors dekhte hain.

### Bonus — Apna Python version code se check karna
`examples/08_check_version.py`:
```python
import sys

print("Python version:", sys.version_info.major, sys.version_info.minor)
```
**Output** (misaal; aap ka version mukhtalif ho sakta hai):
```
Python version: 3 12
```
- `import sys` Python ka built-in `sys` module laata hai, jis mein system ki maloomat hoti hai. Modules Chapter 10 mein.
- `sys.version_info.major` → `3`, `sys.version_info.minor` → `12`

---

## 🌍 Real World: Yeh Sab Kahan Kaam Aata Hai?
- **`print()`**: professional developers debugging ke liye rozana `print()` se check karte hain ke kis waqt kya value hai.
- **Comments**: software houses mein code review ke dauran saaf comments wala code jaldi approve hota hai.
- **Traceback parhna**: job interviews mein aksar aik error wala code de kar poocha jata hai: "masla kya hai?"
- **REPL**: Data Scientists chhote calculations aur idea test karne ke liye REPL ya Jupyter istemal karte hain.

---

## Chapter Summary
1. **Program** computer ke liye instructions ka set hai. **Python** aik high-level, general-purpose, beginner-friendly language hai.
2. Python code pehle **bytecode** mein compile hota hai, phir **Python Virtual Machine** use chalati hai.
3. Windows par install karte waqt **"Add python.exe to PATH"** zaroor tick karein. macOS/Linux par `python3` likhein.
4. **VS Code** programs ke liye, aur **Jupyter/Colab** data analysis ke liye.
5. **REPL** foran test ke liye hai aur result khud dikhata hai. **Script** mein output ke liye `print()` zaroori hai.
6. `print()` screen par output dikhata hai. Comma se kai values aati hain. Quotes ke andar text hai, baghair quotes expression.
7. **Comment** `#` se shuru hota hai. Achay comment **"kyun"** batate hain.
8. **Syntax error** mein aik line bhi nahi chalti. **Runtime error** mein error wali line se pehle ki lines chal jati hain.
9. Traceback ki **aakhri line pehle** parhein, phir line number aur markers dekhein.

---

## Exercises

> 🟢 Asaan · 🟡 Darmiyana · 🔴 Mushkil
> Pehle khud koshish karein. Hint tab dekhein jab 10 minute koshish ke baad bhi raasta na mile.

### 🟢 Exercise 1 — Apna ta'aruf
Aik program likhein jo teen alag lines mein aap ka naam, shehar aur Python seekhne ka maqsad print kare.
**Hint:** Teen `print()` statements.

### 🟢 Exercise 2 — Comments ki practice
Aik program likhein jo aap ki pasandeeda cheezon ka title, khana aur khel print kare. Har `print()` ke upar aik comment ho jo batata ho ke yeh line kya kar rahi hai.
**Hint:** `#` se comment shuru karein.

### 🟢 Exercise 3 — REPL calculator
Terminal mein REPL kholein (`python` ya `python3`) aur yeh hisaab karein. Phir `exit()` se bahar aa jayein.
```
125 + 375
1000 - 250
12 * 12
100 / 8
```
**Hint:** REPL mein `print()` ki zaroorat nahi.

### 🟢 Exercise 4 — Output predict karein
Chalane se **pehle** kaghaz par likhein ke yeh program kya dikhayega. Phir chala kar check karein.
```python
print("10 + 5")
print(10 + 5)
print("Jawab:", 10 + 5)
```
**Hint:** Quotes ke andar sab text hai.

### 🟡 Exercise 5 — Visiting card
`print()` istemal karte hue aik box ki shakal ka visiting card banayein jis mein naam, profession, shehar aur email ho.
**Hint:** Box ke kinare `+`, `-` aur `|` characters se banayein. Har line ki lambai barabar rakhne ke liye spaces ginein.

### 🟡 Exercise 6 — Bug hunter
Is code mein **teen** ghaltiyan hain. Har ghalti dhoondein, batayein ke kaunsa error aayega, aur code theek karein.
```python
print("Pakistan Zindabad)
Print("Python seekhna asaan hai")
print("Shukriya"
```
**Hint:** Quotes, capital letters aur brackets dhyan se dekhein. Python aik waqt mein sirf **pehla** syntax error dikhata hai, is liye theek karke bar bar chalayein.

### 🟡 Exercise 7 — Aik `print()` mein kai values
Sirf **do** `print()` statements se yeh output banayein, aur numbers ko quotes ke baghair likhein:
```
Product: Chai | Qeemat: 80 PKR
Product: Samosa | Qeemat: 50 PKR
```
**Hint:** Comma har value ke beech khud space daalta hai.

### 🔴 Exercise 8 — Traceback detective
Chalane se **pehle** batayein: (a) kaunsi lines print hongi, (b) kaunsa error aayega, (c) kis line par, (d) kyun. Phir chala kar check karein aur code theek karein.
```python
print("Order receive ho gaya")
print("Payment check ho rahi hai")
Print("Order confirm")
print("Delivery rawana")
```
**Hint:** Yeh syntax error hai ya runtime error? Is sawal ka jawab hi bata dega ke pehli do lines chalengi ya nahi.

### 🔴 Exercise 9 — Chai dhaba ki receipt
Aik customer ne order diya: 3 chai (80 PKR each), 2 paratha (60 PKR each), 1 omelette (150 PKR). Aik receipt print karein jis mein har item ki qeemat aur kul bill ho. **Shart:** totals khud hisaab karke na likhein, Python se hisaab karwayein.
**Hint:** `print("Chai x3 :", 3 * 80, "PKR")`. Multiplication ke liye `*`.

### 🔴 Exercise 10 — REPL vs Script
`6 * 7` ko pehle REPL mein likhein, phir aik `.py` file mein likh kar chalayein. Dono ke natije mein kya farq hai aur kyun? Script ko theek karein taake woh `42` dikhaye.
**Hint:** REPL ke naam ka "P" kis cheez ke liye hai?

---

## Complete Solutions

### Solution 1
`solutions/ex01_introduction.py`
```python
# Exercise 1 (Asaan): Apna ta'aruf
print("Naam: Ayesha Khan")
print("Shehar: Karachi")
print("Maqsad: Main Data Scientist banna chahti hoon.")
```
**Output:**
```
Naam: Ayesha Khan
Shehar: Karachi
Maqsad: Main Data Scientist banna chahti hoon.
```
Har `print()` alag line mein output deta hai (sequential execution). Apni maloomat daal kar chalayein.

### Solution 2
`solutions/ex02_comments.py`
```python
# Exercise 2 (Asaan): Har line ke upar comment

# Program ka title dikhana
print("=== Meri Pasandeeda Cheezein ===")

# Pasandeeda khana
print("Khana: Biryani")

# Pasandeeda khel
print("Khel: Cricket")
```
**Output:**
```
=== Meri Pasandeeda Cheezein ===
Khana: Biryani
Khel: Cricket
```
Comments output mein nazar nahi aate. Python unhein ignore karta hai.

### Solution 3
```
>>> 125 + 375
500
>>> 1000 - 250
750
>>> 12 * 12
144
>>> 100 / 8
12.5
>>> exit()
```
REPL har expression ka result khud dikhata hai. Ghaur karein ke `100 / 8` ka jawab `12.5` hai, yaani decimal number (`float`). `/` hamesha decimal deta hai. Is ki wajah Chapter 2 aur 3 mein samjhayi gayi hai.

### Solution 4
**Output:**
```
10 + 5
15
Jawab: 15
```
- Line 1: quotes mein hai, is liye text jaisa hai waisa print hua.
- Line 2: expression hai, is liye `15` aaya.
- Line 3: text `"Jawab:"` aur expression ka natija `15`, beech mein comma ki wajah se space.

### Solution 5
`solutions/ex05_visiting_card.py`
```python
# Exercise 5 (Darmiyana): Visiting card
print("+--------------------------------+")
print("|  Sana Malik                    |")
print("|  Python Developer              |")
print("|  Lahore, Pakistan              |")
print("|  sana@example.com              |")
print("+--------------------------------+")
```
**Output:**
```
+--------------------------------+
|  Sana Malik                    |
|  Python Developer              |
|  Lahore, Pakistan              |
|  sana@example.com              |
+--------------------------------+
```
Har line bilkul 34 characters ki hai, is liye box seedha nazar aata hai. Chapter 4 mein f-string alignment (`:<30`) seekh kar yeh kaam khud ba khud hoga.

### Solution 6
**Ghaltiyan:**
| Line | Ghalti | Error |
|---|---|---|
| 1 | `"Pakistan Zindabad` ka quote band nahi | `SyntaxError: unterminated string literal` |
| 2 | `Print` capital P ke saath | `NameError: name 'Print' is not defined` |
| 3 | `)` band nahi kiya | `SyntaxError: '(' was never closed` |

**Ahem:** Pehli dafa chalane par sirf line 1 ka `SyntaxError` nazar aayega. Use theek karne ke baad line 3 ka `SyntaxError` aayega, kyun ke syntax errors chalne se pehle pakre jate hain. Line 2 ka `NameError` runtime error hai, is liye woh sab se aakhir mein, program chalne ke dauran saamne aayega.

`solutions/ex06_fixed.py`
```python
# Exercise 6 (Darmiyana): Teeno ghaltiyan theek kar di gayi hain
print("Pakistan Zindabad")
print("Python seekhna asaan hai")
print("Shukriya")
```
**Output:**
```
Pakistan Zindabad
Python seekhna asaan hai
Shukriya
```

### Solution 7
`solutions/ex07_multi_values.py`
```python
# Exercise 7 (Darmiyana): Aik print() mein multiple values
print("Product:", "Chai", "| Qeemat:", 80, "PKR")
print("Product:", "Samosa", "| Qeemat:", 50, "PKR")
```
**Output:**
```
Product: Chai | Qeemat: 80 PKR
Product: Samosa | Qeemat: 50 PKR
```
`print()` ko 5 alag values di gayin. Python ne har do values ke beech aik space daala. `80` aur `50` numbers hain (quotes ke baghair), aur `print()` text aur numbers dono ko aik saath dikha sakta hai.

### Solution 8
**(a)** Pehli do lines print hongi. **(b)** `NameError`. **(c)** Line 3. **(d)** `Print` capital "P" ke saath Python mein koi cheez nahi. Python case-sensitive hai, is liye `Print` aur `print` alag naam hain. Yeh **runtime error** hai: grammar sahi thi, is liye program shuru hua aur line 3 par pohanch kar ruk gaya. Line 4 nahi chali.

**Output (asal code):**
```
Order receive ho gaya
Payment check ho rahi hai
Traceback (most recent call last):
  File ".../ex08_traceback.py", line 4, in <module>
    Print("Order confirm")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```
(Companion file mein upar aik comment line hai, is liye wahan line number 4 dikhega. Kitab wale 4-line code mein yahi error line 3 par aayega.)

**Theek kiya hua code:**
```python
print("Order receive ho gaya")
print("Payment check ho rahi hai")
print("Order confirm")
print("Delivery rawana")
```

### Solution 9
`solutions/ex09_dhaba_receipt.py`
```python
# Exercise 9 (Mushkil): Chai dhaba ki receipt
# Order: 3 chai (80 PKR each), 2 paratha (60 PKR each), 1 omelette (150 PKR)
print("===== Bismillah Chai Dhaba =====")
print("Chai     x3 :", 3 * 80, "PKR")
print("Paratha  x2 :", 2 * 60, "PKR")
print("Omelette x1 :", 1 * 150, "PKR")
print("--------------------------------")
print("Kul Bill    :", 3 * 80 + 2 * 60 + 1 * 150, "PKR")
print("================================")
print("Dobara tashreef laiyega!")
```
**Output:**
```
===== Bismillah Chai Dhaba =====
Chai     x3 : 240 PKR
Paratha  x2 : 120 PKR
Omelette x1 : 150 PKR
--------------------------------
Kul Bill    : 510 PKR
================================
Dobara tashreef laiyega!
```
**Line-by-line:**
- `3 * 80` Python ne khud hisaab kiya → `240`.
- `3 * 80 + 2 * 60 + 1 * 150`: math ki tarah Python pehle multiplication karta hai, phir addition: `240 + 120 + 150 = 510`. Is usool (operator precedence) ki tafseel Chapter 3 mein hai.
- **Behtari ki gunjaish:** qeematein bar bar likhi gayi hain. Agar chai ki qeemat badle to kai jagah badalna parega. Chapter 2 ke **variables** yahi masla hal karte hain.

### Solution 10
- **REPL mein:** `6 * 7` likhne par `42` nazar aata hai, kyun ke REPL ka "P" = **Print**, yaani woh har expression ka natija khud dikhata hai.
- **Script mein:** kuch nazar nahi aata. Python ne hisaab kiya, magar dikhane ka hukm nahi diya gaya.

`solutions/ex10_repl_vs_script.py`
```python
# Exercise 10 (Mushkil): Script mein yeh line kuch nahi dikhati
6 * 7
# Hal: result dekhne ke liye print() zaroori hai
print(6 * 7)
```
**Output:**
```
42
```
Sirf aik `42` aaya, jo `print(6 * 7)` se hai. Pehli line ne hisaab kiya magar kuch nahi dikhaya.

---

## Agla Qadam
Chapter 2 mein hum **variables** seekhenge, jin ke zariye program values yaad rakh sakta hai. Saath mein **data types** (`int`, `float`, `str`, `bool`, `None`), `input()` se user ki baat sunna, aur **f-strings** se khoobsurat output banana bhi seekhenge. Exercise 9 ki receipt wahan behtar tareeqe se dobara banayenge.

---
*© MIAVRO Systems · Python Mastery (Roman Urdu Edition) · https://miavrosystems.com*
