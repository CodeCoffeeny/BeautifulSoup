import requests
from bs4 import BeautifulSoup

class Card:
    affiliate = []    
    name = ''
    img = ''

card0001 = Card()

DomainURL = "https://www.trekcc.org"
TargetURL = "/1e/?cardID=0001"
page = requests.get(DomainURL + TargetURL)

soup = BeautifulSoup(page.content, "html.parser")

card_tag = soup.find("img",class_="card-big-img")
card_src = card_tag.get('src')

card0001.img = DomainURL + card_src

''' I think this will be the path to start of card details '''

