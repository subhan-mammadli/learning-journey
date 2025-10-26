# 👋 Adieu, Adieu — CS50P Problem Set 4

## 📘 Problem Description

In *The Sound of Music*, there’s a famous farewell song — **“So Long, Farewell”** — featuring the line:

```
Adieu, adieu, to yieu and yieu and yieu
```

Of course, grammatically it should be written (with an Oxford comma) as:

```
Adieu, adieu, to yieu, yieu, and yieu
```

In this problem, you’ll simulate that lyric pattern by writing a program, **`adieu.py`**, which:

1. Prompts the user for names, one per line.
2. Stops taking input when the user presses **Ctrl-D** (end-of-file).
3. Outputs a line that bids *“adieu”* to all the entered names, using proper grammar:

   * Two names: joined with **“and”**
   * Three or more names: separated with commas and a final **“and”**

Example output:

```
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
```

---

## 💡 My Explanation

In this problem, we simulate the song’s farewell phrase by collecting a list of names from the user, then grammatically joining them in a sentence.

To handle proper English grammar (like commas and *“and”* placement), we use the **`inflect`** library — which provides functions for creating human-readable phrases.

Here’s the main logic:

1. Import and initialize **`inflect`** with `inflect.engine()`.
2. Continuously prompt the user for names using a `while True` loop.
3. Stop the loop gracefully when the user triggers **EOFError** (Ctrl-D).
4. Store all entered names in a list called `names`.
5. Use `p.join(names)` to automatically join the names correctly (e.g., `"A, B, and C"`).
6. Print the final message using an f-string:

   ```
   Adieu, adieu, to {joined_names}
   ```

---

## 🧩 Code Implementation

📄 [adieu.py](./adieu.py)

---

## 🧪 Example Usage

```
Name: Liesl
Name: Friedrich
Name: Louisa
Name: Kurt
Name: Brigitta
Name: Marta
Name: Gretl
^D
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
```

---

## 🧠 Key Concepts Learned

* Reading **multiple lines of input** until end-of-file (`EOFError`)
* Using **lists** to store user input dynamically
* Employing the **`inflect`** library for natural language formatting
* Gracefully handling user termination (`Ctrl-D`)
* Building output strings using **f-strings** and logical joining