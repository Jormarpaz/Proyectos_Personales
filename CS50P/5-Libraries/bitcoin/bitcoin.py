import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <amount>")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Invalid number of Bitcoins. Please enter a valid number.")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException as e:
        sys.exit(f"Error querying CoinDesk API: {e}")

    data = response.json()
    btc_price_usd = data["bpi"]["USD"]["rate_float"]

    total_cost = bitcoins * btc_price_usd
    print(f"Price of {bitcoins:.4f} Bitcoins is ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
