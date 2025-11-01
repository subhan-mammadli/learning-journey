# 🐦 Testing My Twttr — CS50P Problem Set 5

## 📘 Problem Description

In this problem, you revisit **“Setting up my twttr”** from Problem Set 2, but this time you must:

1. **Re-implement** the program in a file called `twttr.py`, using this required structure:

```python
def main():
    ...

def shorten(word):
    ...

if __name__ == "__main__":
    main()
```

* `shorten(word)` must accept a **str** and **return** that string with all vowels removed.
* It should remove **A, E, I, O, U** in both uppercase and lowercase.
* `shorten` must **return**, not print. Only `main` should print.

---

2. Write tests in a separate file, `test_twttr.py`, using **pytest**:

```bash
pytest test_twttr.py
```

* Test functions must start with `test_`
* Import the function using:

```python
import twttr
# or
from twttr import shorten
```

---

## 💡 My Explanation

This problem asks us to test our own function with **pytest**, not just write code.

### ✅ What I did

* Rewrote my original solution from Problem Set 2 inside `shorten()`
* Used vowel removal logic that works for both uppercase and lowercase
* Made sure `shorten()` **returns a string**, not prints it
* Wrote multiple test cases using `assert`:

  * lowercase words
  * uppercase words
  * mixed case
  * numbers and symbols (which should not change)

### ✅ Why this matters

Problem Set 5 introduces **unit testing**, which helps verify that our code works in all scenarios.
It also lets us **improve old solutions** and correct mistakes before submitting again.

---

## 🧩 Code Implementation

📄 Main program: **[`twttr.py`](./twttr.py)**
📄 Tests: **[`test_twttr.py`](./test_twttr.py)**

---

## 🧪 Example Tests Ran

The test file checks:

* `"twitter"` → `"twttr"`
* `"HELLO"` → `"HLL"`
* `"PyThOn"` → `"PyThn"`
* Non-letters like `"123"` or `"h@ppy!"` stay the same

To run tests:

```bash
pytest test_twttr.py
```

---

## 🧠 Key Concepts Learned

✅ Writing reusable functions
✅ Returning values instead of printing
✅ Running automated tests with **pytest**
✅ Using `assert` to check correctness
✅ Handling uppercase, lowercase, numbers, and symbols consistently
