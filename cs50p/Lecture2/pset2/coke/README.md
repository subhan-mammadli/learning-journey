# 🥤 Coke Machine

This program simulates a **Coca-Cola vending machine** that accepts specific coins and provides change when the required amount is reached.

---

## 🧩 Problem Description

The machine sells **one bottle of Coke for 50 cents** and only accepts coins in the following denominations:

```
25¢, 10¢, 5¢
```

Your program should:

1. Continuously prompt the user to **insert a coin**, one at a time.
2. After each valid coin, display the **remaining amount due**.
3. Once the total inserted amount is **at least 50¢**, print how many cents in **change** the user is owed.
4. Ignore any invalid coin denominations.

🧠 **Task:**
Implement this vending machine logic in `coke.py` using loops, conditionals, and simple arithmetic.

---

## 💡 Approach

1. Start with `amount_due = 50` to represent the cost of a Coke.
2. Use a `while True` loop to keep asking the user for coins until the full amount is paid.
3. Store the accepted coin values in a list for easy validation.
4. Subtract each valid coin from `amount_due`.
5. If the total reaches or exceeds 0, the program stops and displays how much **change** is owed.
6. Use `abs()` to handle negative values safely when printing the change amount.

---

## 🧠 Example

**Input & Output Flow:**

```
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 25
Change Owed: 10
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**coke.py**](./coke.py)

---

## ✅ What I Learned

* Using **while loops** for continuous user input.
* Validating user input against a set of accepted values.
* Performing **incremental subtraction** to track remaining amount.
* Handling **negative numbers** and change calculation with `abs()`.
* Designing a user-friendly CLI interaction with clear prompts.