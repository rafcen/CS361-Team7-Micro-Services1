# CS361-Team7-Micro-Services1

This microservice converts a currency amount from one currency to another using a free external exchange-rate API. It communicates using a REST API over HTTP.

# How to Run This Microservice

1. Create and activate the virtual environment

python3 -m venv venv
source venv/bin/activate        # Linux/macOS


2. Install dependencies

pip install -r requirements.txt

3. Start the microservice

python3 app.py

Expected output:

 * Running on http://127.0.0.1:5000

# Communication Contract

This contract describes how to programmatically request and receive data from the Currency Converter microservice.

How to Request Data
Endpoint:
GET /convert


Required Query Parameters:

Parameter | Type | Description
--------- | ---- | -----------
amount | float | The amount to convert
from_currency | string | ISO 4217 currency code to convert from (e.g., "USD")
to_currency | string | ISO 4217 currency code to convert to (e.g., "EUR")

Example Request:

import requests

response = requests.get(
    "http://localhost:5000/convert",
    params={
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR"
    }
)

print(response.json())

-------

How to Receive Data

Successful JSON Response Format:

{
  "from_currency": "USD",
  "to_currency": "EUR",
  "exchange_rate": 0.86302,
  "converted_amount": 86.30,
  "timestamp": "2025-11-13T03:27:17.076613Z"
}

---------

Error Response Format:

{
  "error": "Unsupported currency code: USD or EUR"
}

---------

Example (Processing the Response in Python):

data = response.json()

if "error" in data:
    print("Error:", data["error"])
else:
    print("Converted Amount:", data["converted_amount"])




