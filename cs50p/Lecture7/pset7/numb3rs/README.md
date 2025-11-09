# 🔢 NUMB3RS — IPv4 Validator

**CS50P – Problem Set 7**

In this exercise, we revisit a scene from the TV show **NUMB3RS**, where an on-screen “IP address” appears as:

```
275.3.6.28
```

The problem?
✅ It **looks** like an IPv4 address
❌ But `275` is not a valid octet

---

## ✅ Goal

Write a program that **validates IPv4 addresses** using Python.

An IPv4 address:

* Has **4 numerical parts** (called *octets*)
* Is written as: `A.B.C.D`
* Each octet must be an integer **from 0 to 255**, inclusive

Examples:

| Address           | Valid?             |
| ----------------- | ------------------ |
| `192.168.0.1`     | ✅ Yes              |
| `255.255.255.255` | ✅ Yes              |
| `275.3.6.28`      | ❌ No (`275` > 255) |
| `cat`             | ❌ Not an IP        |

---

## ✅ Requirements

Create a file called **`numb3rs.py`** containing a function:

```python
validate(ip: str) -> bool
```

* Returns `True` if `ip` is a valid IPv4 address
* Returns `False` otherwise
* You may use `re` (recommended), but no external libraries

The program’s `main()` should print the result of calling `validate()` on user input.

> 🔗 See the implementation:
> 📄 [`numb3rs.py`](./numb3rs.py)

---

## ✅ Regular Expression Logic (Explained)

To validate an IPv4 address cleanly, Regex is a powerful tool.
A common pattern used in this exercise looks like:

```
r"^(25[0-5]|2[0-4]\d|1?\d{1,2})(\.(25[0-5]|2[0-4]\d|1?\d{1,2})){3}$"
```

### Breakdown

| Part        | Meaning                                                           |
| ----------- | ----------------------------------------------------------------- |
| `^`         | Start of string                                                   |
| `$`         | End of string                                                     |
| `25[0-5]`   | Matches `250–255`                                                 |
| `2[0-4]\d`  | Matches `200–249`                                                 |
| `1?\d{1,2}` | Matches `0–199` (`1` optional, 1–2 digits allowed)                |
| `\.`        | Literal dot                                                       |
| `{3}`       | Repeat the dot-octet pattern **3 more times** (total of 4 octets) |

Why `{3}` and not `{4}`?
✅ The first octet is matched before the group
✅ The next three must start with a dot

Example structure:

```
 A   .   B   .   C   .   D
[octet][.octet][.octet][.octet]
         ^ repeated 3 times
```

If the whole pattern matches from start to end, the IP is valid.

---

## ✅ Testing the Validator

Create a second file:

📄 **`test_numb3rs.py`**

Write **two or more** test functions using `pytest`.
Each should begin with `test_` and thoroughly check both valid and invalid addresses.

Suggested test areas:

✅ Valid IPv4 formats
✅ Out-of-range numbers (`512.2.3.4`)
✅ Non-numeric input (`cat`)
✅ Too few or too many octets
✅ Leading zeros that shouldn’t be valid (`192.168.001.1`)

> 🔗 See example tests:
> 📄 [`test_numb3rs.py`](./test_numb3rs.py)

Run tests:

```
pytest test_numb3rs.py
```

---

## ✅ What This Problem Teaches

* Understanding IPv4 structure
* Using **regular expressions** for pattern validation
* Working with:

  * `re.search`
  * Raw strings (`r""`)
  * Grouping and repetition
* Writing unit tests with **pytest**
* Ensuring your program handles valid and invalid user input cleanly