# 🌌 Problem Set 1 – Deep Thought

> “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
> “You’re really not going to like it,” observed Deep Thought.
> “Tell us!”
> “All right,” said Deep Thought. “The Answer to the Great Question…”
> “Yes…!”
> “Of Life, the Universe and Everything…” said Deep Thought.
> “Yes…!”
> “Is…” said Deep Thought, and paused.
> “Yes…!”
> “Is…”
> “Yes…!!!…?”
> “Forty-two,” said Deep Thought, with infinite majesty and calm.
>
> — *The Hitchhiker’s Guide to the Galaxy*, Douglas Adams

---

## 🧠 Problem Description

In this problem, you are asked to write a program that mimics the famous dialogue above.
Your program should ask the user:

```
What is the Answer to the Great Question of Life, the Universe, and Everything?
```

and respond with:

* `Yes` — if the user’s input represents the number **42**,
* `No` — for any other input.

---

## ⚙️ Implementation Details

To solve this problem:

1. **Prompt the user** for input.
2. **Normalize** the response so that the answer check is case-insensitive and ignores spaces:

   * Convert text to lowercase (`.lower()`)
   * Remove spaces (`.replace(" ", "")`)
3. **Compare** the cleaned input with acceptable answers:

   * `"42"`
   * `"forty-two"`
   * `"fortytwo"`

If the input matches any of them → print `"Yes"`, otherwise → print `"No"`.

---

## 💻 Solution

👉 You can find the full implementation here:
[`deep.py`](./deep.py)

---

## 🧩 Example Runs

```
$ python deep.py
What is the Answer to the Great Question of Life, the Universe, and Everything? 42
Yes
```

```
$ python deep.py
What is the Answer to the Great Question of Life, the Universe, and Everything? Forty Two
Yes
```

```
$ python deep.py
What is the Answer to the Great Question of Life, the Universe, and Everything? 41
No
```

---

## 💡 Notes

* The comparison ignores **case** and **spaces**, so inputs like `"Forty Two"`, `"fortytwo"`, or `"FORTY-TWO"` are all valid.
* This problem reinforces core concepts from **Lecture 1**:

  * `if` / `else` statements
  * String methods: `.lower()`, `.replace()`
  * Logical operators (`or`)
