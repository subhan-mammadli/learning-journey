# 😶 Regular, um, Expressions

**CS50P – Problem Set 7**

Some people, when thinking aloud, say **“um”** to fill silence. In this exercise, we count how many times **“um”** appears as a standalone word in a given text.

---

## ✅ Goal

Inside **`um.py`**, implement a function:

```python
count(s: str) -> int
```

This function should:

✔ Return the number of times “um” appears
✔ Match **case-insensitively** (`um`, `Um`, `UM`, etc.)
✔ Only count it when “um” is a **whole word**, not part of another word

Examples:

| Input                 | Output                                |
| --------------------- | ------------------------------------- |
| `"hello, um, world"`  | `1`                                   |
| `"Um, thanks, um..."` | `2`                                   |
| `"yummy"`             | `0` (contains “um” but not as a word) |

> 🔗 Implementation:
> 📄 [`um.py`](./um.py)

---

## ✅ The Regex Logic

To find whole-word matches, the solution uses:

```
\b
```

`\b` represents a **word boundary**, meaning the match must start and end like a true separate word, not inside another phrase.

A typical pattern used in this problem looks like:

```
r"\bum\b"
```

### Why this works:

| Pattern | Meaning                   |
| ------- | ------------------------- |
| `\b`    | Word boundary (start)     |
| `um`    | Literal letters "u" + "m" |
| `\b`    | Word boundary (end)       |

So it matches:

✅ `um`
✅ `um?`
✅ `Um,`
❌ `yummy`
❌ `umbrella`

To search without worrying about uppercase or lowercase, the regex uses `re.IGNORECASE`.

Since `re.findall` returns a list of *all* matches, the function simply counts them.

---

## ✅ Testing

Create `test_um.py`, containing at least **three test functions**, each starting with `test_`, so they run with `pytest`.

✔ Test simple matches
✔ Test punctuation (`um?`, `um...`)
✔ Test multiple occurrences
✔ Test words that only contain “um” as substring (`yummy`)

> 🔗 Example tests:
> 📄 [`test_um.py`](./test_um.py)

Run tests:

```
pytest test_um.py
```

---

## ✅ What This Problem Teaches

* How to detect **whole word** regex matches
* Using `\b` (word boundaries)
* Case-insensitive searching with `re.IGNORECASE`
* Counting matches with `re.findall`
* Writing unit tests with pytest