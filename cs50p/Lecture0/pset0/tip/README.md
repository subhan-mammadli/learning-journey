# 💰 Tip Calculator (CS50P Problem Set)

This project is part of the **CS50’s Introduction to Programming with Python** course.
The goal is to implement a simple **tip calculator** that helps users decide how much tip to leave based on the meal cost and desired tip percentage.

---

## 📌 Problem Description

CS50 provides us with the following starter code:

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

The logic of the program is already written, but the two helper functions (`dollars_to_float` and `percent_to_float`) are left incomplete.
Our task is to **implement these functions**.

---

## 🛠️ Implementation Details

### `dollars_to_float(d)`

* Removes the **`$`** sign from the user’s input.
* Converts the result into a floating-point number.
* Example: `"$15.00"` → `15.0`.

### `percent_to_float(p)`

* Removes the **`%`** sign from the user’s input.
* Converts the result into a floating-point number and divides it by 100.
* Example: `"15%"` → `0.15`.

---

## ✅ Solution

The full solution can be found here:
➡️ [tip.py](./tip.py)

---

## 🎯 Example Run

```
How much was the meal? $50.00
What percentage would you like to tip? 20%
Leave $10.00
```

---

## 📚 What I Learned

* String cleaning and conversion in Python.
* Converting percentages into decimal values.
* Formatting floats as currency with `:.2f`.
