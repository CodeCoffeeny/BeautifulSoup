import requests
from bs4 import BeautifulSoup

affilicons = {  'Kli': "https://www.trekcc.org/images/icons/1e/1E-KLG.gif",
                'Fed': "https://www.trekcc.org/images/icons/1e/1E-FED.gif"
                }

class Card:
    affiliate = []
    attribute = []    
    name = ''
    img = ''
    quality = ''

card0001 = Card()

DomainURL = "https://www.trekcc.org"
TargetURL = "/1e/?cardID=0001"
page = requests.get(DomainURL + TargetURL)

soup = BeautifulSoup(page.content, "html.parser")

card_tag = soup.find("img",class_="card-big-img")
card_src = card_tag.get('src')

card0001.img = DomainURL + card_src

''' I think this will be the path to start of card details '''
# lets jump to the information block by looking for this unique style attr
card_block = soup.find('p', attrs={"style":"word-break:break-word"})
#there must be at least one affiliation, will check for more but I think 2 is the max
target_element = card_block.find()
# keep adding affiliate title values to the object until not the img
while ( target_element.name == 'img' ):
    imgTitle = ''.join(filter(str.isalpha,target_element.get('title')))
    card0001.affiliate.append(imgTitle)
    target_element = target_element.find_next_sibling()
# next element should be bold text of the cards name
card0001.name = target_element.get_text()
# next element will just be a br so we can skip over it
target_element = target_element.find_next_sibling().find_next_sibling()
# loop through img tags again here, as there may be 0 or more attribute icons
if( target_element.name == 'img' ):
    while ( target_element.name == 'img' ):
        imgTitle = ''.join(filter(str.isalpha,target_element.get('title')))
        card0001.attribute.append(imgTitle)
        target_element = target_element.find_next_sibling()
        quality = target_element.next_sibling.strip() if isinstance(target_element.next_sibling,str) else None
        if quality != None:
            card0001.quality = quality



print(*card0001.affiliate)
print(card0001.img)
print(card0001.name)
print(*card0001.attribute)
print(card0001.quality)

