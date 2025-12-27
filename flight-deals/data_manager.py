import requests
import os
from pprint import pprint
class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint= os.environ.get("FLIGHT_SHEETY_EP")
        self.users_endpoint=os.environ.get("USERS_ENDPOINT_SHEETY")
        self.token= os.environ.get("FLIGHT_SHEETY_TOKEN")
        self.headers= {
            "Authorization": f"Bearer {self.token}"
        }
        response= requests.get(url=self.endpoint,headers=self.headers).json()
        self.prices_codes= {c['iataCode']:c['lowestPrice'] for c in response['prices']}
        self.iataCodes= list(self.prices_codes.keys())
        self.prices= list(self.prices_codes.values())
    def get_customer_emails(self):
        users_response= requests.get(url=self.users_endpoint,headers=self.headers).json()
        self.user_emails= [row['pleaseEnterYourEmail'] for row in users_response['users']]
        return self.user_emails