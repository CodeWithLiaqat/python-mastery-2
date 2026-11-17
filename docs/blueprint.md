# PYTHON MASTERY — Zero Se Advanced Python Programming Aur Data Science Tak
## Roman Urdu Edition · Complete Publishing Blueprint (v1.1 — Approved)

**Publisher:** MIAVRO Systems · https://miavrosystems.com
**Target:** 100 pages (front matter + 23 chapters + appendices)
**Audience:** Pakistani students, absolute beginners, aspiring developers, career switchers
**Python version:** Python 3.12+ (modern Python 3 practices)
**Status:** Approved · Chapter 1 mukammal
**Format:** Print (hard copy) + companion repo: https://github.com/CodeWithLiaqat/python-mastery-2

> Note: Abhi koi alag English edition syllabus maujood nahi hai. Yeh blueprint dono editions ka **master syllabus** banega — chapter numbering, examples, projects aur exercises dono mein bilkul same rahenge.

---

## 1. Book Ka Structure (6 Parts)

| Part | Level | Chapters | Pages |
|---|---|---|---|
| Front Matter | — | — | 4 |
| Part 1 | Absolute Beginner | 1–3 | 12 |
| Part 2 | Beginner | 4–8 | 18 |
| Part 3 | Intermediate | 9–13 | 19 |
| Part 4 | Advanced Python | 14–15 | 8 |
| Part 5 | Python for Data Science | 16–22 | 26 |
| Part 6 | Capstone Project | 23 | 5 |
| Back Matter | Appendices A–E | — | 8 |
| **Total** | | **23** | **100** |

---

## 2. Detailed Table of Contents + Page Allocation

### FRONT MATTER (pp. 1–4)
- p.1 — Title page (MIAVRO Systems branding)
- p.2 — Copyright, edition info, publisher details, code license
- p.3 — Muqaddama (Preface) + "Yeh Kitab Kaise Parhein" (icons/boxes ki legend, learning path, companion code ka link)
- p.4 — Table of Contents (chapter level)

---

### PART 1 — ABSOLUTE BEGINNER (pp. 5–16)

#### Chapter 1 — Programming Aur Python Ka Ta'aruf (pp. 5–8 · 4 pages)
**Prerequisites:** Koi nahi — sirf computer chalana aana chahiye
**Learning objectives:** Programming, interpreter aur Python ka role samajhna · Python + VS Code install karna · Pehla program likhna aur chalana · Error message parhna seekhna
**Subtopics:**
1.1 Program aur programming language kya hai (computer instructions kaise samajhta hai)
1.2 Python kyun? — use cases (web, automation, data science, AI)
1.3 Compiled vs interpreted language; Python interpreter aur bytecode (overview)
1.4 Python install karna (Windows/macOS/Linux) + PATH ka masla
1.5 VS Code setup + Python extension; Jupyter Notebook aur Google Colab ka ta'aruf
1.6 REPL (interactive mode) vs `.py` script
1.7 Pehla program: `print("Assalam o Alaikum, Python!")`
1.8 Comments (`#`) aur code readability
1.9 Syntax error vs runtime error — traceback parhna (pehli dafa)
**Exercises:** 3 (apna naam/shehar print karna, comment likhna, jaan boojh kar error bana kar parhna)

#### Chapter 2 — Variables, Data Types Aur Input/Output (pp. 9–13 · 5 pages)
**Prerequisites:** Ch 1
**Learning objectives:** Variables banana aur naming rules follow karna · Core data types pehchanna · Type conversion · User se input lena aur formatted output dena
**Subtopics:**
2.1 Variable kya hai — named reference (memory model: name → object)
2.2 Naming rules, PEP 8 conventions (`snake_case`), reserved keywords
2.3 Core types: `int`, `float`, `str`, `bool`, `NoneType`
2.4 `type()` aur `id()` — dynamic typing
2.5 Type conversion: `int()`, `float()`, `str()`, `bool()` — implicit vs explicit
2.6 `input()` — hamesha `str` deta hai (sab se aam ghalti)
2.7 Output: `print()` ke `sep`, `end`; f-strings (`f"{naam}"`, `:.2f`, `:,`)
2.8 Multiple assignment, swapping, constants convention (`UPPER_CASE`)
2.9 Mutable vs immutable — pehla ta'aruf
**Solved example:** Age calculator (birth year se umar)
**Exercises:** 4

