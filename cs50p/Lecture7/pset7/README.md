# 📂 Problem Set 7 — CS50P

This folder contains my solutions for **CS50’s Introduction to Programming with Python — Problem Set 7**.
Each problem is stored in its own directory, and each includes a dedicated `README.md` explaining the task, logic, and implementation details.

---

## 📌 Problems

* 🔹 **[NUMB3RS](./numb3rs/README.md)**
  Validates IPv4 addresses using regular expressions, ensuring each octet is between 0 and 255.

* 🔹 **[Watch on YouTube](./watch/README.md)**
  Extracts embedded YouTube video URLs from HTML `<iframe>` tags and converts them into shorter shareable links like `https://youtu.be/...`.

* 🔹 **[Working 9 to 5](./working/README.md)**
  Converts 12-hour formatted time ranges (e.g., `9:00 AM to 5:00 PM`) to 24-hour format (e.g., `09:00 to 17:00`), validating and handling edge cases like midnight, noon, and missing minutes.

* 🔹 **[Regular, um, Expressions](./um/README.md)**
  Counts occurrences of the standalone word **“um”**, case-insensitively, making sure it doesn’t match inside larger words like “yummy”.

* 🔹 **[Response Validation](./response/README.md)**
  Uses a third-party validation library to check whether a user-input email address is syntactically valid — without using `re`.

---

## 📚 What I Learned

* Strong understanding of **Regular Expressions**:

  * Character sets (`[]`)
  * Shorthand classes (`\w`, `\d`, `\s`)
  * Word boundaries (`\b`)
  * Capturing vs non-capturing groups
  * Anchors: `^` and `$`
  * Greedy vs non-greedy matching

* Input validation and string parsing:

  * Converting time formats
  * Extracting URL components
  * Preventing partial/false matches

* Testing with **pytest**:

  * Creating multiple test functions
  * Asserting valid and invalid cases
  * Testing edge cases and error handling

* Using external Python libraries:

  * Installing third-party packages with `pip`
  * Using `validators` or `validator-collection` to validate email addresses

---

## ✅ Required Tools

Some programs require additional libraries:

```bash
pip install validators
```

or

```bash
pip install validator-collection
```

---

## 🚀 How to Run Each Program

Example (NUMB3RS):

```bash
cd numb3rs
python numb3rs.py
```

Example (Watch on YouTube):

```bash
cd watch
python watch.py
```

Example (Working 9 to 5):

```bash
cd working
python working.py
```

---

> ✅ **Tip:**
> Problem Set 7 focuses heavily on **text analysis, validation, and pattern recognition**.
> These skills are extremely valuable for data cleaning, input sanitization, backend development, and any task that requires structured text processing.