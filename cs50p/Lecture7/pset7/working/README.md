# 🕒 Working 9 to 5

**CS50P – Problem Set 7**

In this exercise, the goal is to convert **12-hour formatted time ranges** into **24-hour (military) time**.

While many countries use the 24-hour clock, the United States commonly formats time like:

```
9:00 AM to 5:00 PM
```

Your task is to translate that format into:

```
09:00 to 17:00
```

---

## ✅ Goal

Implement a function `convert` inside `working.py` that:

✔ Accepts a string in any valid 12-hour format below
✔ Returns the time converted to 24-hour format
✔ Raises `ValueError` for invalid input

Supported formats:

| Input                  | Output           |
| ---------------------- | ---------------- |
| `"9 AM to 5 PM"`       | `09:00 to 17:00` |
| `"9:00 AM to 5:00 PM"` | `09:00 to 17:00` |
| `"9 AM to 5:00 PM"`    | `09:00 to 17:00` |
| `"9:00 AM to 5 PM"`    | `09:00 to 17:00` |

> 🔗 See implementation here:
> 📄 [`working.py`](./working.py)

---

## ✅ Valid Time Rules

| 12-hour input        | Valid?                  |
| -------------------- | ----------------------- |
| `1:00 AM`            | ✅                       |
| `12:00 AM` → `00:00` | ✅                       |
| `12:59 PM` → `12:59` | ✅                       |
| `13:00 PM`           | ❌ hour must be 1–12     |
| `12:60 AM`           | ❌ minutes must be 00–59 |

The function must **not assume** that AM comes before PM—someone could work overnight:

```
5:00 PM to 9:00 AM   ✅ valid
```

---

## ✅ Regex Logic (Explained Clearly)

To verify that the input matches one of the valid formats, a regular expression is used.
A commonly used pattern in this problem looks like:

```
r'((?:[1-9]|1[0-2])(?::[0-5]\d)? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::[0-5]\d)? (?:AM|PM))'
```

### Pattern Breakdown

| Part            | Meaning                              |                      |
| --------------- | ------------------------------------ | -------------------- |
| `[1-9]          | 1[0-2]`                              | Hour is 1–9 or 10–12 |
| `(?::[0-5]\d)?` | Optional minute section, `:00`–`:59` |                      |
| `(AM            | PM)`                                 | Must be capitalized  |
| `to`            | Literal word between times           |                      |

If the string does **not** match this pattern → raise `ValueError`.

If it **does** match:

1. Extract both times (start and end)
2. Convert each from 12-hour format to 24-hour format
3. Rebuild the output in `"HH:MM to HH:MM"` format

### AM / PM Conversion Rules

| 12-hour              | 24-hour |
| -------------------- | ------- |
| `1:00 AM` → `01:00`  |         |
| `12:00 AM` → `00:00` |         |
| `12:00 PM` → `12:00` |         |
| `1:00 PM` → `13:00`  |         |
| `11:59 PM` → `23:59` |         |

Leading zeroes are required, which Python formats with:

```python
f"{hour:02}"
```

---

## ✅ Testing

Create `test_working.py` with at least **three test functions** that thoroughly check:

✅ Valid input formats
✅ Edge cases (midnight/noon conversions)
✅ Overnight shifts
✅ Inputs that should raise `ValueError`

> 🔗 Example test file:
> 📄 [`test_working.py`](./test_working.py)

Run tests using:

```
pytest test_working.py
```

---

## ✅ What This Problem Teaches

* Parsing structured text using regex
* Capturing groups and extracting matched values
* Validating input formats and raising errors correctly
* Converting between time systems
* Using `pytest` to automate testing