#### Chapter 3 — Operators Aur Expressions (pp. 14–16 · 3 pages)
**Prerequisites:** Ch 2
**Learning objectives:** Har operator category use karna · Precedence samajhna · Float precision ke masle pehchanna
**Subtopics:**
3.1 Arithmetic: `+ - * / // % **` — `/` vs `//`, negative numbers ke saath `//` aur `%`
3.2 Assignment aur augmented operators (`+=`, `-=` …)
3.3 Comparison operators aur chained comparison (`0 < x < 10`)
3.4 Logical: `and`, `or`, `not` + short-circuiting
3.5 Membership (`in`, `not in`) aur identity (`is`, `is not`) — `is` vs `==`
3.6 Operator precedence table
3.7 Float precision (`0.1 + 0.2`), `round()`, `abs()`, `divmod()`
**Mini Project 1:** Bill Splitter + Tip Calculator (PKR mein)
**Exercises:** 4

---

### PART 2 — BEGINNER (pp. 17–34)

#### Chapter 4 — Strings Gehrai Se (pp. 17–20 · 4 pages)
**Prerequisites:** Ch 2–3
**Learning objectives:** Indexing/slicing · String methods · Immutability · Professional formatting
**Subtopics:**
4.1 String creation: single, double, triple quotes; multiline
4.2 Escape characters (`\n`, `\t`, `\\`) aur raw strings (`r"..."`)
4.3 Indexing (positive/negative) aur slicing `[start:stop:step]`, reverse `[::-1]`
4.4 Immutability — "string change kyun nahi hoti?"
4.5 Common methods: `upper/lower/title/strip/replace/split/join/find/count/startswith/endswith/isdigit/isalpha`
4.6 Concatenation vs `join()` (performance)
4.7 f-string formatting mini-language (alignment, padding, percentages)
4.8 `len()`, `in`, Unicode basics (Roman Urdu text, emoji)
**Exercises:** 4 (palindrome check, word counter, CNIC/phone format validation)

#### Chapter 5 — Faislay Karna: Conditional Statements (pp. 21–23 · 3 pages)
**Prerequisites:** Ch 3–4
**Learning objectives:** `if/elif/else` likhna · Truthiness samajhna · `match-case` use karna
**Subtopics:**
5.1 `if`, `elif`, `else` — indentation ki ahmiyat
5.2 Nested conditions aur unhe flat karna
5.3 Truthy aur falsy values (`0`, `""`, `[]`, `None`)
5.4 Conditional expression (ternary): `x if cond else y`
5.5 `match-case` (Python 3.10+) — structural pattern matching basics
5.6 Input validation patterns
**Solved example:** Grade calculator (marks → A/B/C/F)
**Exercises:** 4 (leap year, electricity bill slabs, login check)

#### Chapter 6 — Loops: Kaam Ko Dohrana (pp. 24–27 · 4 pages)
**Prerequisites:** Ch 5
**Learning objectives:** `while` aur `for` loops · `range`, `enumerate`, `zip` · Loop control · Common loop patterns
**Subtopics:**
6.1 `while` loop, condition update, infinite loop se bachna
6.2 `for` loop aur iterables; `range(start, stop, step)`
6.3 `break`, `continue`, `pass`; loop ka `else` clause
6.4 Nested loops (patterns, tables)
6.5 `enumerate()` aur `zip()`
6.6 Patterns: counter, accumulator, max/min tracking, search, flag
6.7 Built-ins: `sum`, `min`, `max`, `any`, `all`
**Mini Project 2:** Number Guessing Game (`random` ke saath, attempts limit)
**Exercises:** 4 (multiplication table, FizzBuzz, prime check, digit sum)

