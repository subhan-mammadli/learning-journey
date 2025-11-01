# 🧪 CS50P Lecture 5 — Unit Tests

## 📘 Introduction

When writing programs, manually checking if your code works can be time-consuming.  
To make this easier, we use **automated testing**, which helps us verify that our functions behave correctly every time they run.

In Python, the main tools are:

- The `assert` keyword
    
- The `pytest` testing framework
    
- Organizing tests using **packages**
    

---

## ⚙️ The `assert` Keyword

The `assert` keyword is used to **state that a condition must be true**.  
If the condition is false, Python raises an `AssertionError` and stops the program.

### 🔹 Basic Example

```python
def main():
    n = int(input("n: "))
    print(square(n))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
```

We can test the `square` function like this:

```python
assert square(2) == 4
assert square(3) == 9
```

If any assertion fails:

```
AssertionError
```

---

## ⚠️ AssertionError and try-except

When an assertion fails, the program stops.  
We can catch this error with a `try-except` block:

```python
try:
    assert square(3) == 9
except AssertionError:
    print("3 squared was not 9")
```

This lets the program continue running, even after a failed test.  
But for large projects, this is inefficient — so we use `pytest`.

---

## 🧰 Pytest — A Testing Framework

`pytest` is a powerful tool for writing **unit tests**, which check that individual functions behave correctly.

### 🔹 Installation

```bash
pip install pytest
```

### 🔹 Example Project

`calculator.py`:

```python
def square(n):
    return n * n
```

`test_calculator.py`:

```python
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0
```

### 🔹 Run Tests

```bash
pytest test_calculator.py
```

If all tests pass:

```
....
```

If one fails, pytest shows:

```
..F.
>       assert square(-3) == 9
E       AssertionError: assert 6 == 9
```

---

## 🧩 Test File Naming

Pytest automatically detects files named:

```
test_*.py
*_test.py
```

So a clean structure looks like:

```
calculator.py
test_calculator.py
```

---

## 📦 Python Packages

If a directory contains `__init__.py`, Python treats it as a **package**.

Example:

```
maths/
├── __init__.py
├── calculator.py
└── test_calculator.py
```

Run tests inside that package:

```bash
pytest maths/
```

---

## 🚨 Testing Expected Errors with `pytest.raises`

Sometimes we want to make sure a function raises an error for invalid input — for example, when the user enters the wrong type, invalid format, or impossible value.

Pytest can test this using `pytest.raises`.

### 🔹 Example

```python
import pytest
from calculator import square

def test_type_error():
    with pytest.raises(TypeError):
        square("hello")
```

✅ This test checks that passing a string to `square()` correctly raises a `TypeError`.

If the function does **not** raise a TypeError, the test fails.

### ✅ Why this matters

- Functions should not only return the correct result
    
- They must also handle **incorrect inputs safely**
    
- This is important for writing reliable, professional code
    

---

## 🧠 Tip: Running All Tests

Run all tests in the current directory:

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

---

## 🧪 Advanced Example

```python
from calculator import square
import pytest

def test_positive():
    assert square(2) == 4

def test_negative():
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_type():
    with pytest.raises(TypeError):
        square("cat")
```

---

## ✅ Summary

|Concept|Description|
|---|---|
|**assert**|Checks if a condition is true; otherwise raises `AssertionError`.|
|**try-except**|Prevents the program from crashing when an assertion fails.|
|**pytest**|Framework for running automated tests.|
|**pytest.raises**|Used to test if a function raises the correct error.|
|`__init__.py`|Makes a folder a Python package.|
|`pytest test/`|Runs all tests inside the `test/` directory.|

---

## ✅ Conclusion

In this lecture, you learned how to:

- Use `assert` to test code quickly
    
- Catch failed assertions with `try-except`
    
- Write unit tests with `pytest`
    
- Use `pytest.raises` to verify error handling
    
- Organize your project into packages for cleaner structure
    