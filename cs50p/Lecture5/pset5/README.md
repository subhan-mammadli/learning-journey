# 📂 Problem Set 5 — CS50P

This folder contains my solutions for **CS50’s Introduction to Programming with Python — Problem Set 5**.
Each problem is stored in its own subdirectory with a dedicated `README.md` explaining the task, logic, and implementation details.

---

## 📌 Problems

* 🔹 [Testing my twttr](./test_twttr/README.md)
  Writing automated tests to verify the correctness of a function that removes vowels from text.

* 🔹 [Back to the Bank](./test_bank/README.md)
  Using unit tests to check string behavior, input validation, and correct return values.

* 🔹 [Re-requesting a Vanity Plate](./test_plates/README.md)
  Expanding test coverage to ensure edge cases are handled properly when validating license plates.

* 🔹 [Refueling](./test_fuel/README.md)
  Testing functions that convert fuel fractions to percentages and verifying correct error handling with `pytest.raises`.

---

## 📚 What I Learned

* Writing **unit tests** to ensure code stability and correctness.
* Using the **pytest** framework for automated testing.
* Creating structured test files like `test_*.py` for better project organization.
* Using the `assert` keyword to validate function output.
* Testing error handling using **`pytest.raises`** to confirm that functions raise the correct exceptions.
* Structuring a project as a **Python package** with `__init__.py` and multiple test modules.
* Developing cleaner, safer programs by catching edge cases and invalid input.

---

## ✅ Required Tools

To test the solutions, install pytest:

```bash
pip install pytest
```

---

## 🚀 How to Run Tests

1. Navigate to a problem directory:

   ```bash
   cd twttr
   ```

2. Run its tests:

   ```bash
   pytest
   ```

Or run all tests for the entire Problem Set:

```bash
pytest ..
```

Use verbose mode for detailed output:

```bash
pytest -v
```

---

> ✅ **Tip:** Automated testing makes debugging easier and prevents mistakes from hiding in your code. Even small functions become more reliable when backed by proper test coverage.