#### Chapter 7 — Lists Aur Tuples (pp. 28–31 · 4 pages)
**Prerequisites:** Ch 6
**Learning objectives:** Lists create/modify karna · References aur copying samajhna · Tuples aur unpacking · Sorting
**Subtopics:**
7.1 List creation, indexing, slicing, `len`
7.2 Methods: `append/extend/insert/remove/pop/index/count/clear/reverse`
7.3 Iteration aur list ke saath loops
7.4 Mutability, aliasing aur copying: `=` vs `.copy()` vs `copy.deepcopy()`
7.5 Nested lists (2D data / matrix)
7.6 `sorted()` vs `.sort()`, `key=` aur `reverse=`
7.7 List comprehension (basic): `[x*2 for x in nums if x > 0]`
7.8 Tuples: immutability, single-element tuple `(5,)`, packing/unpacking, `*rest`
7.9 List vs tuple — kab kya use karein
**Exercises:** 4 (second largest, remove duplicates preserving order, matrix sum)

#### Chapter 8 — Dictionaries Aur Sets (pp. 32–34 · 3 pages)
**Prerequisites:** Ch 7
**Learning objectives:** Key-value data model karna · Dict methods · Set operations · Sahi data structure choose karna
**Subtopics:**
8.1 Dict creation, access (`[]` vs `.get()`), add/update/delete
8.2 Methods: `keys/values/items/update/pop/setdefault`
8.3 Dict iteration aur nested dicts (JSON jaisa data)
8.4 Dict comprehension
8.5 Hashable keys — list key kyun nahi ban sakti
8.6 Sets: uniqueness, `add/remove/discard`, union/intersection/difference
8.7 Comparison table: list vs tuple vs dict vs set
**Mini Project 3:** Student Grade Manager (dict of students, average, topper)
**Exercises:** 4 (word frequency, phone book, common items in two lists)

---

### PART 3 — INTERMEDIATE (pp. 35–53)

#### Chapter 9 — Functions (pp. 35–39 · 5 pages)
**Prerequisites:** Part 2
**Learning objectives:** Reusable functions design karna · Har tarah ke arguments · Scope · Recursion aur functional tools
**Subtopics:**
9.1 `def`, call, `return` vs `print` (sab se aam confusion)
9.2 Parameters vs arguments; positional, keyword, default values
9.3 Mutable default argument trap (`def f(x=[])`)
9.4 `*args` aur `**kwargs`; keyword-only aur positional-only parameters
9.5 Scope — LEGB rule; `global` aur `nonlocal`
9.6 Docstrings aur type hints (`def add(a: int, b: int) -> int:`)
9.7 Functions as first-class objects; `lambda`
9.8 `map`, `filter`, `sorted(key=lambda ...)`
9.9 Recursion: base case, factorial, recursion limit
**Solved example:** Reusable input validator function
**Exercises:** 5

#### Chapter 10 — Modules, Packages Aur pip (pp. 40–41 · 2 pages)
**Prerequisites:** Ch 9
**Learning objectives:** Code ko modules mein organize karna · Standard library use karna · `pip` aur virtual environments
**Subtopics:**
10.1 `import`, `from ... import`, aliasing (`as`)
10.2 Apna module banana; `if __name__ == "__main__":`
10.3 Standard library tour: `math`, `random`, `datetime`, `os`, `pathlib`, `collections` (`Counter`, `defaultdict`), `statistics`
10.4 Packages aur `__init__.py`
10.5 `pip install`, `venv` banana/activate karna, `requirements.txt`
**Exercises:** 3

