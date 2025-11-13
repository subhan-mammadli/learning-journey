# 📂 Problem Set 8 — CS50P

This folder contains my solutions for **CS50’s Introduction to Programming with Python — Problem Set 8**.
Each problem is stored in its own directory (or file, when specified), and each includes a dedicated `README.md` explaining the task, design decisions, and implementation details.

---

## 📌 Problems

* 🔹 **[Seasons of Love](./seasons/README.md)**
  Calculates how many minutes a user has lived based on their date of birth.
  Uses the `datetime` module for calendar arithmetic and the `inflect` library to convert large numbers into English words, replicating the lyrical style of *Rent*.

* 🔹 **[Cookie Jar](./jar/README.md)**
  Implements an object-oriented cookie jar with a customizable capacity.
  Supports depositing and withdrawing cookies, enforces invariants through exceptions, and uses Python properties for safe attribute access.

* 🔹 **[CS50 Shirtificate](./shirtificate/README.md)**
  Generates a personalized **PDF shirtificate** containing a CS50 t-shirt image with the user’s name printed on it.
  Uses the `fpdf2` library to work with layout, images, font styling, and PDF generation.

---

## 📚 What I Learned

### ✔ Strong fundamentals of **Object-Oriented Programming**

* Creating custom classes
* Using constructors (`__init__`)
* Writing instance methods
* Encapsulating data with private attributes
* Overriding special methods like `__str__`
* Designing clean and reusable abstractions

### ✔ Safe attribute management with **@property**

* Getter and setter methods
* Input validation through `ValueError`
* Understanding how Python invokes property setters internally

### ✔ Working with built-in and third-party libraries

* `datetime.date` and `timedelta` for date calculations
* `inflect.engine()` for natural-language number conversion
* `fpdf2.FPDF` for generating PDFs with text, images, and custom layout

### ✔ Proper error handling

* Using `try/except` to validate dates
* Exiting cleanly with `sys.exit()`
* Preventing invalid object states in OOP design

### ✔ Writing meaningful program output

* Converting numbers to English words
* Centering text and images on PDFs
* Returning human-friendly string representations for objects

---

## 📦 Required Tools

Some problems require external libraries:

```bash
pip install inflect
```

```bash
pip install fpdf2
```

Both libraries are lightweight and widely used for text generation and PDF creation.

---

## 🚀 How to Run Each Program

Example (Seasons of Love):

```bash
cd seasons
python seasons.py
```

Example (Cookie Jar):

```bash
cd jar
python jar.py
```

Example (CS50 Shirtificate):

```bash
cd shirtificate
python shirtificate.py
```

---

> ✅ **Tip:**
> Problem Set 8 is where everything from earlier lectures—functions, exceptions, testing, and now classes—comes together.
> By completing these exercises, you gain hands-on experience with **abstraction**, **encapsulation**, **data modeling**, and **external libraries**, all of which are essential skills for real-world Python development.