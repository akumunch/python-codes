# import smtplib 

# my_email= "khaboostest@gmail.com"
# password= "ljqldewxlakektyp"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="t.akshath@yahoo.com",
#                         msg="Subject:hello\n\nThis is the body of my email.")
# now= dt.datetime.now()
# year= now.year

# dob= dt.datetime(year=2006,month=4,day=25,hour=14)
# print(dob)

import smtplib
import datetime as dt 
import random

my_email= "khaboostest@gmail.com"
password= "ljqldewxlakektyp"


now= dt.datetime.now()
day_of_week= now.weekday()

def quote_gen():
    with open("quotes.txt") as file:
        list_quotes= file.readlines()
        return random.choice(list_quotes)

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="t.akshath@yahoo.com",
                            msg=f"Subject:Monday motivation\n\n {quote}")

if (day_of_week==2):
    random_quote= quote_gen()
    print("quote is: ",random_quote)
    send_email(quote=random_quote)
    


