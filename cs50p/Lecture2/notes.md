# CS50P – Lecture 2: Loops

In this lecture, we learned about **loops** and **data structures** — how to repeat tasks efficiently and how to store and organize data.

---

## 🔁 While Loops

A **`while` loop** runs as long as its condition is `True`.
When the condition becomes `False`, the loop stops.

### Basic Example

```python
i = 0
while i < 3:
    print("meow")
    i = i + 1
```

🔍 Explanation:

* Start with `i = 0`.
* The condition `i < 3` is checked.
* If `True`, `"meow"` is printed.
* `i` increases by 1 each time.
* When `i` becomes 3, the condition is `False` → loop stops.

Output:

```bash
meow
meow
meow
```

### Summary

> “Repeat the block while the condition is True.”

---

## 🔂 For Loops

A **`for` loop** automatically iterates over a sequence (like a list or range).
Each iteration assigns a new value to the loop variable.

### Example

```python
for i in [0, 1, 2]:
    print("meow")
```

Here:

* `i` takes the values `0`, `1`, and `2` in order.
* The body runs three times.

---

### Using `range()`

Instead of listing all values manually, we can use `range()`.

```python
for _ in range(3):
    print("meow")
```

`range(3)` produces `[0, 1, 2]` — note that `3` is **not included**.

Output:

```bash
meow
meow
meow
```

---

### Using `_` Instead of `i`

If the loop variable isn’t used, use `_` by convention:

```python
for _ in range(5):
    print("CS50p rocks!")
```

---

## ⚙️ Infinite Loops and `break` / `continue`

### `while True`

`while True:` creates an **infinite loop** that runs forever unless stopped manually.
We use `break` and `continue` to control it.

```python
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue  # Skip this iteration if input is negative
    else:
        break     # Exit the loop when input is valid
```

Then:

```python
for _ in range(n):
    print("meow")
```

🧠 Explanation:

* `continue` → go back to the start of the loop (skip current iteration)
* `break` → exit the loop completely

---

## 📋 Lists

A **list** stores multiple values in a single variable.

```python
students = ["Hermione", "Harry", "Ron"]
```

### Accessing Elements

```python
print(students[0])  # Hermione
print(students[1])  # Harry
print(students[2])  # Ron
```

### Looping Through a List

```python
for student in students:
    print(student)
```

Output:

```bash
Hermione
Harry
Ron
```

### The `len()` Function

`len()` returns the length of a list (number of elements).

```python
print(len(students))  # 3
```

### Enumerating Elements with Indexes

```python
for i in range(len(students)):
    print(i + 1, students[i])
```

Output:

```bash
1 Hermione
2 Harry
3 Ron
```

---

## 🗂️ Dictionaries

A **dictionary** stores data in **key–value pairs**.

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
```

### Accessing Values

```python
print(students["Hermione"])  # Gryffindor
print(students["Draco"])     # Slytherin
```

### Looping Through a Dictionary

```python
for student in students:
    print(student, students[student])
```

Output:

```bash
Hermione Gryffindor
Harry Gryffindor
Ron Gryffindor
Draco Slytherin
```

---

## 🔍 List of Dictionaries (Objects)

We can also store dictionaries inside a list — useful for representing multiple records.

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"])
```

Output:

```bash
Hermione Gryffindor Otter
Harry Gryffindor Stag
Draco Slytherin None
```

🧩 `None` means “no value” — the absence of data.

---

## 🧱 Nested Loops

A loop inside another loop is called a **nested loop**.
They’re useful for generating grids, tables, or shapes.

### `mario.py` Example

```python
def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each column in row
        for j in range(size):
            print("#", end="")  # Don't start a new line
        print()  # Move to the next line

main()
```

Output:

```bash
###
###
###
```

---

## 🎯 Summary

| Concept      | Description                                   |
| ------------ | --------------------------------------------- |
| `while`      | Repeats while a condition is `True`.          |
| `for`        | Iterates over a sequence (list, range, etc.). |
| `range(n)`   | Generates numbers from `0` to `n-1`.          |
| `break`      | Exits the loop immediately.                   |
| `continue`   | Skips the current iteration.                  |
| `list`       | An ordered collection of items.               |
| `dictionary` | A collection of key–value pairs.              |
| `None`       | Represents “no value” or “nothing.”           |
