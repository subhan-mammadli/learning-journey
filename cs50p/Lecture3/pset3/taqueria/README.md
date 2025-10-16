# 🌮 Felipe’s Taqueria

This program simulates a simple **ordering system** for Felipe’s Taqueria — a popular restaurant near Harvard Square.
Users can order menu items one by one, and the program calculates the running total of the order in real time.

---

## 🧩 Problem Description

Felipe’s Taqueria offers a menu of delicious Mexican dishes, each with a specific price.
For this problem, you are given a predefined `dict` representing the restaurant’s menu:

```python
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

You must implement a program in `taqueria.py` that:

1. Continuously **prompts the user** for menu items, one per line.
2. **Adds the item’s price** to the running total whenever a valid menu item is entered.
3. After each valid entry, **displays the total cost** so far, formatted with a dollar sign (`$`) and two decimal places.
4. **Ends input** when the user presses **`Ctrl + D`** (EOF).
5. **Ignores invalid items** (i.e., anything not found on the menu).
6. Treats all user input **case-insensitively**.

---

## 💡 Approach

1. **Menu Setup**
   A `menu` dictionary stores all available items and their prices.
   The **keys** are the item names, and the **values** are the corresponding prices.

2. **Main Logic (`main()`):**

   * A variable `total` is initialized to store the accumulated total cost.
   * Inside a `while True` loop, the program:

     * Prompts for user input (`input("Item: ")`)
     * Converts it to lowercase to make comparison case-insensitive
     * Iterates through `menu` and checks if the input matches any menu item (by comparing lowercase versions)
     * If there’s a match, adds the corresponding price to `total` and prints the running total using formatted output:

       ```python
       print(f"${total:.2f}")
       ```
   * If the user presses **Ctrl + D**, an `EOFError` is raised.
     The program handles this with an `except EOFError:` block, prints a newline, and exits the loop gracefully.

3. **Error Handling:**

   * The program uses `try` / `except` to prevent crashes when input ends.
   * Ignores invalid entries silently — only valid menu items affect the total.

---

## 🧠 Example

**Input:**

```
Item: Taco
Item: Burrito
Item: nachos
^D
```

**Output:**

```
$3.00
$10.50
$21.50
```

---

## 📄 Source File

You can view the complete implementation here:
➡️ [**taqueria.py**](./taqueria.py)

---

## ✅ What I Learned

* How to use **dictionaries** to store and retrieve key-value pairs efficiently.
* Handling **EOFError** to detect end-of-input (`Ctrl + D`).
* Formatting **floating-point numbers** to two decimal places using f-strings.
* Implementing **case-insensitive input comparison**.
* Designing loops that respond dynamically to user input.

