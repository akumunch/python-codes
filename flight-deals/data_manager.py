import requests
import os
from pprint import pprint
class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint= os.environ.get("FLIGHT_SHEETY_EP")
        self.token= os.environ.get("FLIGHT_SHEETY_TOKEN")
        self.headers= {
            "Authorization": f"Bearer {self.token}"
        }
        response= requests.get(url=self.endpoint,headers=self.headers).json()
        self.prices_codes= {c['iataCode']:c['lowestPrice'] for c in response['prices']}
        self.iataCodes= list(self.prices_codes.keys())
        self.prices= list(self.prices_codes.values())
