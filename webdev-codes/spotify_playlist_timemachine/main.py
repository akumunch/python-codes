import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

date= input("Enter date in YYYY-MM-DD format: ")
base_url= "https://www.billboard.com/charts/hot-100/"
date_url= f"{base_url}{date}"
header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0"}
response= requests.get(url=date_url,headers=header)
html=response.text
soup=BeautifulSoup(html,'html.parser')
songs = soup.select("li ul li h3.c-title")
titles = [s.get_text(strip=True) for s in songs[:100]]

ytmusic = YTMusic("oauth.json")
playlist_id = ytmusic.create_playlist(f"top-100_{date}", "Top 100 songs")

for title in titles:
    results = ytmusic.search(title, filter="songs", limit=1)
    if results:
        ytmusic.add_playlist_items(playlist_id, [results[0]["videoId"]])