import requests
from datetime import datetime, timedelta
import os 

API_KEY = os.environ.get("AMADEUS_API_KEY")
API_SECRET = os.environ.get("AMADEUS_API_SECRET")

ORIGIN = "MAA"
DESTINATION = "DEL"

START_DATE = datetime(2025, 5, 15)
END_DATE = datetime(2025, 5, 31)


def get_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return requests.post(url, data=data, headers=headers).json()["access_token"]


def search_flights(token, date_str):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": ORIGIN,
        "destinationLocationCode": DESTINATION,
        "departureDate": date_str,
        "adults": 1,
        "currencyCode": "GBP",
        "max": 10,
    }
    return requests.get(url, headers=headers, params=params).json()


token = get_token()

lowest_price = float("inf")
best_offer = None
best_date = None

current_date = START_DATE
while current_date <= END_DATE:
    date_str = current_date.strftime("%Y-%m-%d")
    response = search_flights(token, date_str)

    for offer in response.get("data", []):
        price = float(offer["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            best_offer = offer
            best_date = date_str

    current_date += timedelta(days=1)


if best_offer:
    segments = best_offer["itineraries"][0]["segments"]
    airline = best_offer["validatingAirlineCodes"][0]
    stops = len(segments) - 1
    dep = segments[0]["departure"]["at"]
    arr = segments[-1]["arrival"]["at"]

    print("Cheapest flight in May:")
    print("Date:", best_date)
    print("Price:", lowest_price, "GBP")
    print("Airline:", airline)
    print("Departure:", dep)
    print("Arrival:", arr)
    print("Stops:", stops)
else:
    print("No flights found in May.")
