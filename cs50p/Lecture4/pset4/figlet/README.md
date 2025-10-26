# 🔠 Frank, Ian and Glen’s Letters — CS50P Problem Set 4

## 📘 Problem Description

**FIGlet** (named after *Frank, Ian, and Glen’s letters*) is a program from the early 1990s that creates large, stylized letters made of ASCII characters — a form of **text-based art**:

```
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```

Among the many available fonts, you can explore examples here:
🔗 [figlet.org/examples.html](http://www.figlet.org/examples.html)

The FIGlet program has been ported to Python as the **`pyfiglet`** library.

Your task is to implement a program, **`figlet.py`**, that:

1. Accepts **zero or two command-line arguments**:

   * **Zero arguments** → output text in a random font.
   * **Two arguments** → use a specific font, where:

     * The first argument is `-f` or `--font`.
     * The second argument is the font name.
2. Prompts the user for a string.
3. Outputs that string as ASCII art using the chosen font.

If invalid arguments are provided (for example, an incorrect flag or unknown font name), the program should exit using `sys.exit()` with an error message.

---

## 💡 My Explanation

In this problem, we use the **`pyfiglet`** library to generate ASCII art from regular text.

We also import:

* `sys` → for accessing command-line arguments (`argv`) and exiting with `sys.exit()`.
* `random.choice()` → to randomly select a font when none is specified.

Here’s the step-by-step logic behind the solution:

1. **Import necessary modules:**

   * `Figlet` class from `pyfiglet`
   * `exit` and `argv` from `sys`
   * `choice` from `random`

2. **Initialize FIGlet:**

   * Create an instance of `Figlet()` and store it in a variable named `figlet`.
   * Retrieve all available fonts using `figlet.getFonts()`.

3. **Define a helper function `get_font()`:**

   * If no command-line arguments are given → return a **random font**.
   * If `-f` or `--font` is provided → check if the next argument is a valid font name.

     * If valid, return it.
     * Otherwise, exit with `"Invalid usage"`.
   * If none of these cases apply → exit with `"Invalid usage"`.

4. **Main program logic:**

   * Call `get_font()` to determine which font to use.
   * Prompt the user for input text.
   * Set the font using `figlet.setFont(font=font)`.
   * Render and print the text as ASCII art using `figlet.renderText()`.

---

## 🧩 Code Implementation

📄 [figlet.py](./figlet.py)

---

## 🧪 Example Usage

### 🎲 Random Font Example

```bash
$ python figlet.py
Input: CS50P
```

*Output (example):*

```
  ____ ____  ____  ____  
 / ___/ ___||  _ \/ ___| 
| |   \___ \| |_) \___ \ 
| |___ ___) |  __/ ___) |
 \____|____/|_|   |____/ 
```

---

### 🎨 Specific Font Example

```bash
$ python figlet.py -f slant
Input: Python
```

*Output:*

```
   ____        _   _             
  / __ \ _   _| |_| |__   ___    
 / / _` | | | | __| '_ \ / _ \   
| | (_| | |_| | |_| | | |  __/   
 \ \__,_|\__,_|\__|_| |_|\___|   
  \____/                          
```

---

## 🧠 Key Concepts Learned

* Working with **command-line arguments** using `sys.argv`
* Using **conditional logic** to handle program arguments and errors
* Generating **ASCII art** with `pyfiglet`
* Importing **specific functions or classes** (`from ... import ...`)
* Combining multiple modules (`sys`, `random`, `pyfiglet`) for more dynamic programs
* Exiting gracefully with **`sys.exit()`** upon invalid usage