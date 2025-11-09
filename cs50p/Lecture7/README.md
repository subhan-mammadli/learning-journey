# 📂 CS50P – Lecture 7

Welcome to the **Lecture 7** folder of my CS50’s *Introduction to Programming with Python* notes and exercises.

📘 **Contents:**

* **Lecture 7 Notes:**
  A clear and beginner-friendly summary of Python’s **Regular Expressions (Regex)** — a powerful tool for searching, validating, and manipulating text.
  Covered topics include:

  * What regular expressions are and why they matter

  * The `re` module and its core functions:

    * `re.search()`
    * `re.match()`
    * `re.fullmatch()`
    * `re.findall()`
    * `re.split()`
    * `re.sub()`

  * Important regex symbols and sequences:

    * `.`, `*`, `+`, `?`, `{m,n}`, `^`, `$`
    * Character sets: `[a-z]`, `[A-Z]`, `[0-9]`, `[^...]`
    * Word and whitespace classes: `\w`, `\d`, `\s`, and their opposites
    * Word boundaries with `\b`
    * Capturing & non-capturing groups: `( )` vs `(?: )`
    * Greedy vs non-greedy matching

  * Practical validation examples:

    * Checking IPv4 addresses
    * Recognizing YouTube embed links
    * Converting 12-hour time to 24-hour format
    * Counting standalone words like “um”

  * Cleaner code tips:

    * Using raw strings (`r""`)
    * Walrus operator (`:=`)
    * Extracting regex matches with `.group()` and `.groups()`

* **Problem Set 7 Solutions:**
  Each exercise applies regex and text processing to real scenarios such as:

  * Validating IP addresses (`NUMB3RS`)
  * Extracting YouTube video IDs (`Watch on YouTube`)
  * Converting time formats (`Working 9 to 5`)
  * Counting standalone words (`Regular, um, Expressions`)
  * Validating emails with third-party libraries (`Response Validation`)