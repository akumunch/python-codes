#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


from_date = datetime.now()
to_date = from_date + timedelta(days=180)

STEP=7

FROM_STR = from_date.strftime("%Y-%m-%d")
TO_STR = to_date.strftime("%Y-%m-%d")

TO = "+919873355089"
origin = "MAA"

dm = DataManager()

for key, value in dm.prices_codes.items():
    current_date = from_date
    best_fd = None

    while current_date <= to_date:
        date_str = current_date.strftime("%Y-%m-%d")

        fs = FlightSearch(origin=origin, destination=key, nonStop=True)
        fs.params["departureDate"] = date_str

        offers = fs.search()
        if "data" not in offers or len(offers["data"]) == 0:
            fs = FlightSearch(origin=origin, destination=key, nonStop=False)
            fs.params["departureDate"] = date_str
            offers = fs.search()

        if "data" not in offers:
            current_date += timedelta(days=STEP)
            continue

        fd = FlightData(offers, FROM_STR, TO_STR)

        if fd.lowestPrice != float("inf"):
            if best_fd is None or fd.lowestPrice < best_fd.lowestPrice:
                best_fd = fd

        current_date += timedelta(days=STEP)

    if best_fd and best_fd.lowestPrice <= value:
        if best_fd.stops == 0:
            msg = (
                f"Low price alert! Only GBP {best_fd.lowestPrice} to fly direct from "
                f"{origin} to {best_fd.destination_airport}, on {best_fd.date_of_flight} "
                f"at {best_fd.time_flight} by {best_fd.airline_code}"
            )
        else:
            msg = (
                f"Low price alert! Only GBP {best_fd.lowestPrice} to fly from {origin} to "
                f"{best_fd.destination_airport} with {best_fd.stops} stop(s), on "
                f"{best_fd.date_of_flight} at {best_fd.time_flight} by {best_fd.airline_code}"
            )

        nm = NotificationManager(msg, TO)
        nm.send_message()
