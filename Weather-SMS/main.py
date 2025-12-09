import requests
import os
from twilio.rest import Client

MY_LAT=12.8797
MY_LNG=121.7740
API_KEY=os.environ.get("API_KEY")
account_sid= os.environ.get("ACCOUNT_SID")
auth_token= os.environ.get("AUTH_TOKEN")

parameters= {
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":API_KEY,
    "cnt":4,
}

respond= requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                      params=parameters)
respond.raise_for_status()
will_rain= False
weather_data= respond.json()


# print (weather_data)
# for i in range(4):
#     weather_layers= weather_data['list'][i]['weather'] #this consists of a list of dictionaries 
#     for j in weather_layers:
#         if j['id']<700:
#             will_rain=True

for data in weather_data["list"]:
    if (data["weather"][0]["id"]<700):
        will_rain=True                     #more efficient way

if (will_rain):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today, bring an Umbrella ☂️☔!",
    from_="whatsapp:+14155238886",
    to="whatsapp:+919873355089",
    )

    print(message.status)


else:
    print("It wont rain you chill")    
