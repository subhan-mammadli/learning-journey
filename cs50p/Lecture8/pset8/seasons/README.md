# 📂 Problem Set 8 — Seasons of Love

This directory contains my solution to **CS50P’s “Seasons of Love” problem**, in which the goal is to calculate a person’s age in minutes and express that number in **English words**, inspired by the musical *Rent*.

The program is implemented in **`seasons.py`**, and its corresponding unit tests are in **`test_seasons.py`**.

---

# 🎵 Problem Description

The challenge is based on the iconic lyrics from *“Seasons of Love”*:

> *Five hundred twenty-five thousand, six hundred minutes…
> How do you measure, measure a year?*

A year normally has **525,600 minutes** (365 × 24 × 60).
However, when calculating someone’s age over many years, the total number of minutes changes depending on **how many leap years** have passed.

Your task is to write a program that:

1. Prompts the user for their **date of birth** in `YYYY-MM-DD` format.
2. Calculates how many **minutes** they have lived until today
   (assuming both birth time and current time are **midnight**, even if run at noon).
3. Converts the minute count into **English words** (e.g., “One million two hundred thirty-four thousand minutes”).
4. Prints the result in a format similar to the song — **no “and”** in the wording.
5. Handles invalid input properly by exiting with a message.

You must also implement tests that verify your helper functions using `pytest`.

---

# 🧠 Key Concepts Behind the Solution

Below is an explanation of the Python concepts used in the implementation.
This section is intentionally **thorough**, describing both how the solution works and *why* these techniques are necessary.

---

## 📅 1. Parsing a Date Using `datetime`

The program asks the user for a date string. To convert it into a real date object, the implementation uses:

### `datetime.strptime()`

This method attempts to parse a string according to a given format:

```python
datetime.strptime("1999-10-20", "%Y-%m-%d")
```

✔ If the format matches, it returns a `datetime` object.
✔ If the format does *not* match, it raises a **ValueError**.

The program catches this error and exits gracefully with:

```
Invalid date
```

After parsing, the `.date()` method is used to extract just the **date** component (without time).

---

## 📆 2. Getting Today’s Date

Python’s `date` class provides:

### `date.today()`

This returns the current date (year, month, day) as a `date` object.

Even if the user runs the program at noon, the problem specification requires us to **assume midnight**, so time-of-day is ignored completely.

---

## ➖ 3. Calculating the Difference Between Two Dates

Subtracting one `date` object from another:

```python
today - birthday
```

returns a **`timedelta` object**.

A `timedelta` contains several attributes, but the one we need is:

### `.days`

The total number of days between the two dates.

This automatically includes:

✔ Leap years
✔ Correct calendar calculations
✔ All Gregorian calendar rules

Thus, we do **not** manually handle leap years — Python does it for us.

---

## ⏱️ 4. Converting Days to Minutes

Since:

```
1 day = 24 × 60 minutes = 1,440 minutes
```

We compute:

```
total_minutes = days * 24 * 60
```

This gives the total minutes the user has lived.

---

## 🔤 5. Converting Numbers to English Words (`inflect`)

The `inflect` library transforms numbers into English phrases.

### `inflect.engine()`

Creates an engine object with many helper functions.

### `number_to_words()`

Converts integers into written-out English:

```
123 → "one hundred twenty-three"
```

We use:

```
andword=""
```

to remove “and” from the output, matching the style of the song.

Finally, the text is capitalized and appended with `" minutes"`.

---

## 🧪 6. Testing With `pytest`

The file **`test_seasons.py`** thoroughly checks the behavior of the helper function(s):

### ✔ Valid Inputs

Tests confirm that known dates produce the correct English text.

### ✔ Invalid Inputs

Dates with:

* impossible months (`2025-13-01`)
* impossible days (`2025-12-32`)
* wrong formatting (`04 April, 1988`)

must cause the program to exit using `sys.exit()`.

In tests, this is verified using:

```python
with pytest.raises(SystemExit):
```

These tests ensure that the program is robust and handles errors cleanly.

---

# 🗂️ File Structure

```
.
├── seasons.py
└── test_seasons.py
```

* **`seasons.py`** contains:

  * input handling
  * date validation
  * minute calculation
  * English conversion
  * main logic structure (`main()` and helper functions)

* **`test_seasons.py`** contains:

  * unit tests for valid inputs
  * unit tests for invalid inputs
  * verification that `sys.exit()` behaves correctly

The actual code can be found here:

* [seasons.py](./seasons.py)
* [test_seasons.py](./test_seasons.py)

---

# ▶️ Usage

Run the program:

```bash
python seasons.py
```

Run the tests:

```bash
pytest test_seasons.py
```

---

# ✅ Summary

This problem demonstrates:

✔ How to parse, validate, and manipulate date objects
✔ How `timedelta` automatically accounts for leap years
✔ How to convert numbers into English words using `inflect`
✔ How to organize a program into multiple functions
✔ How to exit cleanly with `sys.exit` on invalid input
✔ How to write robust automated tests using `pytest`

The challenge brings together **date arithmetic**, **string formatting**, **library usage**, and **test-driven development**, making it one of the more practical exercises in CS50P.