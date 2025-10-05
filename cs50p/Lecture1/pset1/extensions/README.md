# 📄 Problem Set 1 – File Extensions

## 🧠 Problem Description

In this problem, you are asked to write a program that determines the **MIME type** of a file based on its **extension**.

When the user enters a file name, the program should identify what type of file it is and print the corresponding **media type** (e.g., `"image/jpeg"`, `"text/plain"`, etc.).

If the program doesn’t recognize the file extension, it should default to:

```
application/octet-stream
```

---

## ⚙️ Implementation Details

1. **Get input** from the user:

   ```python
   file = input("File name: ")
   ```
2. **Normalize** the input to avoid case or spacing issues:

   * `.lower()` — makes the comparison case-insensitive
   * `.strip()` — removes leading and trailing spaces
3. **Check the file extension** using the `.endswith()` method.
4. **Map** the extension to its corresponding MIME type with `if`, `elif`, `else`.

---

## 💻 Solution

👉 You can find the full implementation here:
[`extensions.py`](./extensions.py)

---

## 🧩 Example Runs

```
$ python extensions.py
File name: cat.jpg
image/jpeg
```

```
$ python extensions.py
File name: document.PDF
application/pdf
```

```
$ python extensions.py
File name: archive.zip
application/zip
```

```
$ python extensions.py
File name: unknownfile.xyz
application/octet-stream
```

---

## 🧩 Supported File Types

| Extension       | MIME Type                  |
| --------------- | -------------------------- |
| `.jpg`, `.jpeg` | `image/jpeg`               |
| `.png`          | `image/png`                |
| `.gif`          | `image/gif`                |
| `.txt`          | `text/plain`               |
| `.pdf`          | `application/pdf`          |
| `.zip`          | `application/zip`          |
| *(other)*       | `application/octet-stream` |

---

## 💡 Notes

* The `.endswith()` method is ideal for checking multiple possible suffixes.
* `.lower()` ensures the extension check is **case-insensitive**.
* `.strip()` prevents extra spaces from causing false mismatches.
* This problem reinforces string manipulation, conditional logic, and user input handling.
