# 📘 CS50P — Lecture 9: Et Cetera (Advanced Python Tools)

This lecture introduces powerful Python features that improve readability, efficiency, and code design. Many of these are core to writing **"Pythonic"** code. This guide provides detailed explanations and examples for each concept so learners can understand both the **what** and the **why**.

---

## 🧩 1. Set

A `set` is a **collection of unique elements**. Unlike lists, **sets automatically discard duplicates**.

### 📌 Syntax

```python
houses = set()
houses.add("Gryffindor")
houses.add("Gryffindor")  # Duplicate will be ignored
print(houses)
```

### 🔁 Practical Example

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
```

### ✅ Output

```
Gryffindor
Ravenclaw
Slytherin
```

> ✅ **Why use a set?**
> 
> - To eliminate duplicates automatically
>     
> - To perform fast membership tests (`"Gryffindor" in houses`)
>     

---

## 🌐 2. Global Variables

Variables declared outside of functions are **global**. You can read them from anywhere, but **you can only modify them inside a function using `global` keyword**.

### 🧪 Example

```python
balance = 0

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

main()
```

> ⚠️ If you use a variable inside a function with the same name as a global one **without `global`**, it creates a new **local variable** that shadows the global one.

### 👇 Shadowing Example

```python
x = 10

def shadow():
    x = 5  # Local
    print("Inside:", x)

shadow()
print("Outside:", x)
```

---

## 🔒 3. Constants (Convention)

Python has no native constant type, but by convention, **constants are written in UPPERCASE**.

```python
MEOWS = 3
for _ in range(MEOWS):
    print("meow")
```

> 💡 Constants help express intent. If something shouldn’t change, name it like a constant.

---

## ✍️ 4. Type Hints

**Type hints** make it clear what type of data a function or variable expects. This helps with:

- Catching bugs early
    
- Better editor support
    
- Static analysis tools like `mypy`
    

### ❌ Problem Example

```python
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = input("Number: ")
meow(number)  # input() returns str, causes error
```

### ✅ Correct Version

```python
def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)
```

### ➕ Return Type Hint

```python
def meow(n: int) -> str:
    return "meow\n" * n
```

### ✅ Use `mypy` to check type correctness

```bash
pip install mypy
mypy main.py
```

> 🧠 Type hints are optional but highly recommended for larger projects.

---

## 📘 5. Docstrings

Docstrings are **official documentation strings** used to describe the purpose and usage of a function, class, or module.

```python
def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b
```

### 🛠 `help()` shows the docstring

```python
help(add)
```

|Comment (`#`)|Docstring (`"""`)|
|---|---|
|For inline notes|For official documentation|
|Ignored by Python|Used by IDEs and `help()`|

---

## 🛠️ 6. argparse

Command-line argument parser for building CLI tools.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
```

```bash
$ python meow.py -n 3
meow
meow
meow
```

---

## 📦 7. Unpacking (* and **)

### 🪄 List unpacking

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
print(total(*coins))  # Unpacks list
```

### 📦 Dictionary unpacking

```python
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins))  # Unpacks dictionary
```

---

## 🧩 8. *args and **kwargs

Used for functions that accept variable numbers of arguments.

```python
def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(100, 50, knuts=25)
```

> ✅ `*args` is a tuple of positional args  
> ✅ `**kwargs` is a dict of keyword args

---

## 🔁 9. map()

Applies a function to every element of an iterable.

```python
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

yell("this", "is", "cs50")
```

---

## 🧠 10. List Comprehensions

Pythonic way to build lists.

```python
words = [word.upper() for word in ["this", "is", "cs50"]]
print(words)
```

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [s["name"] for s in students if s["house"] == "Gryffindor"]
print(gryffindors)
```

---

## 🔍 11. filter()

Filters values from a list using a boolean-returning function.

```python
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
for s in gryffindors:
    print(s["name"])
```

---

## 🗺 12. Dictionary Comprehensions

```python
students = ["Harry", "Hermione", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
```

---

## 🔢 13. enumerate()

Adds an automatic index to items in a loop.

```python
students = ["Harry", "Hermione", "Ron"]
for i, student in enumerate(students, start=1):
    print(i, student)
```

---

## 🔄 14. Generators and `yield`

Generators allow you to iterate over data **without storing the whole result in memory**.

### 🧱 Normal version (memory expensive)

```python
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("\U0001F411" * i)
    return flock
```

### ✅ Generator version

```python
def sheep(n):
    for i in range(n):
        yield "\U0001F411" * i
```

```python
for s in sheep(5):
    print(s)
```

> ✅ Use `yield` for efficient streaming of large data.

---

## 🧾 Summary Table

|Concept|Key Idea|
|---|---|
|`set()`|Unique collection|
|`global`|Modify globals inside functions|
|Constants|Convention: uppercase names|
|Type Hints|Improve readability and tooling|
|Docstrings|Official function/class documentation|
|`argparse`|CLI argument parsing|
|`*args`, `**kwargs`|Flexible argument handling|
|`map()` / `filter()`|Functional iteration|
|Comprehensions|Compact list/dict generation|
|`enumerate()`|Loop with index|
|`yield`|Memory-efficient generators|

---

This concludes the lecture. These tools are essential for becoming a more fluent and professional Python programmer. Practice each one with small projects or scripts!

Happy coding! 🚀