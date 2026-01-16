import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response= requests.get(URL).text
soup= BeautifulSoup(response,'html.parser')

movies_raw= soup.find_all('h3',class_="title")
movies_reverse_order= [movie.getText() for movie in movies_raw]
movies= movies_reverse_order[::-1]

with open('movies.txt','w',encoding='utf-8') as file_movies: 
    for movie in movies:
        file_movies.write(f"{movie}\n")


