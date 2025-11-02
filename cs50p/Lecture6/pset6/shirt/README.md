# 👕 CS50 P-Shirt — Problem Set 6 (CS50P)

After completing CS50, Harvard students traditionally receive the famous **“I took CS50”** t-shirt.
In this problem, you’ll create a virtual version of that tradition by overlaying a CS50 shirt onto a photo.

---

## ✅ Problem Description

In a file called **`shirt.py`**, write a program that:

1. Expects **exactly two command-line arguments**:

   * `sys.argv[1]` → the input image (JPEG or PNG)
   * `sys.argv[2]` → the output image (JPEG or PNG)

2. The program should:

   * Open the input image using `Image.open`
   * Resize and crop it to match the size of `shirt.png` using `ImageOps.fit`
   * Overlay `shirt.png` (which has transparency) onto the resized image using `paste`
   * Save the final result using `Image.save`

3. The program must exit via `sys.exit` if:

   * Too few or too many command-line arguments are provided
   * Input and output do **not** both end in `.jpg`, `.jpeg`, or `.png`
   * The extensions don’t match
   * The input file does not exist

Full implementation is here:
➡️ **[`shirt.py`](./shirt.py)**

---

## ✅ How the Program Works

Inside **`shirt.py`**, the logic follows these steps:

1. **Validate arguments**

   * Ensure exactly 2 arguments are provided
   * Extract the file extensions and confirm they are supported (`.jpg`, `.jpeg`, `.png`)
   * Confirm both files have the **same** extension (input → output)

2. **Open the images**

   * Load the input with `Image.open`
   * Load `shirt.png` which already exists in the same directory
   * Wrap opening the input image in `try-except` so a missing image raises `"Input does not exist"`

3. **Resize & crop**

   * Get the shirt’s dimensions using `.size`
   * Use `ImageOps.fit(input_image, size)` to resize the photo so it matches exactly

4. **Overlay the shirt**

   * Use `.paste(shirt, (0,0), shirt)`
     The third argument ensures transparency is handled correctly

5. **Save**

   * Save the result to the filename provided in `sys.argv[2]`

---

## ✅ Example Usage

```
$ python shirt.py before.jpg after.jpg
```

If the input image exists, the program produces an edited image where the shirt appears perfectly fitted.

---

## ✅ Common Errors Handled

| Scenario                | Program Output                               |
| ----------------------- | -------------------------------------------- |
| No arguments            | `Too few command-line arguments`             |
| More than two arguments | `Too many command-line arguments`            |
| Unsupported extension   | `Invalid output`                             |
| Extensions don’t match  | `Input and output have different extensions` |
| Input file missing      | `Input does not exist`                       |

---

## ✅ Required Image Files

| File                                       | Purpose                           |
| ------------------------------------------ | --------------------------------- |
| **`shirt.png`**                            | The transparent t-shirt overlay   |
| Your input image (`.jpg`, `.jpeg`, `.png`) | The picture being edited          |
| Output image                               | Final image saved by your program |

If testing with CS50's sample photos:

```
wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
unzip muppets.zip
```

---

## ✅ Files Included

| File           | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| **`shirt.py`** | The main program that overlays a CS50 shirt onto an image |

---

> ✅ **Takeaway:**
> This problem practices file validation, exception handling, image manipulation with Pillow, and proper use of command-line arguments — valuable skills for automation, web development, and digital media applications.