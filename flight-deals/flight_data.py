class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self,offers:dict,from_date:str,to_date:str):
        #from these offers the lowest price within next 6 months is returned
        self.lowestPrice=float("inf")
        for data in offers['data']:
            dep_date= self.get_date(data)
            if (from_date<dep_date<to_date and 
                float(self.lowestPrice)>float(data['price']['grandTotal'])):
                self.lowestPrice= float(data['price']['grandTotal'])
                self.date_of_flight= dep_date
                self.airline_code= data['validatingAirlineCodes'][0]
                self.time_flight= self.get_time(data)
    def get_date(self,data):
        return data['itineraries'][0]['segments'][0]["departure"]["at"].split("T")[0]
    def get_time(self,data):
        return data['itineraries'][0]['segments'][0]["departure"]["at"].split("T")[1]