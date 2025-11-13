# 🍪 Problem Set 8 — Cookie Jar

This directory contains my solution to **CS50P’s “Cookie Jar” problem**, in which the task is to design, implement, and test a class that simulates a simple cookie jar capable of storing cookies up to a fixed capacity.

The implementation is found in **[`jar.py`](./jar.py)**, and the tests are located in **[`test_jar.py`](./test_jar.py)**.

---

# 📘 Problem Description

The goal of this assignment is to create a fully functional `Jar` class that behaves like a real cookie jar:

* It has a **capacity** (maximum number of cookies it can hold).
* It keeps track of the current number of cookies.
* It allows depositing and withdrawing cookies with proper validation.
* It returns a **string representation** visualized with cookie emojis (`🍪`).
* It should raise `ValueError` for invalid operations.

A test suite verifies that the class behaves correctly under normal and erroneous conditions.

You must structure your class exactly as shown in the problem specification, keeping the method signatures unchanged.

---

# 🧠 How the Solution Works

Below is a detailed explanation of the logic, design decisions, and Python concepts used in the implementation.
These notes expand and correct your original explanation.

---

## 🏗️ 1. Class Structure and Initialization

The class begins with:

```python
class Jar:
    def __init__(self, capacity=12):
        ...
```

### Capacity

The constructor receives a `capacity` argument with a default of **12**.

A valid capacity must be:

* an integer
* non-negative

If not, the constructor must raise `ValueError`.

### Internal State

The cookie count is stored in a private attribute:

* `_cookie` → tracks how many cookies are currently inside the jar
* `_capacity` → tracks the maximum allowed number of cookies

These values are intentionally **encapsulated** and accessed only through getters and setters.

---

## 🔒 2. Encapsulation via Properties

The class protects its internal state using **getter** and **setter** methods via the `@property` decorator.

### `capacity` property

* The getter returns the jar’s maximum capacity.
* The setter ensures:

  * Capacity cannot be negative
  * The jar cannot have more cookies than its capacity

If invalid, a `ValueError` is raised.

### `size` property

* The getter returns the current number of cookies.
* The setter ensures that cookie count:

  * Cannot be negative
  * Cannot exceed capacity

Proper encapsulation ensures that the object **can never enter an invalid state**, even if an attribute is modified indirectly.

---

## 🍪 3. String Representation (`__str__`)

The `__str__` method must return:

* An empty string if the jar is empty
* A string containing **n cookie emojis (`🍪`)** where `n` is the current number of cookies

For example:

| Size | Output     |
| ---- | ---------- |
| 0    | `""`       |
| 1    | `"🍪"`     |
| 3    | `"🍪🍪🍪"` |

This representation makes inspecting the object intuitive and aligns with the problem’s playful theme.

---

## ➕ 4. Depositing Cookies

The `deposit(n)` method:

* Adds `n` cookies to the jar
* Validates that adding these cookies will **not exceed capacity**
* Raises `ValueError` if the jar would overflow

Otherwise, the cookies are successfully deposited.

---

## ➖ 5. Withdrawing Cookies

The `withdraw(n)` method:

* Removes `n` cookies from the jar
* Ensures that you **cannot withdraw more cookies than available**
* Raises `ValueError` if there are not enough cookies

If valid, the method updates the cookie count accordingly.

---

# 🧪 Test Suite Overview

All tests are implemented in **[`test_jar.py`](./test_jar.py)**.

The test suite ensures the correctness of the class by covering:

---

## ✔️ 1. `test_init()`

Checks:

* Default capacity is set correctly
* Initial cookie count is zero
* Invalid capacities raise `ValueError`
* The jar cannot start or be set to an invalid state

---

## ✔️ 2. `test_str()`

Verifies that:

* The string representation is correct at every stage
* Depositing cookies changes the string output properly

---

## ✔️ 3. `test_deposit()`

Ensures:

* Valid deposits succeed
* Depositing above capacity raises `ValueError`

---

## ✔️ 4. `test_withdraw()`

Ensures:

* Withdrawing cookies works only if enough cookies are available
* Attempting to withdraw too many cookies raises `ValueError`

The tests exercise the class thoroughly and confirm that both normal operations and invalid operations behave as expected.

---

# 🗂️ File Overview

```
.
├── jar.py
└── test_jar.py
```

* **[`jar.py`](./jar.py)** → The full implementation of the `Jar` class
* **[`test_jar.py`](./test_jar.py)** → Automated tests using `pytest`

---

# ▶️ Usage

To run the tests:

```bash
pytest test_jar.py
```

To experiment interactively:

```python
from jar import Jar

jar = Jar()
jar.deposit(5)
print(jar)  # 🍪🍪🍪🍪🍪
```

---

# 🎯 Summary

In this problem, you learn how to:

✔ Design a Python class with encapsulated state
✔ Implement input validation using exceptions
✔ Use `@property` for safe attribute access
✔ Override `__str__` for meaningful object display
✔ Manage object state through methods (`deposit`, `withdraw`)
✔ Write comprehensive unit tests for class-based code

The Cookie Jar problem introduces essential OOP techniques used in real-world Python development, all while keeping the task simple and fun.