# ✨ Scourgify — Problem Set 6 (CS50P)

Just like Tonks’s cleaning spell *“Scourgify”*, data often needs a bit of cleaning too.
In this problem, the goal is to take messy CSV data and reformat it into a cleaner, more useful structure.

---

## ✅ Problem Description

You are given a CSV file (e.g., `before.csv`) containing Hogwarts students:

```csv
name,house
"Granger, Hermione",Gryffindor
"Diggory, Cedric",Hufflepuff
"Malfoy, Draco",Slytherin
...
```

Each student’s full name is stored in one column in the format:

```
"Last, First"
```

This is inconvenient if Hogwarts wants to generate personalized letters like:

```
Dear Hermione,
```

instead of:

```
Dear Granger, Hermione,
```

---

## ✅ Goal

In a file called **`scourgify.py`**, write a program that:

✔ Expects **two** command-line arguments:

1. The input CSV file to read (`before.csv`)
2. The output CSV file to write (`after.csv`)

✔ Converts each row so that names are split into separate fields:

| Input Columns | Output Columns     |
| ------------- | ------------------ |
| name, house   | first, last, house |

✔ Writes the cleaned data to the new CSV file using `csv.DictWriter`

✔ Writes a header row: `first,last,house`

If the user:

* does not provide exactly two arguments, or
* the input file cannot be opened

→ the program must exit using `sys.exit` with an appropriate error message.

See the full implementation here:
➡️ **[`scourgify.py`](./scourgify.py)**

---

## ✅ How the Program Works

The logic in `scourgify.py` follows these steps:

1. **Check command-line arguments**

   * Too few → exit with error
   * Too many → exit with error

2. **Open the input CSV**

   * Use `csv.DictReader` so each row becomes a dictionary like:

     ```python
     {"name": "Granger, Hermione", "house": "Gryffindor"}
     ```

3. **Create the output CSV**

   * Open the second file in write mode
   * Use `csv.DictWriter` with fields: `first`, `last`, `house`
   * Call `writeheader()` to write the column names to the file

4. **Split each name**

   * Use `.split(",")` to separate last name and first name
   * Strip whitespace from the first name
   * Write cleaned data to the output file

5. **Handle missing file errors**

   * Wrap file opening in a `try-except`
   * If file does not exist → exit with an error

---

## ✅ Example

**before.csv**

```csv
name,house
"Potter, Harry",Gryffindor
"Malfoy, Draco",Slytherin
```

**Run:**

```
$ python scourgify.py before.csv after.csv
```

**after.csv**

```csv
first,last,house
Harry,Potter,Gryffindor
Draco,Malfoy,Slytherin
```

---

## ✅ Useful Notes

* `csv.DictReader` reads each row into a dictionary automatically
* `csv.DictWriter` can write rows as dictionaries
* `.writeheader()` writes the column names without needing extra code
* Splitting names is simple:

  ```python
  last, first = name.split(",")
  first = first.strip()
  ```

---

## ✅ Files Included

| File               | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| **`scourgify.py`** | Cleans CSV data and rewrites it with separate name fields |
| `before.csv`       | Sample messy input file                                   |
| `after.csv`        | Output produced by the program                            |

---

> ✅ **Takeaway:**
> This challenge practices working with CSV files, defensive programming, string parsing, and writing structured data. It introduces real-world skills used in data cleaning, automation, and back-end processing.