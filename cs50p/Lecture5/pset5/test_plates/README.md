# 🚘 Re-requesting a Vanity Plate — CS50P Problem Set 5

## 📘 Problem Description

In this task, you return to **Vanity Plates** from Problem Set 2 and rewrite the program using proper function structure and automated testing.

### ✅ In `plates.py`

You must:

* Implement `is_valid(s)` which:

  * Returns **True** if a plate meets *all* requirements
  * Returns **False** otherwise
* Requirements to enforce:
  ✅ Must start with at least **two letters**
  ✅ Length must be **between 2 and 6 characters**
  ✅ Numbers (if present) must come **only at the end**
  ✅ First number cannot be **0**
  ✅ No punctuation — only **letters and numbers**
* `main()` should handle user input and printing
* `is_valid()` must **return**, not print

Required structure:

```python
def main():
    ...

def is_valid(s):
    ...

if __name__ == "__main__":
    main()
```

---

### ✅ In `test_plates.py`

You must write **four or more** test functions whose names begin with `test_`, so you can run:

```bash
pytest test_plates.py
```

Your test file must import the function:

```python
import plates
# or
from plates import is_valid
```

---

## 💡 My Explanation

This problem asks us to take the original Vanity Plates logic and properly structure it for **unit testing**.

* I kept all validation rules from the original assignment
* `is_valid()` checks each rule separately:

  * start with two letters
  * correct length
  * numbers only at the end
  * no punctuation
  * first number cannot be zero
* Then I wrote multiple `test_` functions using `assert` to verify every rule

This allowed me to catch edge cases and improve my original logic.

---

## 🧩 Code Implementation

📄 Main Program: **[`plates.py`](./plates.py)**
📄 Tests: **[`test_plates.py`](./test_plates.py)**

---

## 🧪 Example Tests Performed

* ✅ Valid plates: `"CS50"`, `"HELLO"`, `"PI314"`
* ❌ Invalid:

  * starting with digits
  * punctuation or symbols (`"CS50!"`, `"PI3.14"`)
  * letters after numbers (`"CS50P"`)
  * first number being zero (`"CS05"`, `"AB012"`)

Run all tests with:

```bash
pytest test_plates.py
```

---

## 🧠 Key Concepts Learned

✔ Designing functions that return results instead of printing
✔ Re-using old problem logic with better structure
✔ Writing multiple automated tests with **pytest**
✔ Validating strings: `.isalpha()`, `.isdigit()`, `.isalnum()`, `.startswith()`
✔ Handling rule-based input validation cleanly
