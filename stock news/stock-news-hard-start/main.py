import requests
import smtplib
from datetime import date, timedelta
from pprint import pprint
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything" 
news_api_key= '4e22bc9e7e404a1fa1dfb77f477d1434'
stock_api_key='FGM64Y2M6APNHLSL'

account_sid= 'AC7586ac190e0667367bc15a90ac89d842'
auth_token= 'e6875b5589cddbdaaaf7f7e5962f2cb8'


yday= date.today()-timedelta(days=1)
dbyday= yday-timedelta(days=1)

news_params= {
    'q':COMPANY_NAME,
    'apiKey': '4e22bc9e7e404a1fa1dfb77f477d1434',
    'from':yday,
    'to':dbyday,
    'sortBy':'relevancy',
    'language':'en',
}

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}


news_response=requests.get(url=NEWS_ENDPOINT,params=news_params).json()
three_articles= news_response['articles'][:3]



stock_response=requests.get(url=STOCK_ENDPOINT,params=stock_params).json()


yday_stock_response= stock_response['Time Series (Daily)'][str(yday)]
dbyday_stock_response= stock_response['Time Series (Daily)'][str(dbyday)]


prev_close_price= round(float(dbyday_stock_response['4. close']),2)
curr_close_price= round(float(yday_stock_response['4. close']),2)

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