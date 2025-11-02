# 🍕 Pizza Py — Problem Set 6 (CS50P)

Pinocchio’s Pizza & Subs (“Noch’s”) is famous in Harvard Square for its Sicilian deep-dish pizza. Students often buy slices, but the menu also includes whole pizzas, listed in CSV files such as **`sicilian.csv`** and **`regular.csv`**.

While CSV is useful for computers, it’s not very readable for customers. A clean, well-formatted ASCII table would look much better, like this:

```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
```

---

## ✅ Goal

In a file called **`pizza.py`**, write a program that:

1. Expects **exactly one command-line argument** — the name/path of a CSV file
2. Validates that:

   * One argument is provided
   * The file ends in `.csv`
   * The file exists
3. Reads the CSV file and loads its rows into a table-like structure
4. Uses the **`tabulate`** library to print the data as an ASCII table in **grid** format

If any requirement is violated, the program should exit using **`sys.exit`** with an appropriate error message.

---

## ✅ How the Program Works

The logic inside **`pizza.py`** follows these steps:

1. **Validate arguments**

   * No argument → “Too few command-line arguments”
   * More than one argument → “Too many command-line arguments”
   * File does not end in `.csv` → “Not a CSV file”

2. **Read the CSV**

   * Open the file safely inside a `try` block
   * Use `csv.reader` to parse rows into a list
   * Store each row (pizza name, small price, large price)

3. **Format using `tabulate`**

   * Provide the list of rows
   * Tell `tabulate` to use the first row as column headers
   * Output the table in `"grid"` format

See the full implementation here →
➡️ **[`pizza.py`](./pizza.py)**

---

## ✅ Required Libraries

This program uses:

* ✅ `csv` (built-in)
* ✅ `tabulate` (third-party)

Install `tabulate` with:

```bash
pip install tabulate
```

---

## ✅ Example Usage

If `sicilian.csv` contains:

```
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
```

Running:

```
$ python pizza.py sicilian.csv
```

Will output a clean ASCII table similar to:

```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
| 1 item           | $27.50  | $41.95  |
```

---

## ✅ Common Errors Handled

| Situation                       | Behavior                         |
| ------------------------------- | -------------------------------- |
| No command-line argument        | Exits with error                 |
| Too many arguments              | Exits with error                 |
| Filename does not end in `.csv` | Exits with error                 |
| File does not exist             | Exits with `File does not exist` |

---

## ✅ Files Included

| File           | Purpose                                        |
| -------------- | ---------------------------------------------- |
| **`pizza.py`** | Reads a CSV and prints a formatted ASCII table |
| `sicilian.csv` | Sample data                                    |
| `regular.csv`  | Sample data (optional test)                    |

---

> ✅ **Takeaway:** This problem reinforces file handling, CSV parsing, defensive programming, and working with external Python packages. It also demonstrates how Python can transform raw data into user-friendly output.