import requests
import os
from pprint import pprint

class FlightSearch():
    #This class is responsible for structuring the flight data.
    token= None
    def __init__(self,origin:str,destination:str,nonStop=True):
        self.api_key= os.environ.get("AMADEUS_API_KEY")
        self.api_secret=os.environ.get("AMADEUS_API_SECRET")
        self.url= "https://test.api.amadeus.com/v2/shopping/flight-offers"

        self.token= self.getToken()
        self.header= {
            "Authorization":f"Bearer {self.token}"
        }
        self.params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": "2026-01-10",
        "adults": 1,
        "nonStop":nonStop
        }

    def search(self):
        response= requests.get(url=self.url,params=self.params,
                                    headers=self.header).json()
        return response
    def getToken(self):
        if FlightSearch.token:
            return FlightSearch.token
        self.test_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        data= {
            "grant_type":"client_credentials",
            "client_id":self.api_key,
            "client_secret":self.api_secret,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response= requests.post(url=self.test_url,data=data,headers=headers).json()
        FlightSearch.token=  response['access_token']
        return FlightSearch.token