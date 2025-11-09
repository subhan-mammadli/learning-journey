# 📘 CS50P — Lecture 7 Notes

## ✅ Regular Expressions (Regex)

In this lecture, we learned how to use **Regular Expressions (Regex)** in Python with the `re` module.  
Regex allows us to **search, validate, extract, replace, and split** text based on patterns — very useful for validating emails, URLs, phone numbers, dates, and many other formats.

---

## ✅ A Simple Email Check (Without Regex)

```python
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username:
    print("Valid")
else:
    print("Invalid")
```

- If `username` is not empty → `Valid`
    
- If empty → `Invalid`
    

But this code has problems:

- `malan@@@harvard.edu` will break `.split("@")`
    
- It does not check if the domain is correct
    
- It accepts many invalid formats
    

➡️ That’s why we use **Regex** ✅

---

# ✅ The `re` Module

```python
import re
```

### ✔ `re.search(pattern, string)`

Searches for a match **anywhere** in the string.

```python
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
```

Still very weak — it only checks if `@` exists.

---

# ✅ Basic Regex Symbols

|Symbol|Meaning|Example|
|---|---|---|
|`.`|Any character (except newline)|`a.c` → `abc`, `a!c`|
|`*`|0 or more repetitions|`a*` → `""`, `"a"`, `"aaaa"`|
|`+`|1 or more repetitions|`a+` → `"a"`, `"aaa"`|
|`?`|0 or 1 repetition|`a?` → `""` or `"a"`|
|`{m}`|exactly m times|`a{3}` → `"aaa"`|
|`{m,n}`|between m and n times|`a{2,4}` → `"aa"`, `"aaa"`, `"aaaa"`|

---

# ✅ Email Validation Example

```python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
```

❌ Still incorrect:

✔ `malan@harvard.edu`  
❌ `malan@@@harvard.edu` (still valid)  
❌ `My email is malan@harvard.edu.` (still valid)

Because:

- `.` matches ANY character
    
- pattern can appear anywhere
    

---

# ✅ Anchors: `^` and `$`

|Symbol|Meaning|
|---|---|
|`^`|Start of string|
|`$`|End of string|

```python
import re

if re.search("^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

✅ Now the pattern must match the **entire** string.

---

## ✅ Character Sets — `[]`

|Pattern|Meaning|
|---|---|
|`[abc]`|a or b or c|
|`[a-z]`|a to z|
|`[A-Z]`|A to Z|
|`[0-9]`|digits|
|`[^...]`|NOT inside brackets|

Example:

```python
"^[^@]+@[^@]+\.edu$"
```

✔ Characters that are not `@`  
✔ Then one `@`  
✔ Then characters not `@`  
✔ Ends with `.edu`

Now: `malan@@@harvard.edu` → **Invalid ✅**

---

# ✅ Shorthand Character Classes

|Shortcut|Meaning|
|---|---|
|`\d`|digit (0–9)|
|`\D`|not a digit|
|`\w`|letter, digit, `_`|
|`\W`|anything except `\w`|
|`\s`|whitespace|
|`\S`|not whitespace|

```python
if re.search("^\w+@\w+\.edu$", email):
    print("Valid")
```

---

# ✅ Multiple Domain Support

```python
import re

if re.search("^\w+@\w+\.(com|edu|org|net|gov)$", email, re.IGNORECASE):
    print("Valid")
```

`(A|B|C)` means **A or B or C**

---

# ✅ Capturing Groups `( ... )`

```python
import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")
```

- `Doe, John` → `John Doe`
    

|Group|Output|
|---|---|
|`group(0)`|full match|
|`group(1)`|first capture|
|`group(2)`|second capture|

---

# ✅ Walrus Operator `:=`

Assign and use at the same time:

```python
if matches := re.search(r"^(.+), *(.+)$", name):
    print(matches.group(1))
```

---

# ✅ `re.match` and `re.fullmatch`

|Function|Meaning|
|---|---|
|`re.search`|look anywhere|
|`re.match`|only at the start (`^` not required)|
|`re.fullmatch`|must match entire string (`^$` not required)|

---

# ✅ Raw Strings — `r""`

Why use?

Because regex has many backslashes (`\d`, `\w`, `\s`...)

|Without Raw|With Raw|
|---|---|
|`"\\d"`|`r"\d"` ✅|

You should almost always use `r""` for regex.

---

# ✅ Extracting Twitter Username

### ✅ Using `removeprefix`

```python
url = input("URL: ").strip()
username = url.removeprefix("https://twitter.com/")
print(username)
```

### ✅ Using Regex

```python
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print("Username:", matches.group(2))
```

- `https?` → http or https
    
- `(www\.)?` → [www](http://www). is optional
    
- `(\w+)` → username
    

---

# ✅ `re.sub` — Search & Replace

```python
import re

url = input("URL: ").strip()

username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
print(username)
```

---

# ✅ `re.findall` — Find all matches

```python
import re
print(re.findall(r"\d", "a1b2c3"))
```

Output:

```
['1', '2', '3']
```

---

# ✅ `re.split` — Split by regex

```python
import re
print(re.split(r"[,; ]", "a,b;c d"))
```

Output:

```
['a', 'b', 'c', 'd']
```

---

# ✅ Summary Table

|Pattern|Meaning|
|---|---|
|`\d`|digit|
|`\D`|not a digit|
|`\w`|word character (a–z, A–Z, 0–9, `_`)|
|`\W`|not a word character|
|`\s`|whitespace|
|`\S`|not whitespace|
|`^`|start of string|
|`$`|end of string|
|`|`|
|`( )`|capturing group|
|`(?: )`|non-capturing group|
|`*`|0+ repeats|
|`+`|1+ repeats|
|`{m,n}`|m to n repeats|

---

# ✅ Final Example: Proper Email Validator

```python
import re

email = input("What's your email? ").strip()

pattern = r"^[\w\.-]+@[\w\.-]+\.(com|edu|org|net|gov)$"

if re.fullmatch(pattern, email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```

✅ Username required  
✅ Domain required  
✅ Popular extensions supported  
✅ Case-insensitive

---

## ✅ Key Takeaways

- Use `re` for powerful text validation and searching
    
- `re.search`, `re.match`, `re.fullmatch`, `re.findall`, `re.split`, `re.sub`
    
- character sets, repetition, anchors, groups
    
- capturing vs non-capturing groups
    
- `r""` for raw regex strings
    
- walrus operator for clean code
    
- real examples: email and Twitter username extraction
    