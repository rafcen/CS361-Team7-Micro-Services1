import requests

# from urllib import response


def test_currency_converter():
    print("Sending request to microservice...")

    response = requests.get(
        "http://localhost:8000/convert",
        params={"amount": 100, "from_currency": "USD", "to_currency": "EUR"},
    )
    if response.headers.get("Content-Type") == "application/json":
        print("Response received from Microservice:")
        print(response.json())
    else:
        print("Response not in JSON format")



if __name__ == "__main__":
    test_currency_converter()
