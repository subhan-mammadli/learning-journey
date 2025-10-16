# 📅 Outdated

This program converts dates written in **U.S. format** (month-day-year) into the **ISO 8601 standard format** (year-month-day).

---

## 🧩 Problem Description

In the United States, dates are often written in **MM/DD/YYYY** or **Month Day, Year** format — e.g., `9/8/1636` or `September 8, 1636`.
However, this format is ambiguous and not easily sortable.

Your task is to implement a program (`outdated.py`) that:

1. Prompts the user to enter a date in **either** of these formats:

   * `MM/DD/YYYY`
   * `Month Day, Year`
2. Converts and outputs the date in **YYYY-MM-DD** format.
3. If the input is invalid (not a real date or incorrectly formatted), the program should **reprompt** the user.

You can assume:

* Each month has **no more than 31 days**.
* The list of valid months is predefined:

  ```python
  [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
  ]
  ```

---

## 💡 Approach

1. **List of Months**
   Store all valid month names in a list to easily match them with their corresponding number (January → 1, February → 2, etc.).

2. **Input Handling with Loops and Exceptions**

   * Use a `while True` loop to repeatedly prompt the user until a valid date is entered.
   * Use **`try` / `except`** blocks to handle different input formats:

     * The first `try` block handles the numeric format (`MM/DD/YYYY`).
     * The nested `try` block inside `except ValueError` handles the text format (`Month Day, Year`).

3. **Validation**

   * Check that `1 ≤ month ≤ 12` and `1 ≤ day ≤ 31`.
   * If valid, format and print the result as:

     ```
     YYYY-MM-DD
     ```

4. **Month Conversion**

   * For text-based months (e.g., "September"), find the index in the `months` list and add `1` to get its numerical value.

5. **Formatting Output**

   * Use Python’s formatted string syntax to ensure:

     * Year has **4 digits**
     * Month and day have **2 digits each**, with leading zeros if needed
       Example:

       ```python
       f"{year:04}-{month:02}-{day:02}"
       ```

---

## 🧠 Example

**Input:**

```
Date: September 8, 1636
```

**Output:**

```
1636-09-08
```

**Input:**

```
Date: 9/8/1636
```

**Output:**

```
1636-09-08
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**outdated.py**](./outdated.py)

---

## ✅ What I Learned

* How to handle **multiple input formats** gracefully in Python.
* How to use **exception handling (try / except)** for input validation.
* How to **convert month names** into numeric values using lists.
* How to use **f-string formatting** to standardize date output.
* How to design a **loop that reprompts until valid input is entered**.


