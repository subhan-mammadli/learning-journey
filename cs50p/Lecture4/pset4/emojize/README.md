# 😀 Emojize — CS50P Problem Set 4

## 📘 Problem Description

Because emojis aren’t as easy to type as regular text (especially on laptops and desktops), some programs support **emoji codes** — for example, typing `:thumbs_up:` will automatically be converted to 👍.

Some programs also support **aliases**, allowing you to type shorter versions like `:thumbsup:` to produce the same emoji.

In this problem, you’ll implement a program called **`emojize.py`** that:

1. Prompts the user for a string in English.
2. Converts any emoji codes or aliases in the string to their corresponding emojis.
3. Prints the emojized version of the text.

You can see the full list of supported emoji codes and aliases here:
🔗 [carpedm20.github.io/emoji/all.html](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias)

---

## 💡 My Explanation

In this problem, we use the **`emoji`** library to automatically convert words written between colons (`:`) into real emojis.

We only need the **`emojize()`** function from this library, so instead of importing the whole module, we import just that function with `from`.

* The program first asks the user for input text.
* Then it passes that input to `emojize()`.
* The `language='alias'` argument allows the program to recognize **both** standard emoji codes (`:thumbs_up:`) **and** their shorter aliases (`:thumbsup:`).
* Finally, the program prints the converted (emojized) output.

---

## 🧩 Code Implementation

📄 [emojize.py](./emojize.py)

---

## 🧪 Example Usage

```
Input: I love Python :snake:
Output: I love Python 🐍
```

```
Input: That’s great :thumbsup:
Output: That’s great 👍
```

---

## 🧠 Key Concepts Learned

* Importing specific functions using `from ... import ...`
* Using third-party libraries installed via `pip`
* Handling **text replacement and Unicode emoji conversion**
* Understanding how **function arguments** (like `language='alias'`) modify behavior