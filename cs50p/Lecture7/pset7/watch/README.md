# ▶️ Watch on YouTube

**CS50P – Problem Set 7**

In this exercise, we work with embedded YouTube videos inside HTML and convert their long embed URLs into short, shareable `youtu.be` links.

---

## ✅ Goal

You’re given a string of HTML that may contain an `<iframe>` tag with an embedded YouTube video.
Your task:

1. **Find** the YouTube embed URL inside the `src` attribute
2. **Extract** the video ID
3. **Convert** it into a shorter `https://youtu.be/...` link
4. **Return `None`** if there is no embedded YouTube URL in the input

---

## ✅ About Embedded YouTube URLs

HTML pages can embed YouTube videos using:

```
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
```

or with extra attributes:

```
<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0" allowfullscreen></iframe>
```

You must support URLs in these formats:

| Accepted URL formats                    |
| --------------------------------------- |
| `http://youtube.com/embed/VIDEOID`      |
| `https://youtube.com/embed/VIDEOID`     |
| `https://www.youtube.com/embed/VIDEOID` |

After extracting the video ID, convert to:

```
https://youtu.be/VIDEOID
```

---

## ✅ Requirements

Create a file named **`watch.py`** that contains a function:

```python
parse(html: str) -> str | None
```

* Returns a short `youtu.be` link if a valid YouTube embed URL is found
* Returns `None` if no such URL exists
* Only one YouTube URL will appear in the input
* The value of `src` will always be in **double quotes**
* You may use the `re` module, but no external libraries

➡️ View implementation:
📄 [`watch.py`](./watch.py)

---

## ✅ How the Regex Works

To locate the YouTube URL and extract it, a pattern similar to the following is used:

```
r'<iframe[^>]*src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"'
```

### Explanation by parts:

| Pattern               | Meaning                                                              |
| --------------------- | -------------------------------------------------------------------- |
| `<iframe`             | We are inside an iframe element                                      |
| `[^>]*`               | Match anything until we reach `>` (but do *not* include it)          |
| `src=" ... "`         | The YouTube URL will be inside these quotes                          |
| `https?://`           | `http` or `https`                                                    |
| `(?:www\.)?`          | `www.` may or may not appear (non-capturing group)                   |
| `youtube\.com/embed/` | Literal match for embed path                                         |
| `[^"]+`               | One or more characters until the closing quote (video ID lives here) |

Once the URL is captured, the video ID is the final part after `/embed/`.

Example:

```
https://www.youtube.com/embed/xvFZjo5PgG0
                                ↑ video ID
```

The program then returns:

```
https://youtu.be/xvFZjo5PgG0
```

---

## ✅ What This Problem Teaches

* Extracting structured information from HTML
* Using `re.search` and capturing groups
* Understanding:

  * greedy characters (`*` and `+`)
  * non-capturing groups `(?: ... )`
  * raw string notation `r""`
* Real-world text parsing