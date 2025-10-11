# 🐍 camelCase → snake_case

This program converts a variable name from **camelCase** to **snake_case**, following Python’s naming conventions.

---

## 🧩 Problem Description

In some programming languages, **camel case** (also known as *mixed case*) is used for variable names that consist of multiple words.
The first word starts with a lowercase letter, and each subsequent word starts with an uppercase letter.

Examples:

```
firstName
preferredFirstName
```

In Python, however, the recommended style is **snake case**, where words are separated by underscores (`_`) and all letters are lowercase:

```
first_name
preferred_first_name
```

🧠 **Task:**
Implement a program that:

1. Prompts the user for a variable name in **camelCase**.
2. Converts it to **snake_case**.
3. Prints the result.

You can assume that the input will always be a valid camelCase string.

---

## 💡 Approach

1. Use `input()` to get a camelCase variable name from the user.
2. Copy the input into another variable for modification.
3. Iterate through each character:

   * If it’s **uppercase** (and not the first character),
     insert an underscore (`_`) before it.
4. Convert the entire string to lowercase using `.lower()`.
5. Print the final snake_case version.

---

## 🧠 Example

**Input:**

```
camelCase: firstName
```

**Output:**

```
snake_case: first_name
```

---

## 📄 Source File

You can view the full implementation here:
➡️ [**camel.py**](./camel.py)

---

## ✅ What I Learned

* Iterating through strings character by character.
* Detecting uppercase letters using `.isupper()`.
* Performing text transformations with `.replace()` and `.lower()`.
* Understanding the difference between **camelCase** and **snake_case** naming styles.
