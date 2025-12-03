##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt 
import pandas as pd 
import random

now= dt.datetime.now()
day= now.day
month= now.month

today= (month,day)
letters= ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

df= pd.read_csv("birthdays.csv")
dict_df= {(data_row["month"],data_row["day"]): data_row for (index,data_row) in df.iterrows()}

my_email= "khaboostest@gmail.com"
password= "ljqldewxlakektyp"


if today in dict_df:
    letter= random.choice(letters)
    with open(letter) as file:
        birthday_person= dict_df[today]
        lines_letters= file.read()
        new_name= birthday_person["name"].strip()
        new_letter= lines_letters.replace("[NAME]",new_name)
        with smtplib.SMTP("smtp.gmail.com",587) as connection: 
            connection.ehlo()
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email, 
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Birthday Wishes\n\n{new_letter}")


