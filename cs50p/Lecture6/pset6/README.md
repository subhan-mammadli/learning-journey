# 📂 Problem Set 6 — CS50P

This folder contains my solutions for **CS50’s Introduction to Programming with Python — Problem Set 6**.
Each problem is located in its own directory and includes a dedicated `README.md` explaining the task, logic, and implementation details.

---

## 📌 Problems

* 🔹 **[Lines of Code](./lines/README.md)**
  Counts how many actual lines of code exist in a `.py` file, excluding blank lines and comments.

* 🔹 **[Pizza Py](./pizza/README.md)**
  Reads pizza menu data from a CSV file and prints a clean ASCII table using the `tabulate` library.

* 🔹 **[Scourgify](./scourgify/README.md)**
  Cleans messy CSV data by splitting combined full names into separate first and last name columns.

* 🔹 **[CS50 P-Shirt](./shirt/README.md)**
  Uses Pillow to overlay a CS50 shirt image onto a user-supplied photo, resizing and fitting it automatically.

---

## 📚 What I Learned

* Working with **CSV files**, including:

  * Reading with `csv.reader` & `csv.DictReader`
  * Writing clean data using `csv.writer` & `csv.DictWriter`
  * Converting messy datasets into structured formats

* Manipulating images using the **Pillow (PIL)** library:

  * Opening, resizing, cropping, and overlaying images
  * Handling transparency and saving results

* Using **command-line arguments** with `sys.argv`

  * Validating input files, file extensions, and error handling
  * Exiting programs safely using `sys.exit`

* Proper error handling:

  * Detecting invalid usage
  * Catching missing files with `FileNotFoundError`

---

## ✅ Required Tools

Install the libraries used in some of the problems:

```bash
pip install tabulate pillow
```

---

## 🚀 How to Run Each Program

Example:

1. Navigate to a problem folder:

   ```bash
   cd pizza
   ```

2. Run the script, providing required arguments:

   ```bash
   python pizza.py sicilian.csv
   ```

For programs that take two arguments, such as **Scourgify** or **P-Shirt**:

```bash
python scourgify.py before.csv after.csv
python shirt.py before.jpg after.jpg
```

---

> ✅ **Tip:**
> Problem Set 6 connects data processing and automation with real-world tools.
> From cleaning CSV files to editing images, these exercises build essential skills for backend development, scripting, and data handling.