#### Chapter 11 — File Handling Aur Data Formats (pp. 42–44 · 3 pages)
**Prerequisites:** Ch 10
**Learning objectives:** Files parhna/likhna safely · CSV aur JSON handle karna · Paths ko sahi manage karna
**Subtopics:**
11.1 `open()` modes (`r`, `w`, `a`, `x`, `b`), encoding (`utf-8`)
11.2 `with` statement (context manager) — kyun zaroori hai
11.3 `read()`, `readline()`, `readlines()`, line-by-line iteration
11.4 `pathlib.Path` — cross-platform paths, file exists check
11.5 `csv` module (`reader`, `DictReader`, `DictWriter`)
11.6 `json` module (`load/dump/loads/dumps`)
11.7 Web API se JSON data — `requests` ka chhota ta'aruf
**Exercises:** 3

#### Chapter 12 — Errors, Exceptions Aur Debugging (pp. 45–47 · 3 pages)
**Prerequisites:** Ch 11
**Learning objectives:** Tracebacks parhna · Exceptions handle aur raise karna · Systematic debugging
**Subtopics:**
12.1 Syntax errors vs exceptions; common exceptions (`ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`)
12.2 Traceback ko neeche se upar parhna
12.3 `try / except / else / finally`
12.4 Multiple aur specific exceptions — bare `except:` kyun bura hai
12.5 `raise` aur custom exception classes
12.6 Debugging: print debugging, VS Code debugger (breakpoints, step over), `assert`
12.7 `logging` module basics
**Exercises:** 3

#### Chapter 13 — Object-Oriented Programming (OOP) (pp. 48–53 · 6 pages)
**Prerequisites:** Ch 9, 12
**Learning objectives:** Classes design karna · OOP ke 4 pillars · Dunder methods · `dataclasses`
**Subtopics:**
13.1 OOP kyun — procedural vs object-oriented
13.2 Class vs object; `__init__` aur `self`
13.3 Instance attributes vs class attributes
13.4 Instance methods, `@classmethod`, `@staticmethod`
13.5 Encapsulation: `_protected`, `__private` (name mangling), `@property` getters/setters
13.6 Inheritance, `super()`, method overriding
13.7 Polymorphism aur duck typing
13.8 Abstraction: `abc.ABC` aur `@abstractmethod`
13.9 Dunder methods: `__str__`, `__repr__`, `__len__`, `__eq__`, `__lt__`, `__add__`
13.10 Composition vs inheritance
13.11 `@dataclass` — modern Python way
**Mini Project 4:** Bank Account System (accounts, deposit/withdraw, custom `InsufficientFundsError`, JSON mein save)
**Exercises:** 4

---

### PART 4 — ADVANCED PYTHON (pp. 54–61)

#### Chapter 14 — Advanced Python Features (pp. 54–58 · 5 pages)
**Prerequisites:** Part 3
**Learning objectives:** Comprehensions, iterators, generators, decorators aur context managers mein mahirat · Regex basics
**Subtopics:**
14.1 Comprehensions: list, dict, set, nested; generator expressions; kab comprehension use NA karein
14.2 Iterables vs iterators: `iter()`, `next()`, `__iter__`/`__next__`
14.3 Generators aur `yield` — memory efficiency (bari files)
14.4 Closures
14.5 Decorators: function wrapping, `functools.wraps`, arguments wale decorators (timer, logger example)
14.6 Custom context managers: class-based aur `contextlib.contextmanager`
14.7 `itertools` (`chain`, `groupby`, `combinations`) aur `functools` (`reduce`, `lru_cache`, `partial`)
14.8 Unpacking advanced (`*`, `**`), walrus operator `:=`
14.9 `re` module: `search`, `findall`, `sub`, common patterns (email, phone)
14.10 Git aur GitHub basics: `init`, `add`, `commit`, `status`, `log`, `.gitignore`, `push`, apna code GitHub par rakhna
**Exercises:** 4

