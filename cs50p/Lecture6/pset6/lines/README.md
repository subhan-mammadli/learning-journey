# 🧮 Lines of Code — Problem Set 6 (CS50P)

In this exercise, the goal is to write a program that counts how many *actual* lines of code exist in a Python file. Instead of counting every physical line, the program ignores:

✅ Blank lines
✅ Comment-only lines (lines starting with `#`, even if they have leading spaces)

This helps estimate a program’s size or complexity more accurately than simply counting raw lines.

---

## ✅ Problem Description

In a file called **`lines.py`**, implement a program that:

1. Expects **exactly one command-line argument** — the name or path of a `.py` file
2. Validates that:

   * A file name was provided
   * Only one argument was given
   * The file name ends with `.py`
   * The file actually exists
3. Opens the file and counts lines of *real* code, ignoring:

   * Lines that contain only whitespace
   * Lines that start with `#` (after optionally stripping leading spaces)

Finally, the program should print the total number of valid code lines.

If any requirement is violated, the program must exit using `sys.exit`.

---

## ✅ How the Program Works

The logic behind **`lines.py`** is straightforward:

1. **Validate command-line arguments**

   * If no argument or too many arguments → exit
   * If the filename does not end in `.py` → exit
   * If the file cannot be opened (missing or invalid path) → exit

2. **Read the file line-by-line**

   * Strip whitespace from each line
   * Skip the line if it's empty (`""`)
   * Skip the line if it starts with `#`

3. **Count all remaining lines**

   * Those are considered actual lines of code

4. **Output the final count**

See the full implementation here:
➡️ **[`lines.py`](./lines.py)**

---

## ✅ Example

Consider this file:

```python
# Say hello

name = input("What's your name? ")
print(f"hello, {name}")
```

Although it contains 4 physical lines, only **2** of them are real code lines.
Your program should correctly output:

```
2
```

---

## ✅ Hints & Notes

* `str.lstrip()` and `str.startswith()` are useful for detecting comments
* `readlines()` can help iterate over file contents
* Try testing your script on:

  * Files from Week 6’s lectures
  * Your own small Python programs
* Be sure to catch `FileNotFoundError` when opening the file

---

## ✅ Files Included

| File           | Purpose                                           |
| -------------- | ------------------------------------------------- |
| **`lines.py`** | The main program that counts actual lines of code |

---

> 🧠 **Takeaway:**
> This exercise reinforces command-line arguments, defensive programming, file I/O, and basic parsing. It also demonstrates why raw line count does not always reflect a program’s real complexity.