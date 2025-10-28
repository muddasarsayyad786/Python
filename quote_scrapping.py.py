#importing library
from os import write
from warnings import catch_warnings

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#requested for html page and parseHTML
n=2
Base_url = 'http://quotes.toscrape.com/'
url = Base_url
response = requests.get(url)
soup = bs(response.text, 'html.parser') #takes respose converted into text and parse it as html
QUOTES = []
while True:

    for i in soup.find_all('div' , class_='quote'):  #there is div and class quots having multiple quotes thats why used loop
        text=i.find('span', class_='text').get_text(strip=True)  #get_text only give_text part remove tags and all
        #print("Quote: ",text)

        author=i.find('small', class_='author').get_text(strip=True)
        #print("Author: ",author)
        tags=[]
        for tag in i.find_all("a", class_="tag"):
            tags.append(tag.get_text(strip=True))
        #print('tags: ',tags)

        QUOTES.append({'text':text,'author':author,'tags':tags})

    a = soup.find('li', class_='next')

    if a is None:
        break





    else:
        next_page = a.find('a')['href']

        url = Base_url + next_page

        response = requests.get(url)
        soup = bs(response.text,'html.parser')
        print(f"___________page {n} started______________")
        n+=1


print(QUOTES)
print(len(QUOTES))

data = pd.DataFrame(QUOTES)
data.to_csv("Quotes.csv")
print("Saved to Quotes.csv")



