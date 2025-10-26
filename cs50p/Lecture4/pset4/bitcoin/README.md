# ₿ Bitcoin Price Index — CS50P Problem Set 4

## 📘 Problem Description

**Bitcoin** is a form of digital currency (cryptocurrency) that operates on a decentralized network called the **blockchain**.
Rather than rely on a central authority such as a bank, Bitcoin transactions are recorded and verified by a distributed network of users.

In this problem, you’ll implement a program, **`bitcoin.py`**, that uses the **CoinCap API** to determine how much it would cost (in USD) to buy a given number of Bitcoins.

Your program should:

1. Expect the user to specify, as a **command-line argument**, how many Bitcoins they want to buy.

   * If the argument can’t be converted to a float, exit via `sys.exit()` with an error message.
2. Query the **CoinCap v3 API** for the current Bitcoin price:

   ```
   https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey
   ```

   You must first create a free account on [CoinCap](https://pro.coincap.io/signup) and obtain your own **API key**.
3. Handle possible network errors with a `try`/`except requests.RequestException` block.
4. Parse the returned **JSON** object, access the `"priceUsd"` field, and compute the total cost.
5. Output the price of `n` Bitcoins in USD to four decimal places, with commas as thousands separators.

Example JSON response (truncated):

```json
{
  "data": {
    "id": "bitcoin",
    "priceUsd": "97845.0243474572557500"
  },
  "timestamp": 1739399343596
}
```

Example output format:

```
$97,845.0243
```

---

## 💡 My Explanation

In this program, we determine the **USD value** of a given number of Bitcoins using real-time data from the CoinCap API.

### Steps I Followed

1. **Command-line validation**

   * Check that exactly one argument is provided.
   * Try converting it to a float; if it fails, exit with an error.

2. **API request**

   * Send a `GET` request to the CoinCap API endpoint using `requests.get()`.
   * Wrap this call in `try/except` to handle connection or timeout errors gracefully.

3. **Extract and calculate**

   * Convert the JSON response to a Python dictionary with `.json()`.
   * Retrieve the current price from `["data"]["priceUsd"]` and cast it to `float`.
   * Multiply that value by the user’s Bitcoin amount.

4. **Format and output**

   * Print the total cost in U.S. dollars, formatted with commas and four decimal places.

---

## 🧩 Code Implementation

📄 [bitcoin.py](./bitcoin.py)

---

## 🧪 Example Usage

```bash
$ python bitcoin.py 2.5
$244,612.5609
```

```bash
$ python bitcoin.py two
Command-line argument is not a number
```

```bash
$ python bitcoin.py
Missing command-line argument
```

---

## 🧠 Key Concepts Learned

* Reading and validating **command-line arguments** (`sys.argv`)
* Using **HTTP requests** in Python with the `requests` library
* Handling network and parsing errors using **`try` / `except`**
* Parsing **JSON** data and accessing nested keys
* Working with **floats**, **type conversion**, and **output formatting**
* Real-world use of an external **API key** and web data integration