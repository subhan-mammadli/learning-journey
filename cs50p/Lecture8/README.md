# 📂 CS50P – Lecture 8

Welcome to the **Lecture 8** folder of my CS50’s *Introduction to Programming with Python* notes and exercises.

📘 **Contents:**

---

## 📝 **Lecture 8 Notes**

A detailed, beginner-friendly yet thorough introduction to **Object-Oriented Programming (OOP)** in Python.
This lecture explains how Python allows you to design **your own data types** using classes, giving you far more structure, flexibility, and expressive power than basic lists and dictionaries.

### Covered topics include:

### **🔹 Designing Classes & Creating Objects**

* What classes are and why we need them
* Instances, attributes, and encapsulation
* Difference between *objects*, *types*, and *constructors*

### **🔹 The `__init__` Constructor**

* Initializing attributes
* Validating data with `raise`
* Preventing invalid object state

### **🔹 The `__str__` Method**

* Making custom classes printable
* Returning human-readable string representations

### **🔹 Methods**

* How to write functions inside classes
* Why `self` is required
* Calling methods vs. calling plain functions

### **🔹 Tuples, Lists, and Dictionaries in OOP**

* Returning multiple values from functions
* Why tuples are immutable
* When to choose list or dict instead

### **🔹 Properties (`@property`)**

* Encapsulation and safe attribute access
* Writing getter and setter methods
* Hidden fields (`_attribute`) and controlled mutation
* Python’s internal behavior when using `object.attribute = value`

### **🔹 Class Methods & Static Methods**

* `@classmethod` with `cls`
* Factory methods like `Student.get()`
* `@staticmethod` for helper utilities

### **🔹 Inheritance (Extending Classes)**

* Parent and child classes
* Using `super()` correctly
* How Python’s own Exception classes use inheritance

### **🔹 Operator Overloading**

* Redefining built-in operators
* Implementing custom behavior for `+`, `*`, and others
* Example: adding two `Vault` objects

These notes provide both conceptual explanations and practical examples.
You can find them here:

👉 **[notes.md](./notes.md)**

---

## 🧪 **Problem Set 8 Solutions**

Lecture 8’s exercises apply OOP to real-world scenarios — designing custom classes, validating attributes, and generating output using external libraries.

The following problems are implemented in this folder:

### **🍪 Cookie Jar**

A fully object-oriented simulation of a cookie jar with:

* capacity control
* deposit/withdraw mechanics
* string representation with cookie emojis
* input validation through exceptions

Solution:
👉 **[`jar.py`](./jar.py)**
👉 **[`test_jar.py`](./test_jar.py)**

---

### **📄 Seasons of Love**

A date-handling exercise that uses:

* the `datetime` module
* arithmetic with date and timedelta objects
* the `inflect` library for converting numbers to English words
* error handling for invalid dates

Solution:
👉 **[`seasons.py`](./seasons.py)**
👉 **[`test_seasons.py`](./test_seasons.py)**

---

### **👕 CS50 Shirtificate**

A PDF-generation program using `fpdf2` that:

* loads and centers an image
* overlays the user’s name in white text
* aligns text and controls layout on an A4 portrait page
* outputs a custom “shirtificate” in PDF format

Solution:
👉 **[`shirtificate.py`](./shirtificate.py)**
👉 Includes **`shirtificate.png`** as the template image.

---

## 🎯 Summary

Lecture 8 introduces the core pillars of OOP and demonstrates how Python lets you design powerful abstractions using:

✔ Classes & objects
✔ Constructors and methods
✔ Encapsulation with properties
✔ Inheritance and operator overloading
✔ External libraries (datetime, inflect, fpdf2)

These concepts form the foundation for writing clean, scalable, and testable software in Python.