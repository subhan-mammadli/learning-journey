# 🧩 CS50P — Lecture 8

# Object-Oriented Programming (OOP) in Python


In this lecture, we move from working with simple data structures like lists, tuples, and dictionaries into the more powerful world of **Object-Oriented Programming**.
These notes explain not only *what* happens but also *why* it happens — including Python’s internal logic and behavior.

This document is designed as a complete learning resource for CS50P students.

---

# 1. Returning Multiple Values in Python

Consider the following function:

```python
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
```

You might think this function returns **two values**, but Python actually returns **one value**:
a **tuple**.

```python
(name, house)
```

### Tuples

A **tuple** is similar to a list, but it is **immutable** — you cannot change its items.

Example:

```python
student = ("Padma", "Gryffindor")
student[1] = "Ravenclaw"
```

Output:

```
TypeError: 'tuple' object does not support item assignment
```

### When should you use a tuple?

✔ When the structure is fixed
✔ When the data should not change
✔ When you want safer code with fewer accidental modifications

---

# 2. If You Need Mutability → Use a List

```python
return [name, house]
```

Now this works:

```python
student[1] = "Ravenclaw"
```

But in most cases, especially when representing structured data like a “student,” a simple list is not expressive enough.

---

# 3. More Readable and Safer → Use a Dictionary

```python
return {"name": name, "house": house}
```

Usage:

```python
student["name"]
student["house"]
```

Dictionaries give meaningful names to the data and are often a stepping stone to creating full classes.

---

# 4. Creating Your Own Data Type with Classes

```python
class Student:
    ...
```

A **class** defines a new data type.
An **object (instance)** is a variable created from that class.

Example:

```python
student = Student()
student.name = "Harry"
student.house = "Gryffindor"
```

This approach works but is not ideal because:

❌ There is no validation
❌ Attributes can be added incorrectly
❌ Structure is not guaranteed

The solution? → A constructor.

---

# 5. The `__init__` Constructor

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

This method is called **automatically** when you create a new object:

```python
student = Student("Harry", "Gryffindor")
```

Internally Python does:

```python
Student.__init__(student, "Harry", "Gryffindor")
```

✔ `self` refers to the current object
✔ `self.attribute = value` creates attributes

---

# 6. Validation (Checking Values) with `raise`

```python
if not name:
    raise ValueError("Name missing")

if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    raise ValueError("Invalid house")
```

`raise` interrupts the program with a meaningful error message.

Validation is essential in real-world programs, and OOP helps enforce it.

---

# 7. Making Objects Printable with `__str__`

Without defining `__str__`, printing an object gives:

```
<__main__.Student object at 0x10273be80>
```

Add:

```python
def __str__(self):
    return f"{self.name} from {self.house}"
```

Output becomes human-readable:

```
Harry from Gryffindor
```

---

# 8. Methods — Functions Inside a Class

A function written inside a class is called a **method**.

Example:

```python
def charm(self):
    match self.patronus:
        case "Stag": return "🦌"
        case "Otter": return "🦦"
        case _: return "✨"
```

Usage:

```python
student.charm()
```

### Why must methods include `self`?

Because Python internally calls:

```python
Student.charm(student)
```

---

# 9. Properties — Controlled Access to Attributes

This is one of the most important parts of Lecture 8.

Suppose we define:

```python
@property
def house(self):
    return self._house

@house.setter
def house(self, house):
    if house not in [...]:
        raise ValueError("Invalid house")
    self._house = house
```

Now when you do:

```python
student.house = "Number Four, Privet Drive"
```

Python thinks:

> “house has a setter, so I shouldn't assign directly.
> I must call the setter method.”

Internally Python runs:

```python
Student.house.__set__(student, "Number Four, Privet Drive")
```

Inside the setter, this happens:

```python
if house not in valid_houses:
    raise ValueError("Invalid house")
```

Thus validation prevents incorrect assignments.

### Why `_house`?

`_house` is a naming convention for “private-like” attributes used behind the scenes.

---

# 10. Class Methods (`@classmethod`)

Methods that belong to the class (not only to objects).

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

This creates a new object using the class itself (`cls`).

---

# 11. Static Methods (`@staticmethod`)

They do not depend on the class or an instance.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

Use static methods for small helper functions logically related to the class.

---

# 12. Inheritance (Extending Classes)

A subclass inherits attributes and methods from a parent class.

```python
class Wizard:
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
```

`super()` calls the constructor of the parent class.

This technique is widely used — even Python’s built-in exception classes follow this hierarchy.

---

# 13. Operator Overloading

Python lets you redefine how operators work for your class.

Example: overloading `+` for Vault objects:

```python
def __add__(self, other):
    g = self.galleons + other.galleons
    s = self.sickles + other.sickles
    k = self.knuts + other.knuts
    return Vault(g, s, k)
```

Usage:

```python
total = potter + weasley
```

---

# 14. Additional Tools

### `type()`

Returns the type of a variable.

```python
type(student)
```

### `...` (Ellipsis)

A placeholder used when code will be added later.

---

# ✔ Summary of What You Learned

By the end of Lecture 8 you should understand:

✔ The difference between tuple, list, and dict for structured data
✔ How classes and objects work
✔ The purpose of `__init__`
✔ How to validate attributes using `raise`
✔ How to make objects printable with `__str__`
✔ What methods are and why they require `self`
✔ How `@property` and setters work internally
✔ How class methods and static methods differ
✔ How inheritance enables code reuse
✔ How to overload operators like `+`
✔ How Python behaves behind the scenes when you manipulate object attributes