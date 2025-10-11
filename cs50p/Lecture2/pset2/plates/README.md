# 🚘 Vanity Plates

This program validates **Massachusetts vanity license plates** according to the official formatting rules.
It checks whether a given plate meets all the conditions for being considered *valid*.

---

## 🧩 Problem Description

In Massachusetts, drivers can request a **vanity plate** — a personalized license plate with custom letters and numbers.
However, certain formatting rules must be followed:

1. **All vanity plates must start with at least two letters.**
2. **Plates must contain between 2 and 6 characters** (letters or numbers).
3. **Numbers cannot appear in the middle of a plate** — they must come only at the end.

   * Example: `AAA222` ✅ acceptable
   * Example: `AAA22A` ❌ not acceptable
   * The **first number** used **cannot be ‘0’**.
4. **No periods, spaces, or punctuation marks** are allowed — only letters and digits.

Your program should ask the user for a plate name and print:

```
Valid
```

if all conditions are met, or:

```
Invalid
```

if not.

---

## 💡 Approach

1. **Main logic:**
   The `main()` function prompts the user for a plate and prints “Valid” or “Invalid” based on the result of `is_valid()`.

2. **Validation checks:**
   The program uses several helper functions inside `is_valid()` to verify each rule:

   * `starts_with_two_letters(s)` → checks if the plate begins with at least two letters.
   * `valid_length(s)` → ensures length is between 2 and 6 characters.
   * `numbers_at_the_end(s)` → confirms that any digits appear only at the end.
   * `valid_first_number(s)` → ensures that if numbers exist, the first one isn’t `0`.
   * `no_punctuation(s)` → uses `.isalnum()` to reject punctuation or spaces.

3. Each check returns a **boolean** value (`True` or `False`), which is stored in a dictionary for clarity.
   The plate is valid only if **all** conditions return `True`.

---

## 🧠 Example

**Input:**

```
Plate: CS50
```

**Output:**

```
Valid
```

**Input:**

```
Plate: CS05
```

**Output:**

```
Invalid
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**plates.py**](./plates.py)

---

## ✅ What I Learned

* Applying **multiple logical conditions** to validate complex input.
* Using **helper functions** to break large problems into smaller, reusable parts.
* Working with **string methods** like `.isalpha()`, `.isdigit()`, and `.isalnum()`.
* Understanding **Boolean logic** and combining conditions using `and`.
* Designing clear, readable, and modular validation code in Python.