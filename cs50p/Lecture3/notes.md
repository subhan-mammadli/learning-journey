# CS50P — Lecture 3: Exceptions

In this lecture, we learn how to handle **errors (exceptions)** in Python.  
The goal is to make programs **gracefully handle mistakes** instead of crashing.

---

## 🔹 SyntaxError

**Definition:**  
Occurs when there’s a grammatical mistake in your Python code — like missing parentheses or quotation marks.

```python
print("Hello, world)
```

➡️ Output:

```
SyntaxError: EOL while scanning string literal
```

**Explanation:**  
This happens _before_ the program runs — Python detects that the code’s syntax is invalid.

---

## 🔹 ValueError

**Definition:**  
Occurs when the data type is correct but the **value** is invalid for the operation.

Example:

```python
x = int(input("What's x? "))
print(f"x is {x}")
```

If the user types `cat`:

```
ValueError: invalid literal for int() with base 10: 'cat'
```

Because `"cat"` cannot be converted to an integer.

---

## 🔹 try / except

Used to handle errors so your program doesn’t crash.

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

🧠 **Explanation:**

- `try`: Python tries to run this block.
- `except`: If an error occurs, this block runs instead.
- The program continues running instead of stopping abruptly.

---

## 🔹 NameError

**Definition:**  
Occurs when you try to use a variable or name that hasn’t been defined.

```python
print(x)
```

Output:

```
NameError: name 'x' is not defined
```

---

## 🔹 else Block

Used together with `try` and `except`.  
If no error occurs in the `try` block, the `else` block runs.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

🧠 **Logic:**

- If an error occurs → `except` runs.
- If no error occurs → `else` runs.

---

## 🔹 Reprompting

Sometimes users enter invalid input.  
Instead of stopping the program, we can **keep asking** until valid input is provided.

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```

🧩 **Explanation:**

1. Prompts the user for a number.
2. If an error occurs, shows a message and asks again.
3. When input is valid, exits the loop and prints the value.

---

### Shorter Version

```python
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
```

If an exception occurs, Python skips `break` and executes the `except` block.

---

## 🔹 Turning It Into a Function

To reuse this logic, we can create a helper function:

```python
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
```

🧠 **Note:**  
`return` not only gives back the value — it also **automatically exits** the loop.

---

### Even Shorter Version

```python
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()
```

---

## 🔹 Using `pass`

If you don’t want to print an error message each time, use `pass` to silently skip the error.

```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
```

The program will simply re-ask the question without printing anything when input is invalid.

---

## 🔹 Adding a Prompt Parameter

We can make our function more flexible by adding a prompt argument:

```python
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
```

Now we can reuse it with different prompts:

```python
age = get_int("How old are you? ")
score = get_int("What is your score? ")
```

---

## 🧠 Summary

|Concept|Description|
|---|---|
|`SyntaxError`|Occurs when there’s an error in the code’s syntax.|
|`ValueError`|The data type is correct, but the value is invalid.|
|`NameError`|Variable or name hasn’t been defined.|
|`try`|Wraps code that might cause an error.|
|`except`|Runs when an error occurs.|
|`else`|Runs when **no error** occurs.|
|`while True` + `try/except`|Used to keep asking until valid input is entered.|
|`pass`|Ignores the error silently.|

---

## 💡 Extra Info

Other common exceptions in Python:

- **ZeroDivisionError:** Dividing by zero.
- **TypeError:** Performing invalid operations between incompatible types.
- **IndexError:** Accessing an out-of-range list index.
- **KeyError:** Accessing a dictionary key that doesn’t exist.

Example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```


