# 🛒 Grocery List

This program simulates a simple **grocery list manager** that keeps track of items you want to buy and how many times each item is added.

---

## 🧩 Problem Description

In this problem, you are asked to implement a program (`grocery.py`) that:

1. Prompts the user to input grocery items, **one per line**.
2. Continues accepting input until the user presses **`Ctrl + D`** (EOF).
3. **Counts how many times** each item is entered.
4. When input ends, prints the grocery list:

   * In **all uppercase**
   * **Alphabetically sorted**
   * Each line prefixed by the item’s **quantity**

Example:

```
2 APPLE
1 BANANA
```

All input is treated **case-insensitively**, meaning “apple”, “APPLE”, and “Apple” are considered the same item.

---

## 💡 Approach

1. **Using a Dictionary**

   * Create an empty dictionary `d = {}`.
   * The **keys** are item names (in uppercase).
   * The **values** are the number of times each item was entered.

2. **Reading Input**

   * Use an infinite `while True` loop with a `try` / `except` block.
   * Inside the loop:

     * Read input with `input()`.
     * Convert to uppercase and remove extra spaces using `.upper().strip()`.
     * If the item already exists in the dictionary, increment its value by 1.
     * Otherwise, add it to the dictionary with an initial value of 1.

3. **Handling End of Input**

   * When the user presses **Ctrl + D**, Python raises an `EOFError`.
   * Catch this exception and:

     * Sort the dictionary alphabetically using `dict(sorted(d.items()))`
     * Loop through the sorted dictionary and print each item as:

       ```
       <count> <ITEM>
       ```

---

## 🧠 Example

**Input:**

```
apple
banana
apple
^D
```

**Output:**

```
2 APPLE
1 BANANA
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**grocery.py**](./grocery.py)

---

## ✅ What I Learned

* How to use **dictionaries** to count and store item occurrences.
* How to handle **EOFError** (triggered by `Ctrl + D`) to stop user input.
* How to **sort dictionaries** alphabetically by keys.
* How to use **string methods** like `.upper()` and `.strip()` for clean input handling.
* Structuring a simple, interactive Python program using a **loop with exception handling**.

