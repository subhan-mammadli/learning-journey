# 🧮 Little Professor — CS50P Problem Set 4

## 📘 Problem Description

When David was a child, one of his first “toys” was the **Little Professor**, a calculator-like device that generated simple math problems for kids to solve.
If the toy displayed `4 + 1 =`, the correct answer would be 5; if answered incorrectly, it would show **EEE**.
After **three wrong attempts**, it displayed the correct answer.

Your task is to implement a program, **`professor.py`**, that simulates this toy:

1. Prompts the user for a **level (1, 2, or 3)**

   * If the input is invalid, prompt again.
2. Generates **10 random addition problems**, each with numbers that have *n* digits depending on the level:

   * Level 1 → single-digit numbers (0 – 9)
   * Level 2 → two-digit numbers (10 – 99)
   * Level 3 → three-digit numbers (100 – 999)
3. For each problem:

   * Prompt the user for the answer.
   * If the answer is incorrect or invalid, print **EEE**.
   * Allow **up to 3 tries** per problem.
   * After 3 wrong attempts, display the correct answer.
4. At the end, output the user’s **final score** (out of 10).

Program structure suggested by CS50P:

```python
import random

def main():
    ...

def get_level():
    ...

def generate_integer(level):
    ...

if __name__ == "__main__":
    main()
```

---

## 💡 My Explanation

This program reproduces the *Little Professor* toy’s logic.

1. **`get_level()`**

   * Uses a `while True` loop and `try/except` to ensure a valid input.
   * Only accepts 1, 2, or 3.
   * Returns the chosen level.

2. **`generate_integer(level)`**

   * Uses a `match-case` structure (Python 3.10+) to choose number ranges:

     * Level 1 → `randint(0, 9)`
     * Level 2 → `randint(10, 99)`
     * Level 3 → `randint(100, 999)`

3. **`main()`**

   * Calls `get_level()` to set the level.
   * Initializes `score = 0`.
   * Runs a loop 10 times to generate 10 problems.
   * For each problem:

     * Generates two random numbers `x` and `y`.
     * Calculates `answer = x + y`.
     * Gives the user up to 3 tries:

       * If the input is invalid → print **EEE** and retry.
       * If the answer is wrong → print **EEE** again.
       * If correct → increment score and break.
     * Uses a `for ... else` block — the `else` executes if the loop ends without `break`, meaning 3 failed attempts, so the correct answer is printed.
   * After all 10 questions, prints the final `Score`.

---

## 🧩 Code Implementation

📄 [professor.py](./professor.py)

---

## 🧪 Example Usage

```
Level: 2
41 + 73 = 115
EEE
41 + 73 = 114
EEE
41 + 73 = 113
EEE
41 + 73 = 114
EEE
41 + 73 = 114
EEE
41 + 73 = 114
EEE
41 + 73 = 114
EEE
41 + 73 = 114
EEE
41 + 73 = 114
EEE
Score: 6
```

(Example above illustrates wrong attempts and final score display.)

---

## 🧠 Key Concepts Learned

* Validating and sanitizing user input
* Working with **loops** and **nested control structures**
* Using **`for ... else`** to detect unsuccessful attempts
* Generating **random numbers** based on level logic
* Handling **exceptions** (`ValueError`) for robust user interaction
* Combining multiple functions into a structured program
* Implementing **score tracking** and user feedback