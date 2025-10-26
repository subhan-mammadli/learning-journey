# 🎯 Guessing Game — CS50P Problem Set 4

## 📘 Problem Description

“I’m thinking of a number between 1 and 100… what is it?”

In this problem, you’ll write a simple **number guessing game** that chooses a random number and lets the user try to guess it.

Your program, **`game.py`**, should:

1. Prompt the user for a **level** (`n`):

   * If the input is **not a positive integer**, ask again.
2. Generate a **random integer** between `1` and `n` (inclusive) using the `random` module.
3. Prompt the user to **guess** the number:

   * If the guess is **not a positive integer**, prompt again.
   * If the guess is **too small**, output `Too small!` and ask again.
   * If the guess is **too large**, output `Too large!` and ask again.
   * If the guess is **just right**, output `Just right!` and end the program.

💡 *Hint:*
The `random` module provides several functions for generating random integers — such as `randint()` and `randrange()`.

---

## 💡 My Explanation

This problem asks us to build a simple **guessing game** using the `random` module.

1. I first created a helper function `get_positive()` to repeatedly prompt the user until they provide a valid **positive integer**.

   * It uses a `while True` loop and handles invalid input with a `try-except` block.

2. Inside the `main()` function:

   * I ask the user for a **level** (upper limit of the random range).
   * Then generate a random integer between `1` and `n` using `random.randint(1, n)`.
   * I start another `while True` loop to repeatedly prompt the user for their **guess**.
   * If the guess is smaller → print **“Too small!”**
   * If larger → print **“Too large!”**
   * If equal → print **“Just right!”** and break the loop.

This structure ensures the game keeps running until the correct number is guessed.

---

## 🧩 Code Implementation

📄 [game.py](./game.py)

---

## 🧪 Example Usage

```
Level: 10
Guess: 7
Too small!
Guess: 9
Too large!
Guess: 8
Just right!
```

---

## 🧠 Key Concepts Learned

* Using the **`random`** library to generate random numbers
* Validating and sanitizing user input with `try` / `except`
* Using **loops (`while True`)** for repeated interaction
* Comparing numerical input and providing feedback
* Breaking out of loops once a condition is met
* Writing clean, modular code with helper functions