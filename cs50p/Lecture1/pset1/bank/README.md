# 🏦 Problem Set 1 – Home Federal Savings Bank

> In Season 7, Episode 24 of *Seinfeld*, Kramer visits a bank that promises to give **$100** to anyone not greeted with “hello.”
> Instead, he’s greeted with a “hey,” and insists that it doesn’t count.
> The bank manager offers a compromise:
> “You got a greeting that starts with an *‘H’*. How about **$20**?”
> Kramer accepts.

---

## 🧠 Problem Description

In this problem, we’re asked to simulate the scenario from the Seinfeld episode.
The program should prompt the user for a greeting and determine how much money to give based on the form of greeting.

**The rules:**

* If the greeting starts with `"hello"` → print **`$0`**
* If the greeting starts with the letter `"h"` but is not `"hello"` → print **`$20`**
* Otherwise → print **`$100`**

---

## ⚙️ Implementation Details

1. **Get user input** with `input("Greeting: ")`.
2. **Normalize** the text to make the comparison case-insensitive and ignore extra spaces:

   * Convert to lowercase with `.lower()`
   * Remove surrounding whitespace with `.strip()`
3. **Check** the greeting using `startswith()`:

   * `startswith("hello")` → `$0`
   * `startswith("h")` → `$20`
   * Else → `$100`

---

## 💻 Solution

👉 You can view the full implementation here:
[`bank.py`](./bank.py)

---

## 🧩 Example Runs

```
$ python bank.py
Greeting: Hello there
$0
```

```
$ python bank.py
Greeting: Hey
$20
```

```
$ python bank.py
Greeting: Good morning
$100
```

---

## 💡 Notes

* `.startswith()` is a convenient way to check the beginning of a string.
* `.lower()` ensures the check is **case-insensitive**, so `"HELLO"` and `"hello"` both match.
* `.strip()` removes unnecessary whitespace from the input.
* This problem reinforces the use of **string methods** and **conditional logic** from **Lecture 1**.
