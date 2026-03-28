import requests
from bs4 import BeautifulSoup

class DataManager:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []
    
    def get_listings(self):
        zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0",
            "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
        }
        
        response = requests.get(zillow_clone_url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        
        beg_links = soup.find_all("a", attrs={"data-test": "property-card-link"})
        self.links = [link.get("href") for link in beg_links]
        
        beg_prices = soup.find_all("span", attrs={"data-test": "property-card-price"})
        self.prices = [price.text.split("+")[0].replace("/mo", "") for price in beg_prices]
        
        beg_address = soup.find_all("img", attrs={"class": "Image-c11n-8-84-listing"})
        self.addresses = [addr.get("alt").strip().replace(" |", "") for addr in beg_address]