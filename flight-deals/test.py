import requests
from data_manager import DataManager
from pprint import pprint
from datetime import datetime,timedelta

class FlightSearch(DataManager):
    #This class is responsible for structuring the flight data.
    def __init__(self,origin:str,destination:str):
        super().__init__() #now super().cities is the list of cities
        self.api_key= "v1Gj1uwOz6ZAEh49YTzPM3reGbyQ9P9m"
        self.api_secret="Hm246ymAUtPV0i7c"
        self.url= "https://test.api.amadeus.com/v2/shopping/flight-offers"

        self.token= self.getToken()
        self.header= {
            "Authorization":f"Bearer {self.token}"
        }
        self.params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": "2026-01-10",
        "adults": 1
        }
        response= requests.get(url=self.url,params=self.params,
                                    headers=self.header).json()
        # print(len(response['data']))
        from_date= datetime.now()
        to_date= from_date + timedelta(days=180)
        from_date= from_date.strftime("%Y-%m-%d")
        to_date= to_date.strftime("%Y-%m-%d")
        lowestPrice= self.prices[0]
        
        print(response['dictionaries'])




    def getToken(self):
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
        return response['access_token']

fs= FlightSearch("MAA","PAR")