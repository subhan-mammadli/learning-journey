# 🏦 Back to the Bank — CS50P Problem Set 5

## 📘 Problem Description

In this problem, you return to **Home Federal Savings Bank** from Problem Set 1, but restructure your program to use proper function design and automated testing.

### ✅ In `bank.py`

You must:

* Implement a function `value(greeting)` that:

  * Returns **0** if the input starts with `"hello"`
  * Returns **20** if it starts with `"h"` (but not `"hello"`)
  * Returns **100** otherwise
* Treat the input **case-insensitively**
* Assume there are **no leading spaces**
* Only `main()` should print — **`value()` must return an int**, not print

Required structure:

```python
def main():
    ...

def value(greeting):
    ...

if __name__ == "__main__":
    main()
```

---

### ✅ In `test_bank.py`

You must write **three or more test functions** whose names begin with `test_`, so they can be executed using:

```bash
pytest test_bank.py
```

Your test file must import the function:

```python
import bank
# or
from bank import value
```

---

## 💡 My Explanation

This task asks us to rewrite the original Bank problem using **clean function structure** and then write **pytest tests** that confirm the logic works in all cases.

What I tested:

✅ Greetings that begin with `"hello"` → should return `0`
✅ Greetings that begin with `"h"` but not `"hello"` → should return `20`
✅ All other greetings → should return `100`

I also improved my original `bank.py` from Problem Set 1 by making the logic cleaner and case-insensitive using `.lower()` and `.startswith()`.

---

## 🧩 Code Implementation

📄 Main Program: **[`bank.py`](./bank.py)**
📄 Tests: **[`test_bank.py`](./test_bank.py)**

---

## 🧪 Example Tests

* `"Hello"` → `0`
* `"Hello, Newman"` → `0`
* `"How you doing?"` → `20`
* `"What's happening?"` → `100`

Run tests with:

```bash
pytest test_bank.py
```

---

## 🧠 Key Concepts Learned

* Converting code into reusable **functions**
* Returning values instead of printing
* Using `.lower()` and `.startswith()` for case-insensitive logic
* Writing automated tests with **pytest**
* Using multiple test functions to check many input types
