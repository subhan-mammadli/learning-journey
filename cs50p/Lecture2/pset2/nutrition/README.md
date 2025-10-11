# 🍎 Nutrition Facts

This program provides the **calorie information for fruits** based on the official FDA *Nutrition Facts* poster for the 20 most frequently consumed raw fruits in the U.S.

---

## 🧩 Problem Description

The **U.S. Food & Drug Administration (FDA)** publishes nutrition information for fruits, which stores may display for consumers.

In this problem, your task is to write a program that:

* Prompts the user to **input a fruit name** (case-insensitive).
* Outputs the **number of calories** in one serving of that fruit.
* Ignores any input that **isn’t a valid fruit** from the FDA list.

Example fruits include:
`apple`, `banana`, `strawberries`, `watermelon`, etc.

---

## 💡 Approach

1. A **dictionary** named `fruits` stores each fruit’s calorie count.
   Example:

   ```python
   fruits = {
       "Apple": 130,
       "Banana": 110,
       "Orange": 80,
       ...
   }
   ```
2. The user’s input is converted to **lowercase** using `.lower()` to ensure case-insensitive comparison.
3. The program loops through the dictionary keys, and if the lowercase version of a fruit matches the user’s input, it prints:

   ```
   Calories: <value>
   ```
4. If the fruit is not found in the dictionary, the program simply prints nothing (per CS50P’s instructions).

---

## 🧠 Example

**Input:**

```
Item: Apple
```

**Output:**

```
Calories: 130
```

**Input:**

```
Item: mango
```

**Output:**

```
# (no output)
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**nutrition.py**](./nutrition.py)

---

## ✅ What I Learned

* How to store data using **Python dictionaries (`dict`)**.
* Using `.lower()` to perform **case-insensitive string comparisons**.
* Accessing dictionary values dynamically using **key lookups**.
* Writing simple **input–output logic** for real-world data mapping tasks.