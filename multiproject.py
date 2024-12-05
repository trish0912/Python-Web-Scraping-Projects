import requests
from bs4 import BeautifulSoup
import pandas as pd

data_list = []
for i in range(1,10):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    r = requests.get(url)
    response = r.content
    soup = BeautifulSoup(response,'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = (article.find('p', class_='price_color')).text
        price = float(price[1:])
    
        data_list.append([title,star,price])
    
df = pd.DataFrame(data_list, columns=['Title','Star Rating','Price'])
df.to_csv('Books.csv')






