#CREATING COMPUTER GENERATED WORD. 
import requests 
import random
def fetcher(): 
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = [word.decode("utf-8") for word in response.content.splitlines()]
    return WORDS
def random_choice(word_list): 
    return random.choice(word_list)