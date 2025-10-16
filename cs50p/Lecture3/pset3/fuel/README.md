⛽ Fuel Gauge

This program simulates a fuel gauge, converting a user-inputted fraction (e.g., 1/2) into a percentage that represents how full a tank is.


---

🧩 Problem Description

Fuel gauges often display the amount of fuel in a tank as a fraction.
For example:

1/4 → 25% full

1/2 → 50% full

3/4 → 75% full


Your task is to write a program that:

1. Prompts the user for a fraction in the format X/Y, where both X and Y are positive integers.


2. Converts that fraction into a percentage, rounded to the nearest integer.


3. Displays:

E if 1% or less remains (essentially empty).

F if 99% or more remains (essentially full).

Otherwise, prints the calculated percentage followed by %.




If the input is invalid (e.g., X or Y is not an integer, Y is 0, or X > Y), the user should be prompted again.


---

💡 Approach

1. Main logic (main()):

Calls get_fraction() to obtain a valid fuel percentage.

Compares the integer value of the fraction to determine whether to display E, F, or the percentage itself.



2. Input handling (get_fraction()):

Continuously prompts the user until valid input is provided.

Splits the user input ("X/Y") using .split("/") to extract x and y.

Converts both to integers inside a try block to catch ValueError.

Uses conditionals to ensure:

x ≤ y

y > 0

x ≥ 0


If input is valid, converts the fraction to a percentage using:

x * 100 / y

and returns the result formatted without decimal places (:.0f).



3. Error Handling:

ValueError → raised if input can’t be converted to integers (e.g., letters instead of numbers).

ZeroDivisionError → avoided by explicitly checking y > 0.





---

🧠 Example

Input:

Fraction: 3/4

Output:

75%

Input:

Fraction: 1/100

Output:

E

Input:

Fraction: 100/100

Output:

F


---

📄 Source File

You can view the full implementation here:
➡️ fuel.py


---

✅ What I Learned

Parsing and validating user input using try / except.

Handling ValueError and ZeroDivisionError safely.

Using loops to re-prompt until valid data is entered.

Formatting numeric output using Python f-strings.

Applying logical conditions to simulate a real-world gauge system.


