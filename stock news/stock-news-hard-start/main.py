import requests
import smtplib
from datetime import date, timedelta
from pprint import pprint
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything" 
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


yday= date.today()-timedelta(days=1)
dbyday= yday-timedelta(days=1)

news_params= {
    'q':COMPANY_NAME,
    'apiKey': NEWS_API_KEY,
    'from':yday,
    'to':dbyday,
    'sortBy':'relevancy',
    'language':'en',
}

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}


news_response=requests.get(url=NEWS_ENDPOINT,params=news_params).json()
three_articles= news_response['articles'][:3]



stock_response=requests.get(url=STOCK_ENDPOINT,params=stock_params).json()

# yday_stock_response= stock_response['Time Series (Daily)'][str(yday)]
# dbyday_stock_response= stock_response['Time Series (Daily)'][str(dbyday)]
time_series= stock_response["Time Series (Daily)"]
dates= list(time_series.keys())
latest_date= dates[0]
previous_date= dates[1]

prev_close_price= round(float(time_series[previous_date]['4. close']),2)
curr_close_price= round(float(time_series[latest_date]['4. close']),2)

percent_change= round(((curr_close_price-prev_close_price)/prev_close_price)*100,2)

var= "🔻"
if percent_change>0: 
    var="🔺"
formated_messages= [f"{STOCK}: {var}{abs(percent_change)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

if (abs(percent_change)>=1.0):
    for article in formated_messages:        
        client= Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_="whatsapp:+14155238886",
            to="whatsapp:+919873355089",
            )
        print(message.status)