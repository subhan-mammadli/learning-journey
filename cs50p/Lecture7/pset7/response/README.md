# ✅ Response Validation

**CS50P – Problem Set 7**

When building forms—especially on platforms like Google Forms—it’s common to validate user input. One typical requirement is making sure the user provides a **properly formatted email address**.

In this problem, we implement a command-line program that asks the user for an email address and reports whether it is syntactically valid.

---

## ✅ Goal

Inside **`response.py`**, write a program that:

✔ Prompts the user for an email address
✔ Uses a third-party validation library (not `re`)
✔ Prints `"Valid"` if the email is properly formatted
✔ Prints `"Invalid"` otherwise

> ❗ The program **should not** check whether the domain actually exists — only whether the email is syntactically valid.

---

## ✅ Allowed Libraries

You must use **one** of these from PyPI:

| Library                | Install command                    |
| ---------------------- | ---------------------------------- |
| `validator-collection` | `pip install validator-collection` |
| `validators`           | `pip install validators`           |

Either is acceptable.
In this solution, the `validators` library is used.

➡️ Implementation:
📄 [`response.py`](./response.py)

---

## ✅ How It Works

The `validators` library includes a built-in function:

```
validators.email(s)
```

* Returns `True` if `s` is a syntactically valid email
* Returns `False` otherwise

The program simply calls this function and prints the correct output.

Example behavior:

| Input                      | Output    |
| -------------------------- | --------- |
| `user@example.com`         | `Valid`   |
| `user@com`                 | `Invalid` |
| `hello`                    | `Invalid` |
| `john_doe@mail-server.org` | `Valid`   |

---

## ✅ What This Problem Teaches

* Installing and using external Python packages
* Basic input validation
* Separating logic into helper functions
* Avoiding regex by delegating validation to a library