#### Chapter 15 — Professional Python: Best Practices, Testing Aur Performance (pp. 59–61 · 3 pages)
**Prerequisites:** Ch 14
**Learning objectives:** Clean, testable, maintainable code likhna · Project structure · Performance ki bunyadi samajh
**Subtopics:**
15.1 PEP 8, naming, "Pythonic" code (Zen of Python)
15.2 Project structure (`src/`, `tests/`, `requirements.txt`, `README`)
15.3 Testing: `assert`, `pytest` basics, test cases likhna
15.4 Type hints advanced (`list[int]`, `dict[str, float]`, `Optional`, `|` union) + type checker ka ta'aruf
15.5 Time complexity / Big-O ka asaan ta'aruf; list vs set lookup
15.6 `timeit` se code measure karna
**Mini Project 5:** Log File Analyzer (generator + regex + `Counter` + tests)
**Exercises:** 3

---

### PART 5 — PYTHON FOR DATA SCIENCE (pp. 62–87)

#### Chapter 16 — Data Science Ka Ta'aruf Aur Environment (pp. 62–63 · 2 pages)
**Prerequisites:** Part 3 (Part 4 recommended)
**Learning objectives:** Data Science workflow samajhna · Jupyter/Colab mein kaam karna · Libraries install karna
**Subtopics:**
16.1 Data Science kya hai; Data Analyst vs Data Scientist vs ML Engineer
16.2 Workflow: Question → Collect → Clean → Explore → Model → Communicate
16.3 Data types: structured/unstructured, numerical/categorical
16.4 Jupyter Notebook / JupyterLab / Google Colab — cells, kernels, markdown
16.5 Libraries install: `pip install numpy pandas matplotlib seaborn scipy scikit-learn`
**Exercises:** 2

#### Chapter 17 — NumPy (pp. 64–67 · 4 pages)
**Prerequisites:** Ch 16, Ch 7
**Learning objectives:** `ndarray` banana aur manipulate karna · Vectorization aur broadcasting · Aggregations axis ke saath
**Subtopics:**
17.1 NumPy kyun — list vs array (speed, memory)
17.2 Array creation: `array`, `zeros`, `ones`, `arange`, `linspace`, `eye`
17.3 `shape`, `ndim`, `size`, `dtype`; `reshape`, `flatten`, `ravel`
17.4 Indexing, slicing (2D), fancy indexing, boolean masking
17.5 Vectorized operations aur universal functions (`np.sqrt`, `np.exp`)
17.6 Broadcasting rules (visual diagram)
17.7 Aggregations: `sum/mean/std/min/max/argmax` + `axis`
17.8 `np.random.default_rng(seed)` — reproducible random data
17.9 Linear algebra basics: dot product, matrix multiplication (`@`), transpose
17.10 View vs copy (aam ghalti)
**Exercises:** 4

#### Chapter 18 — Pandas: Data Analysis Ka Asal Hathyar (pp. 68–74 · 7 pages)
**Prerequisites:** Ch 17
**Learning objectives:** Real data load, clean, transform aur summarize karna · `groupby`, merge, pivot mein mahirat
**Subtopics:**
18.1 `Series` aur `DataFrame` — index ka concept
18.2 Data load: `read_csv`, `read_excel`, `read_json`; save: `to_csv`, `to_excel`
18.3 Inspection: `head/tail/shape/info/describe/dtypes/value_counts/nunique`
18.4 Selection: column(s), `loc` (label) vs `iloc` (position)
18.5 Filtering: boolean conditions, `&`/`|`, `isin`, `between`, `query`
18.6 Columns add/rename/drop; `assign`
18.7 Missing data: `isna`, `dropna`, `fillna`, strategy choose karna
18.8 Duplicates aur data types fix karna (`astype`, `to_numeric`, `to_datetime`)
18.9 String operations (`.str`) aur datetime operations (`.dt`)
18.10 Sorting: `sort_values`, `sort_index`, `nlargest`
18.11 `apply`, `map`, vectorized alternatives (apply ka overuse se bachna)
18.12 `groupby` + `agg` (multiple aggregations), split-apply-combine
18.13 `merge` / `join` / `concat` — join types (inner, left, outer) diagram ke saath
18.14 `pivot_table` aur `crosstab`
18.15 `SettingWithCopyWarning` aur `.copy()` — aam masla
**Mini Project 6:** Online Store Sales Analysis (city-wise, month-wise revenue, top products — Pakistani context, PKR)
**Exercises:** 5

