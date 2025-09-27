# 📘 CS50p Lecture 0 Notes

## 🖥️ Running Code

```bash
code hello.py   # open/create hello.py in VS Code
python hello.py # run hello.py
```

---

## 🖨️ The `print` Function

```python
print("Hello, world", end="!")
```

* By default, `print` ends with **`\n` (a newline)**.
* This is the same as `end="\n"`.
* You can change `end` to control what appears at the end of the line.

```python
print("Hello", "world", sep=",")
```

* By default, `print` separates multiple arguments with a space (`sep=" "`).
* You can change `sep` to any custom separator.

---

## 📝 Strings and Methods

### Quotation Marks

```python
print("Hello, \"Writer\"")
```

* Use `\` (escape character) to include quotes inside a string.

### Useful Methods

```python
name = "   subhan   mammadli   "
name = name.strip().capitalize()
print(name)  # Subhan mammadli
```

* `.strip()` → removes extra whitespace
* `.capitalize()` → capitalizes the first letter only
* `.title()` → capitalizes the first letter of *every* word

```python
name = "Subhan Mammadli"
firstname, lastname = name.split(" ")
print(firstname)  # Subhan
print(lastname)   # Mammadli
```

* `.split(" ")` → splits a string at spaces (or another character)

### f-Strings

```python
print(f"Hello, {name}")
```

* Allows embedding variables directly inside strings.

---

## 🔢 Numbers and Types

### Integers (`int`)

* Whole numbers: `3, -3, 0`
* Operators: `+ - * / %`
* `%` gives the remainder: `5 % 2 = 1`

```python
number = "1"
int(number)  # string → int
```

### Floats (`float`)

* Decimal numbers: `3.2, -4.5`

```python
float(3)  # int → float
```

### The `round()` Function

```python
round(22.5678)     # 23
round(22.52, 1)    # 22.5
```

* Without a second argument → rounds to the nearest integer.
* With a second argument → rounds to a specific number of decimal places.

---

## 📊 Number Formatting

```python
z = 1000
print(f"{z:,}")     # 1,000
```

* Formats numbers with commas as thousands separators.

```python
z = 0.6789
print(f"{z:.2f}")   # 0.68
```

* Formats numbers with a fixed number of decimal places.

---

## 🛠️ Functions

```python
def hello(to):
    print("hello,", to)

hello("Subhan")
```

* `def` defines a function.
* `to` is an argument.
* If no argument is provided, it raises an error.
* We can use default values:

```python
def hello(to="world"):
    print("hello,", to)
```

### Calling Before Defining

If you call a function **before** defining it, Python raises an error.
To avoid this, we can wrap the main code in a `main()` function:

```python
def main():
    hello()

def hello():
    print("hello, world")

main()
```

---

## 🔄 The `return` Statement

```python
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
```

* `return` sends the result (output) of a function back to the caller.

---

✨ These notes summarize the key concepts from **Lecture 0**:

* print and string formatting
* integers & floats
* rounding and number formatting
* functions and return values