import requests 
from bs4 import BeautifulSoup
from smtplib import SMTP
import os

my_email=os.environ.get("MY_EMAIL")
my_pass= os.environ.get("MY_PASS")

URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0","Accept-Language": "en-US,en;q=0.9,es;q=0.8"}
response= requests.get(url=URL,headers=header)
html=response.text 
soup=BeautifulSoup(html,'html.parser')
target_price= 10000.00

int_price= soup.find("span",class_="a-price-whole").getText()
fraction_price= soup.find("span",class_="a-price-fraction").getText()
price= float((int_price+fraction_price).replace(",",""))
title = soup.find(id="productTitle").get_text().strip()

if (price<target_price):
    with SMTP("smtp.gmail.com",587) as connection:
        message = f"{title} is on sale for {price}!"
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email, 
                          to_addrs="t.akshath@yahoo.com",
                          msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))