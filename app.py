from flask import Flask, request, jsonify
from exchange_service import get_exchange_rate
from datetime import datetime

app = Flask(__name__)


@app.route("/convert", methods=["GET"])
def convert_currency():
    amount = request.args.get("amount", type=float)
    from_currency = request.args.get("from_currency", type=str)
    to_currency = request.args.get("to_currency", type=str)

    if amount is None or from_currency is None or to_currency is None:
        return jsonify({"error": "Missing required parameters"}), 400

    rate = get_exchange_rate(from_currency, to_currency)

    if rate is None:
        return (
            jsonify(
                {
                    "error": f"Unsupported currency code: {from_currency} or {to_currency}"
                }
            ),
            400,
        )

    converted_amount = amount * rate

    return jsonify(
        {
            "from_currency": from_currency,
            "to_currency": to_currency,
            "exchange_rate": rate,
            "converted_amount": round(converted_amount, 2),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )


if __name__ == "__main__":
    app.run(port=8000, debug=True)
