import requests

def get_exchange_rate(from_currency, to_currency):
    # free API 
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        data = response.json()

        # If API failed or unsupported currency
        if data.get("result") != "success":
            return None

        # rates dictionary contains mapping: {"EUR": 0.92, "GBP": 0.80, ...}
        rates = data.get("rates", {})

        if to_currency.upper() not in rates:
            return None

        return rates[to_currency.upper()]

    except Exception as e:
        print("Error calling exchange API:", e)
        return None
