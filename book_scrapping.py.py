import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame

#
# base_url = 'https://books.toscrape.com/catalogue/'
# url = 'https://books.toscrape.com/catalogue/page-1.html'
#
# books=[]
# n=2
# while True:
#
#     response = requests.get(url)
#     soup = bs(response.text, 'html.parser')
#
#     for i in soup.find_all('article', class_='product_pod'):
#         book_name = i.h3.a['title']
#         #print(book_name)
#
#         for price in i.find_all('div', class_='product_price'):
#             value = price.find('p', class_='price_color').get_text(strip=True)
#             #print(value)
#
#             ava = price.find('p', class_="instock availability").get_text(strip=True)
#             #print(ava)
#
#         rating= i.p['class'][-1]
#         #print(rating)
#         books.append({'book_name ':book_name, 'price ': value, 'Availability ': ava, 'rating ': rating})
#
#     print(f"--------------------page{n}----------------------")
#     n+=1
#     next_page=soup.find('li', class_='next')
#     if next_page is None:
#         break
#     else:
#         url = base_url+next_page.a['href']

# book = pd.DataFrame(books)
# book.to_csv('books_data.csv')
df: DataFrame = pd.read_csv('books_data.csv', index_col=False)

# df['price '] = df['price '].str.replace('Â£', '').astype(float)
# min_price=df.loc[df['price '].idxmin()]
# print("minimum priced book: ", min_price)
# df.columns=['name','price','Availability','rating']
# print(df[df['rating ']=='Four'])

df.columns=['index','name','price','Availability','rating']
df=df.drop(columns=['index'])
# print(df.head(1))

df['price']=df['price'].str.replace('Â£','').astype(float)
print(df.head(1))

#min price
min_price = df.loc[df['price'].idxmin()]
print(min_price)

# rating with four start
four_rating = df['rating'] == "Four"
print(df[four_rating].head(1))