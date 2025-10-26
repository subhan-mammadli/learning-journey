# 🧠 CS50p Lecture 4 — Libraries

## 📦 The `random` Library

The `random` module allows you to make random selections, generate random numbers, or shuffle lists in Python.

### 🔹 import

To import the entire library:

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

`random.choice(seq)` → returns a random element from the given sequence (like a list).

---

### 🔹 from

To import only specific functions from a module:

```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

When using `from`, you don’t need to write the module name — you can call the function directly.

---

### 🎲 `random.randint(a, b)`

Returns a random **integer** between `a` and `b` (inclusive).

```python
import random

number = random.randint(1, 10)
print(number)  # Random integer between 1 and 10
```

---

### 🔀 `random.shuffle(x)`

Takes a list and shuffles its elements in place (changes their order randomly).

```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)
```

---

## 📊 The `statistics` Library

The `statistics` module provides functions to perform common mathematical and statistical operations such as mean, median, and mode.

```python
import statistics

print(statistics.mean([100, 90]))  # 95.0
```

### Key Functions

* `statistics.mean(data)` → arithmetic mean
* `statistics.median(data)` → median value
* `statistics.mode(data)` → most frequent value
* `statistics.stdev(data)` → standard deviation

---

## 💻 Command-Line Arguments

When you run a Python program, you can pass **arguments** to it from the terminal.

```bash
python hello.py David
```

These arguments can be accessed from within your program.

---

### 🧩 The `sys` Library

The `sys` module provides access to system-level operations and the command-line arguments used to run a Python script.

#### sys.argv

`sys.argv` is a list that stores all the command-line arguments passed to the program.

```python
import sys

print("Hello, my name is", sys.argv[1])
```

```bash
python name.py David
# Output: Hello, my name is David
```

#### ⚠️ Note:

If you don’t provide an argument, you’ll get:

```
IndexError: list index out of range
```

`sys.argv[0]` always contains the script’s filename (e.g., `name.py`).

---

### ⚙️ Error Handling Example

```python
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
```

If your argument contains spaces, enclose it in quotes:

```bash
python name.py "David Malan"
```

---

### 🔚 `sys.exit()`

Stops program execution. You can optionally provide an exit message.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
```

---

## ✂️ Slicing with `sys.argv`

Since `sys.argv` is a list, you can use slicing to access specific parts of it.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
```

* `sys.argv[1:]` → all arguments except the first
* `sys.argv[1:-1]` → from the second argument up to (but not including) the last one

---

## 📦 Packages and `pip`

### 🔹 PyPI (Python Package Index)

A central repository of Python libraries:
👉 [https://pypi.org](https://pypi.org)

### 🔹 pip

A package manager used to install external libraries.

```bash
pip install cowsay
```

---

### 🐮 Example: `cowsay`

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello " + sys.argv[1])
```

---

## 🌐 APIs, Requests, and JSON

### 🔹 The `requests` Library

Allows you to send **HTTP/HTTPS requests** (like a browser) and retrieve data from APIs.

Install:

```bash
pip install requests
```

Example:

```python
import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python songs.py [artist]")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
```

---

### 🔹 JSON (JavaScript Object Notation)

JSON is a lightweight, language-independent format for data exchange.
Python can convert JSON into dictionaries for easy access.

```python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
data = response.json()

for result in data["results"]:
    print(result["trackName"])
```

---

## 🧩 Creating Your Own Module

### sayings.py

```python
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":
    main()
```

### say.py

```python
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
```

---

### 🧠 Explanation

* `if __name__ == "__main__":`
  Ensures that `main()` runs **only if** the file is executed directly.
  It will **not** run when the module is imported from another file.

---

## 🧾 Summary

| Topic                    | Description                                         |
| ------------------------ | --------------------------------------------------- |
| `random`                 | Random selection, number generation, list shuffling |
| `statistics`             | Mean, median, mode, standard deviation              |
| `sys.argv`               | Access command-line arguments                       |
| `sys.exit()`             | Exit a program gracefully                           |
| `pip`, `PyPI`            | Install and manage Python packages                  |
| `requests`, `json`       | Fetch and parse web API data                        |
| `__name__ == "__main__"` | Control script execution behavior                   |