#### Chapter 19 — Matplotlib: Data Visualization (pp. 75–76 · 2 pages)
**Prerequisites:** Ch 18
**Learning objectives:** Sahi chart choose karna · Figure/Axes API se professional charts banana
**Subtopics:**
19.1 Figure aur Axes — `plt` vs object-oriented API (`fig, ax = plt.subplots()`)
19.2 Line, bar, horizontal bar, scatter, histogram, pie (aur pie kab avoid karein)
19.3 Titles, labels, legends, ticks, colors, styles
19.4 Subplots (multiple charts aik figure mein)
19.5 `savefig` (dpi, PNG/PDF), Pandas `.plot()` shortcut
**Exercises:** 3

#### Chapter 20 — Seaborn: Statistical Visualization (pp. 77–78 · 2 pages)
**Prerequisites:** Ch 19
**Learning objectives:** Distributions, relationships aur categories ko Seaborn se visualize karna
**Subtopics:**
20.1 Seaborn vs Matplotlib; themes (`set_theme`)
20.2 Distribution: `histplot`, `kdeplot`, `boxplot`, `violinplot`
20.3 Categorical: `countplot`, `barplot`
20.4 Relationship: `scatterplot` (`hue`, `size`), `lineplot`, `regplot`
20.5 `heatmap` (correlation matrix), `pairplot`
**Exercises:** 3

#### Chapter 21 — Data Science Ke Liye Statistics (pp. 79–82 · 4 pages)
**Prerequisites:** Ch 18, 20
**Learning objectives:** Descriptive statistics calculate aur interpret karna · Distributions, correlation aur hypothesis testing ka bunyadi framework
**Subtopics:**
21.1 Population vs sample; types of variables
21.2 Central tendency: mean, median, mode — skewed data mein kaunsa?
21.3 Spread: range, variance, standard deviation, percentiles, IQR
21.4 Outliers: IQR method aur z-score
21.5 Probability basics aur distributions: uniform, normal (68-95-99.7 rule), binomial (overview)
21.6 Sampling aur Central Limit Theorem (simulation ke zariye)
21.7 Correlation (Pearson) — correlation ≠ causation
21.8 Hypothesis testing intro: null/alternative, p-value ka sahi matlab, t-test (`scipy.stats`)
**Mini Project 7:** Student Performance Statistical Report
**Exercises:** 4

#### Chapter 22 — Machine Learning Ka Ta'aruf: Scikit-learn (pp. 83–87 · 5 pages)
**Prerequisites:** Ch 17–21
**Learning objectives:** ML workflow samajhna · Regression aur classification model train/evaluate karna · Overfitting pehchanna
**Subtopics:**
22.1 Machine Learning kya hai; supervised vs unsupervised; regression vs classification
22.2 Features (X) aur target (y); Scikit-learn ka `fit / predict / score` pattern
22.3 `train_test_split` — data leakage kya hai
22.4 Preprocessing: missing values, categorical encoding (`OneHotEncoder`), scaling (`StandardScaler`)
22.5 Linear Regression + metrics (MAE, RMSE, R²)
22.6 Classification: Logistic Regression aur Decision Tree / KNN
22.7 Classification metrics: accuracy, confusion matrix, precision, recall, F1
22.8 Overfitting vs underfitting; cross-validation (`cross_val_score`)
22.9 `Pipeline` aur `ColumnTransformer`
22.10 Unsupervised glimpse: K-Means clustering
22.11 Model save/load (`joblib`) aur aage ka raasta
**Mini Project 8:** House Price Prediction (Lahore/Karachi-style synthetic dataset)
**Exercises:** 4

---

### PART 6 — CAPSTONE (pp. 88–92)

