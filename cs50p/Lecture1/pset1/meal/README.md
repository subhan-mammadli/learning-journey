# ⏰ Problem Set 1 – Meal Time

## 🧠 Problem Description

In this problem, you’ll write a program that determines which **meal time** it is based on a user’s inputted time.

The user will enter the time in **24-hour format**, such as `7:30` or `18:45`, and your program will print whether it’s **breakfast time**, **lunch time**, or **dinner time**, depending on the hour.

---

## ⚙️ Implementation Details

1. **Prompt the user** for a time input:

   ```python
   time = input("What time is it? ")
   ```

2. **Convert** the time (in `HH:MM` format) into a **floating-point number** to simplify comparisons.
   Example:

   ```
   7:30 → 7.5
   12:00 → 12.0
   18:45 → 18.75
   ```

   This is done using the formula:

   ```python
   hours + minutes / 60
   ```

3. **Use `if-elif` statements** to check which range the time falls into:

   * Between **7:00 and 8:00 → breakfast time**
   * Between **12:00 and 13:00 → lunch time**
   * Between **18:00 and 19:00 → dinner time**

4. Structure the program with a `main()` function and a helper function `convert()` for clean organization.

---

## 💻 Solution

👉 Full implementation:
[`meal.py`](./meal.py)

---

## 🧩 Example Runs

```
$ python meal.py
What time is it? 7:30
breakfast time
```

```
$ python meal.py
What time is it? 12:45
lunch time
```

```
$ python meal.py
What time is it? 18:10
dinner time
```

```
$ python meal.py
What time is it? 22:00
# (no output)
```

---

## 🧩 Key Concepts

| Concept            | Description                                  |
| ------------------ | -------------------------------------------- |
| `.split(':')`      | Splits the input into hours and minutes.     |
| `int()`            | Converts string values into integers.        |
| `float` arithmetic | Allows fractional time values like `7.5`.    |
| Conditional ranges | Used to determine which meal period applies. |

---

## 💡 Notes

* The `convert()` function isolates conversion logic, keeping the main program clean and readable.
* This exercise reinforces **function design**, **numeric operations**, and **conditional logic** in Python.
* You could easily expand it to include other time ranges or outputs (e.g., “snack time!”).
