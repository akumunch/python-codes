import requests 
from datetime import datetime
import smtplib

MY_LAT=13.082680
MY_LNG=80.270721

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters= {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}

response= requests.get(url=" https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
sunrise=int(response.json()['results']['sunrise'].split("T")[1].split(":")[0])
sunset=int(response.json()['results']['sunset'].split("T")[1].split(":")[0])

time_now= datetime.now().hour


def isnighttime(time_now,sunrise,sunset):
    if (sunset<time_now<sunrise):
        return True
    return False

def overhead(iss_latitude,iss_longitude):
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    return False

def send_email(text):
    my_email= "khaboostest@gmail.com"
    password= "ljqldewxlakektyp"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="t.akshath@yahoo.com",
                            msg=f"{text}")

if (isnighttime(time_now,sunrise,sunset) and overhead(iss_latitude,iss_longitude)):
    text= "Subject: Look up ☝️\n\nLook above you, ISS is passing by!"
    send_email(text)