#### Chapter 23 — Capstone Project: End-to-End Data Analysis & Prediction (pp. 88–92 · 5 pages)
**Prerequisites:** Poori kitab
**Project:** "PakMart" online store — customer aur sales data
**Stages:**
1. Problem statement aur business questions
2. Messy dataset generate/load (missing values, duplicates, ghalat types)
3. Data cleaning pipeline (functions + Pandas)
4. EDA: statistics + Matplotlib/Seaborn charts
5. Insights (top cities, seasonal trends, customer segments)
6. ML model: repeat-purchase prediction (classification) ya next-month revenue (regression)
7. Results report aur next steps
**Deliverable:** Clean, modular, commented notebook + charts + short findings report
**Extension challenges:** 3

---

### BACK MATTER (pp. 93–100)
- **Appendix A (p.93):** Python Core Cheat Sheet
- **Appendix B (p.94):** NumPy · Pandas · Matplotlib · Seaborn · Scikit-learn Cheat Sheet
- **Appendix C (p.95):** 25 aam errors aur unke fixes (error message → wajah → hal)
- **Appendix D (pp.96–99):** Exercise solutions (har chapter ke selected exercises ke detailed solutions; baqi ke concise solutions)
- **Appendix E (p.100):** Glossary (English term → Roman Urdu wazahat), aage kya seekhein (Git, SQL, Deep Learning, web frameworks), MIAVRO Systems ka ta'aruf

---

## 3. Har Chapter Ka Standard Template

Har chapter is fixed order mein likha jayega:

1. **Chapter Opener** — title, learning objectives, prerequisites, estimated study time
2. **Concept sections** — har important concept 10-point framework ke saath:
   - Kya hai? · Kyun zaroorat? · Kaise kaam karta hai? · Kab use karein?
   - **Syntax box**
   - **Code block** (complete, runnable)
   - **Output box** (exact expected output)
   - **Line-by-line explanation**
   - **⚠ Aam Ghaltiyan** box
   - **💡 Ghalat Fehmi** (misconception) box
   - **🌍 Real World** box (practical application)
3. **Solved Example** (hal shuda misaal)
4. **Chapter Summary** (key points, 5–8 bullets)
5. **Exercises** — levels: 🟢 Asaan / 🟡 Darmiyana / 🔴 Mushkil, har exercise ke saath hint
6. **Mini Project** (jahan allocate hai)

**Page density ka usool:** Major concepts (variables, loops, functions, OOP, Pandas groupby, ML workflow) ko poora 10-point treatment milega. Chhote/related concepts (e.g. string methods, Matplotlib styling) ko compact tables aur combined code examples mein cover kiya jayega taake 100-page budget mein koi topic skip na ho.

---

## 4. Projects Aur Exercises Ka Summary

| # | Mini Project | Chapter | Skills |
|---|---|---|---|
| 1 | Bill Splitter + Tip Calculator | 3 | input, operators, f-strings |
| 2 | Number Guessing Game | 6 | loops, conditions, random |
| 3 | Student Grade Manager | 8 | dicts, lists, aggregation |
| 4 | Bank Account System | 13 | OOP, exceptions, JSON |
| 5 | Log File Analyzer | 15 | generators, regex, testing |
| 6 | Online Store Sales Analysis | 18 | Pandas, groupby, merge |
| 7 | Student Performance Stats Report | 21 | statistics, Seaborn |
| 8 | House Price Prediction | 22 | Scikit-learn, pipelines |
| ★ | PakMart Capstone | 23 | end-to-end workflow |

**Exercises:** Har chapter mein taqreeban 10 exercises (🟢 4 · 🟡 3 · 🔴 3), har aik ke saath hint aur mukammal solution. Print edition aur companion repo dono mein exercises aur solutions shamil.

---

## 5. Style Guide (Language + Code)

