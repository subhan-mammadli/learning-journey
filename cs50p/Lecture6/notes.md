
# 📘 CS50P — Lecture 6 - File I/O

**Working with Files, CSV, DictReader, DictWriter, and Images with PIL**

---

## 📂 Working with Files — `open()`

Whenever you want to work with a file in Python, the first step is to open it.

```python
open(file, mode)
```

- `file` → name or path of the file
    
- `mode` → how the file should be opened
    
    - `"r"` → read mode (default)
        
    - `"w"` → write mode
        
    - `"a"` → append mode
        

### ✅ Basic example: writing to a file

```python
file = open("names.txt", "w")
name = input("What's your name? ")
file.write(name)
file.close()
```

### `.write()`

Writes text into the file.

### `.close()`

Closes the file. If you don’t close a file, data may not be properly saved.

---

## ✅ More Pythonic Way — Using `with`

Using `with` automatically closes the file when the block ends.

```python
with open("names.txt", "a") as file:
    name = input("What's your name? ")
    file.write(f"{name}\n")
```

- `"w"` removes old content and rewrites the file
    
- `"a"` adds new data without deleting existing content
    

---

## 📖 Reading a File — `"r"` Mode

```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
```

- `.readlines()` returns a list of lines
    
- Each line includes `\n`, so `rstrip()` cleans it up
    

Shorter and cleaner:

```python
with open("names.txt") as file:
    for line in file:
        print("Hello,", line.rstrip())
```

---

## 📌 Reading and Sorting Names

```python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
```

Or even shorter:

```python
with open("names.txt") as file:
    for name in sorted(file):
        print(f"Hello, {name.rstrip()}")
```

---

## 🔤 `sorted()` Function

```python
sorted(iterable, /, *, key=None, reverse=False)
```

- `reverse=True` → reverse order
    
- `key=` lets you sort based on a rule
    
    - `key=len` → sort by length
        
    - `key=lambda ...` → custom sorting
        

---

# ✅ CSV (Comma-Separated Values)

A CSV file stores data in a simple text format where columns are separated by commas.

Example:

```csv
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
```

```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```

---

## ✅ Better Design — Using Dictionaries

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```

---

## ✅ Sorting with `key=...`

```python
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
```

---

# ⚡ Lambda Functions

A lambda is an **anonymous function** used for short, simple tasks.

```python
add = lambda x, y: x + y
print(add(3, 5))
```

Sorting with lambda:

```python
for student in sorted(students, key=lambda s: s["name"]]):
    print(f"{student['name']} is in {student['house']}")
```

---

# ❗ Problem — `split()` is not enough

If CSV contains:

```csv
Harry, Number Four, Privet Drive
Ron, The Burrow
Draco, Malfoy Manor
```

This will fail:

```python
name, home = line.split(",")
```

Because Harry’s home contains **two commas**.  
✅ Solution: use the `csv` module.

---

# ✅ `csv.reader`

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is from {student['home']}")
```

✅ Automatically handles commas and quotes  
✅ No need to use `split()`

---

# ✅ `csv.DictReader()`

If the CSV has headers:

```csv
name, home
Harry, "Number Four, Privet Drive"
Ron, The Burrow
Draco, Malfoy Manor
```

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda s: s["home"]):
    print(f"{student['name']} is from {student['home']}")
```

✅ Works even if column order changes  
✅ Extra columns don’t break the code

---

# ✅ Writing to CSV — `csv.writer`

```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
```

- `.writerow()` → writes a new row to the file
    
- Automatically adds quotes if commas exist
    

---

# ✅ `csv.DictWriter`

```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```

- `fieldnames=` defines the column order
    
- You write a dictionary instead of a list
    

---

# 🖼️ Working with Images — PIL / Pillow

Pillow is a Python library used for:

✅ opening images  
✅ modifying them  
✅ filtering and resizing  
✅ creating GIF animations

---

## ✅ Creating a GIF from multiple images

```python
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
)
```

```bash
$ python costumes.py costume1.gif costume2.gif costume3.gif
```

- `save_all=True` → keeps multiple frames
    
- `duration` → time between frames (ms)
    
- `loop=0` → infinite loop playback
    

---

# ✅ Summary

In this lecture, we learned how to:

✅ Open, read, write, and append to files  
✅ Use `with` to automatically close files  
✅ Read and write CSV files properly  
✅ Use `csv.reader`, `csv.DictReader`, `csv.writer`, and `csv.DictWriter`  
✅ Sort data using `sorted()`, `key`, and `lambda`  
✅ Work with images and create GIFs using Pillow
