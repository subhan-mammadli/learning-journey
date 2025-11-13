# 📂 Problem Set 8 — CS50 Shirtificate

This directory contains my solution to the **CS50 Shirtificate** problem from CS50P.
The assignment involves generating a personalized PDF “shirtificate” inspired by the CS50 community t-shirt, using Python and the **fpdf2** library.

The implementation is located in **[`shirtificate.py`](./shirtificate.py)**.

---

# 👕 Problem Description

The goal of this problem is to write a Python program that automatically creates a **PDF certificate** featuring a CS50 t-shirt design and the user’s name placed on top of the shirt.

Your PDF must include:

* **Portrait** orientation
* **A4** size (210mm × 297mm)
* A centered title at the top: **“CS50 Shirtificate”**
* A centered image of the t-shirt (`shirtificate.png`)
* The user’s name printed **in white text**, placed on top of the shirt

The design does NOT need to match the example perfectly; you are free to customize colors, borders, or styling. Long names do not need line-wrapping.

The final result is saved as **`shirtificate.pdf`**.

---

# 🧠 How the Program Works

The implementation relies on the **FPDF class** from the `fpdf2` library.
Below is an explanation of each major step involved in creating the PDF.

---

## 🏗️ 1. Initializing the PDF

The program begins by creating an instance of `FPDF`, configuring:

* Orientation → `"portrait"`
* Format → `"A4"`

This establishes a blank A4 portrait PDF on which the rest of the design will be built.

---

## ➕ 2. Adding a Page

Before placing any elements, the program calls:

```
add_page()
```

This inserts a fresh page into the PDF document.

FPDF always requires at least one page before adding images or text.

---

## 🖼️ 3. Adding the Shirt Image

The CS50 t-shirt template (`shirtificate.png`) is added using the PDF’s `image` method.

Because the shirt should be centered horizontally, the program adjusts the x/y coordinates appropriately.
(Your own alignment strategy may vary depending on your layout.)

The image effectively becomes the background upon which the user’s name will appear.

---

## 🎨 4. Setting Font and Text Color

The user’s name must appear in **white text** on top of the shirt.
To accomplish this, the program:

* Sets the font to **Helvetica**, bold, size **24**
* Sets the text color to **white** using RGB values `(255, 255, 255)`

These choices ensure the text is readable against the shirt graphic.

---

## ✍️ 5. Positioning the User’s Name

FPDF’s coordinate system begins at the top-left corner of the page.
The program uses:

```
set_xy(x, y)
```

to move the cursor to a position above the shirt graphic.

* `x = 0` aligns the text horizontally to the center when used with `align="C"`
* `y ≈ 70` is typically the correct vertical placement for the overlay text
  (exact values may vary slightly depending on the shirt template)

---

## 📝 6. Writing Text to the PDF

The program draws a full-width text cell:

* Width → automatically spans the page
* Height → used for vertical spacing
* Text → `"<name> took CS50"`
* Alignment → `"C"` for centered

This overlays the user’s name neatly on the shirt.

---

## 📤 7. Exporting the Finished PDF

Finally, the program outputs the file using:

```
output("shirtificate.pdf")
```

This writes the completed shirtificate to your working directory.
You can open it in VS Code or your system’s PDF viewer.

---

# 🧩 File Overview

```
.
├── shirtificate.py
└── shirtificate.png
```

* **[`shirtificate.py`](./shirtificate.py)** contains the full implementation.
* **`shirtificate.png`** is the template shirt image used in the PDF.

---

# ▶️ Usage

Run the program:

```bash
python shirtificate.py
```

When prompted, enter your name, and the program generates:

```
shirtificate.pdf
```

---

# 📦 Dependencies

This program requires the **fpdf2** library:

```bash
pip install fpdf2
```

The official tutorial and API reference are highly recommended:

* Tutorial: [https://py-pdf.github.io/fpdf2/Tutorial.html](https://py-pdf.github.io/fpdf2/Tutorial.html)
* API Docs: [https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF](https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF)

---

# 🎯 Summary

This problem teaches you how to:

✔ Work with external libraries
✔ Manipulate PDFs programmatically
✔ Add images and formatted text
✔ Control coordinates, alignment, and colors
✔ Produce polished, personalized PDF output

The CS50 Shirtificate is a fun and practical introduction to PDF generation in Python.