**Language:**
- Sirf Roman Urdu — Urdu script bilkul nahi
- Technical terms English mein: variable, function, loop, DataFrame, etc.
- Spelling consistency list (e.g. "hai/hain", "kyun", "zaroorat", "misaal", "ghalti", "tareeqa") — poori kitab mein aik hi spelling
- Teacher-jaisa lehja: "Ab dekhte hain…", "Yahan dhyan dein…"
- Literal tarjuma se parhez (e.g. "loop" ko "chakkar" nahi likhna)

**Code:**
- Python 3.12+, PEP 8, meaningful names
- Type hints Chapter 9 ke baad se
- Har code block standalone runnable
- Random data hamesha fixed seed ke saath (output reproducible)
- Datasets code se generate honge (koi external download dependency nahi) — Pakistani context: shehar, PKR, local naam
- Library versions `requirements.txt` mein pin honge (latest stable at time of writing)

**Visual design:**
- Code blocks monospace + light background, output blocks alag rang mein
- Boxes ke consistent icons (⚠ 💡 🌍 🟢🟡🔴)
- Charts print-friendly (grayscale mein bhi parhne layak)
- MIAVRO Systems branding: header/footer, chapter opener band

---

## 6. Quality Assurance Strategy

1. **Code execution testing:** Har code block extract karke Python 3.12 environment mein automatically run kiya jayega; actual output ko book mein likhe output se compare kiya jayega. Mismatch = fail.
2. **Version pinning:** Tamam libraries ke versions fix; deprecated APIs (e.g. purane Pandas methods) check kiye jayenge.
3. **Technical accuracy review:** Har chapter ka checklist — definitions sahi, edge cases mention, misconceptions sahi tor par correct kiye gaye.
4. **Syllabus coverage checklist:** Is blueprint ka har subtopic tick hoga; koi topic silently skip nahi.
5. **Language QA:** Urdu script ke liye automated check (Arabic Unicode range scan); spelling consistency list ke against review; awkward tarjume hatana.
6. **Beginner readability test:** Har chapter ko "zero knowledge reader" ki nazar se parhna — koi concept pehle istemal na ho jo baad mein samjhaya gaya ho (dependency order check).
7. **Exercise validation:** Har exercise ka solution run aur test; difficulty level sahi label.
8. **Page budget tracking:** Har chapter likhne ke baad actual page count record; ±1 page tolerance; overflow hone par compact formatting.
9. **English edition parity checklist:** Chapter numbering, examples, projects, exercises — dono editions mein same.
10. **Final proof pass:** Cross-references, page numbers, TOC, glossary terms, branding.

---

## 7. Production Workflow

1. Blueprint approval (yeh document)
2. Chapter-by-chapter writing (aik response mein aik chapter, ya bara chapter do hisson mein)
3. Har chapter ke baad: code test + QA checklist + aap ka review/approval
4. Har Part ke baad: consistency review
5. Appendices aur front matter aakhir mein
6. Final layout aur publication-ready export (PDF)

---

## 8. Approved Faislay (v1.1)

- Edition: print (hard copy) + companion GitHub repo, dono
- Language: Roman Urdu (sirf)
- Chapter 14 mein Git basics shamil (14.10)
- Zyada exercises: print aur repo dono mein (har chapter ~10, teen levels)
- Companion repo: https://github.com/CodeWithLiaqat/python-mastery-2
- Page budget: zyada exercises aur solutions ki wajah se asal pages 100 se zyada ho sakte hain; har chapter ke baad actual count track hoga

## 9. Pehle Ke Sawalat (v1.0)

1. **Page size/density:** A4 ya B5 (6.9×9.8 in)? 100 pages mein poora syllabus dense layout maangta hai — A4 recommended.
2. **Exercise solutions:** Appendix D (4 pages) mein selected detailed solutions + poore solutions companion GitHub repo/MIAVRO website par — kya yeh theek hai?
3. **Coding environment:** Main tool VS Code (Part 1–4) + Jupyter/Colab (Part 5) — approve?
4. **Capstone domain:** "PakMart" e-commerce data — ya koi aur context (e.g. cricket, banking, real estate)?
