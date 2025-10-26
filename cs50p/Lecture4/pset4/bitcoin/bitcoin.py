import json
import requests
import sys


def main():
    argv = sys.argv

    if len(argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    apiKey = "YOUR_API_KEY"

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + apiKey)
    except requests.RequestException:
        sys.exit()

    o = response.json()
    usd = float(o["data"]["priceUsd"])
    amount = bitcoin * usd
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
