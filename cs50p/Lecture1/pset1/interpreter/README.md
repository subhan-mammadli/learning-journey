# ➗ Problem Set 1 – Math Interpreter

## 🧠 Problem Description

In this problem, you’re asked to implement a simple **math interpreter** — a program that can evaluate a basic arithmetic expression entered by the user.

The user will input a mathematical expression in the form:

```
x y z
```

where:

* `x` and `z` are numbers
* `y` is an operator (`+`, `-`, `*`, `/`)

Your program should parse the expression and output the **calculated result**.

---

## ⚙️ Implementation Details

1. **Get input** from the user:

   ```python
   expression = input("Expression: ")
   ```
2. **Split** the input into three parts using `.split(' ')`:

   ```python
   x, y, z = expression.split(' ')
   ```
3. **Convert** `x` and `z` into floating-point numbers for decimal precision:

   ```python
   x = float(x)
   z = float(z)
   ```
4. **Use `match-case`** (Python 3.10+) to handle each operator:

   ```python
   match y:
       case "+":
           print(x + z)
       case "-":
           print(x - z)
       case "*":
           print(x * z)
       case "/":
           print(x / z)
   ```

---

## 💻 Solution

👉 Full implementation:
[`interpreter.py`](./interpreter.py)

---

## 🧩 Example Runs

```
$ python interpreter.py
Expression: 2 + 3
5.0
```

```
$ python interpreter.py
Expression: 10 / 4
2.5
```

```
$ python interpreter.py
Expression: 7 * 8
56.0
```

---

## 🧩 Key Concepts

| Concept      | Description                                                                              |
| ------------ | ---------------------------------------------------------------------------------------- |
| `.split()`   | Splits a string into parts based on a separator (space `" "` in this case).              |
| `float()`    | Converts string input into a floating-point number.                                      |
| `match-case` | Simplifies conditional branching based on a single variable (introduced in Python 3.10). |

---

## 💡 Notes

* This problem reinforces **string parsing**, **data type conversion**, and **control flow** using `match-case`.
* Using `float()` allows handling of both integers and decimals.
* Each case directly performs the arithmetic operation and prints the result.

