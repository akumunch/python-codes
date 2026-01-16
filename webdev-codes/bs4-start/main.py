#for static website
from bs4 import BeautifulSoup
import requests

response= requests.get("https://appbrewery.github.io/news.ycombinator.com/").text
soup=BeautifulSoup(response,'html.parser')

top_news= soup.find_all("a",class_="storylink")
upvotes= soup.find_all("span",class_="score")
article_texts=[news.getText() for news in top_news] 
article_links=[news.get("href") for news in top_news]
article_upvotes=[int(upvote.getText().split()[0]) for upvote in upvotes]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvote_index= article_upvotes.index(max(article_upvotes))
print(f"Title: {article_texts[max_upvote_index]}, Link: {article_links[max_upvote_index]}")

# first_article= top_news[0]
# fa_tag=first_article.getText()
# fa_link=first_article.get("href")    
# fa_upvotes=upvotes[0].getText()
# print(fa_tag,fa_link,fa_upvotes)


# with open("website.html") as file: 
#     contents= file.read()
#     print(contents)
# soup=BeautifulSoup(contents,'html.parser')