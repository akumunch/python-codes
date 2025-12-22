import os
import requests
from pprint import pprint
from datetime import datetime

API_KEY= "nix_live_LZXq4S7Ia9F7c15AUi6mzeaTp0LAqJ4F"
APP_ID= "app_ce6978a5390740e7b864be7e"
AI_HEADERS= {
    "x-app-id": "app_ce6978a5390740e7b864be7e",
    "x-app-key": "nix_live_LZXq4S7Ia9F7c15AUi6mzeaTp0LAqJ4F",
}

AI_URL= "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
user_input= input("Enter your workout today: ")
ai_params= {
  "query": user_input,
  "weight_kg": 116,
  "height_cm": 183,
  "age": 19,
  "gender": "male",
}
ai_response= requests.post(url=AI_URL,json=ai_params,headers=AI_HEADERS)
ai_result= ai_response.json()

now=datetime.now()
time_now= now.strftime("%H:%M:%S")
date_now= now.date()
sheety_headers= {
    "Authorization": "Bearer pokemonballs"
}
post_sheety_url= os.environ.get("SHEETY_ENDPOINT")
sheety_params= {
    "workout":{
        "date":f"{date_now}",
        "time":f"{time_now}",
        "exercise":ai_result['exercises'][0]['name'],
        "duration":ai_result['exercises'][0]['duration_min'],
        "calories":ai_result['exercises'][0]['nf_calories'],
    }
}
sheety_response= requests.post(url=post_sheety_url,json=sheety_params,headers=sheety_headers)
print(sheety_response.text)
