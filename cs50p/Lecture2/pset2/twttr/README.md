# 🐦 Just setting up my twttr

This program removes all **vowels** from a user-provided text, imitating how words are often shortened on social media platforms like Twitter.

---

## 🧩 Problem Description

When texting or tweeting, it’s common to shorten words by **omitting vowels** to save time or space — just like how “Twitter” was originally called **“twttr.”**

Your task is to write a program that:

1. Prompts the user for a line of text.
2. Outputs that same text but with **all vowels (A, E, I, O, U)** removed.
3. Handles both uppercase and lowercase vowels.

---

## 💡 Approach

1. Use `input()` to get a string from the user.
2. Copy the input into another variable to modify safely.
3. Create a list of vowels (both uppercase and lowercase).
4. Loop through each character in the text:

   * If the character is a vowel, remove it using `.replace()`.
5. Finally, print the result without vowels.

---

## 🧠 Example

**Input:**

```
Input: Twitter
```

**Output:**

```
Output: Twttr
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**twttr.py**](./twttr.py)

---

## ✅ What I Learned

* Handling **strings and loops** in Python.
* Using `.replace()` to remove specific characters from text.
* Creating and using **lists** to store multiple values (vowels).
* Working with **case sensitivity** by checking both uppercase and lowercase vowels.
* Understanding simple **text transformation logic**.