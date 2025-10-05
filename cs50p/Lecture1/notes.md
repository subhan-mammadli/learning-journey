# 🧠 CS50P – Lecture 1: Conditionals

## 📘 Overview

In this lecture, we learn about **conditionals** — statements that allow a program to make decisions based on data.
Using `if`, `elif`, `else`, and `match-case`, we can control the **flow of execution** depending on whether certain conditions are true or false.

We’ll also review **comparison operators**, **logical operators**, and the **boolean data type** (`True` / `False`).

---

## ⚖️ Comparison Operators

| Operator | Meaning                  | Description                      |
| -------- | ------------------------ | -------------------------------- |
| `==`     | equal to                 | True if both sides are equal     |
| `!=`     | not equal to             | True if both sides are not equal |
| `>`      | greater than             | True if left side is greater     |
| `<`      | less than                | True if left side is smaller     |
| `>=`     | greater than or equal to | True if left side ≥ right side   |
| `<=`     | less than or equal to    | True if left side ≤ right side   |

**Example:**

```python
x = 5
y = 3

if x > y:
    print("x is greater than y")
```

Here, `x > y` is a **condition** that returns either `True` or `False`.
If it’s `True`, the code inside the `if` block runs.

---

## 🔀 Conditional Statements (`if`, `elif`, `else`)

Conditional expressions in Python follow this structure:

```python
if condition:
    # Executes if the condition is True
elif another_condition:
    # Executes if the previous condition was False and this one is True
else:
    # Executes if all previous conditions are False
```

**Example:**

```python
x = int(input("x: "))
y = int(input("y: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} is equal to {y}")
```

---

## 🔣 Logical Operators

| Operator | Meaning | Description                                   |
| -------- | ------- | --------------------------------------------- |
| `and`    | and     | True only if **both** conditions are True     |
| `or`     | or      | True if **at least one** condition is True    |
| `not`    | not     | Inverts the value: True → False, False → True |

**Example:**

```python
x = int(input("x: "))
y = int(input("y: "))

if x > y or x < y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")
```

---

## 🧾 Example: `grade.py`

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

### More Pythonic alternatives:

```python
if 90 <= score <= 100:
    print("Grade: A")
```

This chained comparison is cleaner and easier to read.

> 💡 Use `elif` to prevent multiple conditions from being executed at once.

**Incorrect version:**

```python
if score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
```

If `score = 95`, both `if` blocks will execute:

```
Grade: A
Grade: B
```

---

## ➕ Arithmetic Operators

| Operator | Meaning             |
| -------- | ------------------- |
| `+`      | addition            |
| `-`      | subtraction         |
| `*`      | multiplication      |
| `/`      | division            |
| `%`      | modulus (remainder) |

**Example:**

```python
n = 10

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
```

---

## 🧩 Boolean (Bool) Values

A **boolean** can only have one of two values: `True` or `False`.

### Example: `parity.py`

```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
```

Simplified version:

```python
def is_even(n):
    return n % 2 == 0
```

> 💡 `return n % 2 == 0` directly returns `True` or `False`.

---

## 🏰 `match-case` (Python 3.10+)

The `match-case` statement is similar to `switch` in other languages.
It makes your code cleaner when comparing a single value against many options.

**Example:**

```python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

> `_` acts as a default case — similar to `else`.

---

## 🧩 Summary

In this lecture, we learned:

* How to use `if`, `elif`, and `else` to check conditions
* The meaning and use of **comparison** and **logical** operators
* How **boolean** values (`True` / `False`) control program flow
* How to simplify code with **chained comparisons** and **match-case**
* How conditionals make programs respond dynamically to user input