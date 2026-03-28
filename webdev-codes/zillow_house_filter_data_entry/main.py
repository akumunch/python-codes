import requests
from bs4 import BeautifulSoup
from pprint import pprint
from data_manager import DataManager
from form_filler import FormFiller
# price,addr, url, (beautiful soup) 
# selenium -> google sheet 
gform_link= "https://docs.google.com/forms/d/e/1FAIpQLSf3PmBRpxYcvL2PIBXNteDWD5fQ2QY9Yc1SXKVGbXyDYqcD5w/viewform?usp=sharing&ouid=113303488545948900930"
dm= DataManager()
dm.get_listings()
ff= FormFiller()
ff.fill_form(gform_link,dm.links,dm.addresses,dm.prices)
