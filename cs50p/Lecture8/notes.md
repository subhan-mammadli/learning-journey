# 🧩 CS50P — Lecture 8

## ⭐ Object-Oriented Programming (OOP) in Python

In this lecture, we move from simple data structures like lists and dictionaries into the more powerful world of **Object-Oriented Programming**.
These notes explain both *what* happens and *why* it happens — including how Python behaves behind the scenes.

This document is designed as a complete and clean learning resource for CS50P students.

---

# 📘 1. Returning Multiple Values in Python

```python
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
```

Although it looks like the function returns **two separate values**, Python actually returns a **single tuple**:

```python
(name, house)
```

### ✔ Tuples

A tuple is similar to a list but **immutable**.

```python
student = ("Padma", "Gryffindor")
student[1] = "Ravenclaw"  # ❌ Error
```

```
TypeError: 'tuple' object does not support item assignment
```

### When should you use a tuple?

* ✔ When the structure is fixed
* ✔ When data should not change
* ✔ When you want safer, more predictable code

---

# 📗 2. If You Need Mutability → Use a List

```python
return [name, house]
```

Lists allow modification:

```python
student[1] = "Ravenclaw"  
```

But lists don’t express meaning clearly enough for structured data.

---

# 📕 3. More Expressive and Safer → Use a Dictionary

```python
return {"name": name, "house": house}
```

Access:

```python
student["name"]
student["house"]
```

Dictionaries are often the stepping stone toward creating **custom classes**.

---

# 🏗 4. Defining Your Own Data Type with Classes

```python
class Student:
    ...
```

An object is an **instance** of a class:

```python
student = Student()
student.name = "Harry"
student.house = "Gryffindor"
```

But this is unsafe:

* ❌ No validation
* ❌ Wrong attributes can be added
* ❌ Structure is not guaranteed

Solution: **constructor**.

---

# ⚙️ 5. The `__init__` Constructor

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

Usage:

```python
student = Student("Harry", "Gryffindor")
```

Internally:

```python
Student.__init__(student, "Harry", "Gryffindor")
```

---

# 🛡 6. Validation with `raise`

```python
if not name:
    raise ValueError("Name missing")

if house not in valid_houses:
    raise ValueError("Invalid house")
```

Validation ensures correctness and prevents incorrect assignments.

---

# 📝 7. Making Objects Printable with `__str__`

Default print:

```
<__main__.Student object at 0x10273be80>
```

Custom version:

```python
def __str__(self):
    return f"{self.name} from {self.house}"
```

Output:

```
Harry from Gryffindor
```

---

# 🧩 8. Methods — Functions Inside Classes

```python
def charm(self):
    match self.patronus:
        case "Stag": return "🦌"
        case "Otter": return "🦦"
        case _: return "✨"
```

Why `self`?
Because Python internally calls:

```python
Student.charm(student)
```

---

# 🔒 9. Properties — Controlled Attribute Access

```python
@property
def house(self):
    return self._house

@house.setter
def house(self, house):
    if house not in valid_houses:
        raise ValueError("Invalid house")
    self._house = house
```

Python automatically calls the setter when you do:

```python
student.house = "Privet Drive"
```

### Why `_house`?

By convention, attributes starting with `_` are “internal” and not meant to be accessed directly.

---

# 🏛 10. Class Methods (`@classmethod`)

```python
@classmethod
def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)
```

Usage:

```python
student = Student.get()
```

`cls` refers to the class itself.

---

# 🧰 11. Static Methods (`@staticmethod`)

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

Use static methods for helpers logically related to the class.

---

# 🧬 12. Inheritance (Extending Classes)

```python
class Wizard:
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
```

`super()` calls the parent constructor.

---

# ➕ 13. Operator Overloading

```python
def __add__(self, other):
    return Vault(
        self.galleons + other.galleons,
        self.sickles + other.sickles,
        self.knuts + other.knuts,
    )
```

Usage:

```python
total = potter + weasley
```

---

# 🛠 14. Additional Tools

### `type()`

Returns the type of a variable.

```python
type(student)
```

### `...` (Ellipsis)

A placeholder used when code will be added later.

---

# 🎯 Summary of What You Learned

> ### ✔ By the end of Lecture 8, you should understand:

* **Tuple vs List vs Dict** for structured data
* **How classes and objects work**
* The purpose of **`__init__`**
* Validating attributes using **`raise`**
* Making objects printable with **`__str__`**
* Why methods require **`self`**
* How **`@property`** and setters work
* How **class methods** and **static methods** differ
* How **inheritance** enables code reuse
* How to **overload operators** like `+`
* How Python behaves internally when objects are manipulated

---
