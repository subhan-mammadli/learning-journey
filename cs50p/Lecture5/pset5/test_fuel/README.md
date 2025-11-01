# ⛽ Refueling — CS50P Problem Set 5

## 📘 Problem Description

This task revisits **Fuel Gauge** from Problem Set 3, but now the program must be properly structured into functions **and** tested using `pytest`.

### ✅ In `fuel.py`

You must implement:

* **`convert(fraction)`**

  * Accepts a string in `X/Y` format
  * Converts it to a percentage (`0–100`, rounded to nearest integer)
  * Raises **ValueError** if:

    * X or Y is not an integer
    * X is greater than Y
  * Raises **ZeroDivisionError** if Y is `0`
  * Returns an **int**, not a string

* **`gauge(percentage)`**

  * Accepts an **int**
  * Returns:

    * `"E"` if ≤ 1
    * `"F"` if ≥ 99
    * Otherwise `"Z%"`, where Z is the percentage

Required structure:

```python
def main():
    ...

def convert(fraction):
    ...

def gauge(percentage):
    ...

if __name__ == "__main__":
    main()
```

---

### ✅ In `test_fuel.py`

Write **two or more** test functions starting with `test_`, and run them using:

```bash
pytest test_fuel.py
```

Test both:

✅ Valid conversions
✅ Errors using `pytest.raises` for `ValueError` and `ZeroDivisionError`
✅ Outputs of `gauge()`

Import the functions like:

```python
from fuel import convert, gauge
```

---

## 💡 My Explanation

This problem is about **refactoring** and **testing**.

What I changed:

* Split the original logic into reusable functions
* `convert()` handles math and exceptions
* `gauge()` turns the percentage into `"E"`, `"F"`, or `"Z%"`

In `test_fuel.py`:

* I tested correct values using `assert`
* I tested incorrect input using `pytest.raises`, confirming correct exceptions
* I tested edge cases like `"1/100" → 1` becomes `"E"` and `"99/100" → 99` becomes `"F"`

---

## 🧩 Code Implementation

📄 Main Program: **[`fuel.py`](./fuel.py)**
📄 Tests: **[`test_fuel.py`](./test_fuel.py)**

---

## 🧪 Example Tests Performed

✅ `"3/4"` → `75`
✅ `"1/100"` → `1`
✅ `"99/100"` → `99`
✅ Invalid strings → `ValueError`
✅ Denominator `0` → `ZeroDivisionError`
✅ `gauge(1)` → `"E"`
✅ `gauge(99)` → `"F"`
✅ `gauge(50)` → `"50%"`

Run tests with:

```bash
pytest test_fuel.py
```

---

## 🧠 Key Concepts Learned

✔ Raising and handling exceptions properly
✔ Using `pytest` to test both valid output and expected errors
✔ Returning values instead of printing
✔ Clean function structure with `main()` and helpers
✔ Edge-case testing and robustness
