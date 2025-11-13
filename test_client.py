import requests

def test_currency_converter():
    print("Sending request to microservice...")

    response = requests.get(
        "http://localhost:5000/convert",
        params={
            "amount": 100,
            "from_currency": "USD",
            "to_currency": "EUR"
        }
    )

    print("Response received from microservice:")
    print(response.json())

if __name__ == "__main__":
    test_currency_converter()
