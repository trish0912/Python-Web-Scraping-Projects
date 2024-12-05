import requests
from bs4 import BeautifulSoup
import pandas as pd

l =[]
for i in range(1,11):
    url = f'https://www.flipkart.com/furniture/drawers/pr?sid=wwe%2Cxdf&otracker=categorytree&p%5B%5D=facets.price_range.from%3D2000&p%5B%5D=facets.price_range.to%3DMax&fm=neo%2Fmerchandising&iid=M_9b585174-fe95-4969-95e3-3d9772313f2a_1_372UD5BXDFYS_MC.RMQOXCI4XITE&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BFurniture%7ELiving%2BRoom%2BFurniture%7ECabinet%2B%2526%2BDrawers_RMQOXCI4XITE&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L2_view-all&cid=RMQOXCI4XITE&page={i}'
    response = (requests.get(url)).content
    soup = BeautifulSoup(response,'html.parser')

    data = soup.find_all('div',class_='_4ddWXP')

    for d in data:
        title = (d.find('a',class_='s1Q9rs')).text
        price = ((d.find('div',class_='_30jeq3')).text)[1:]
        price = float(price.replace(',',''))
        div_elements = d.find_all('div', class_='_3LWZlK')
    #Extract the text from each div element and print the value
        for div in div_elements:
            value = div.text.strip()  # Get the text and remove leading/trailing spaces    
        l.append([title,price,value])
    
df = pd.DataFrame(l, columns=['Title','Price','Rating'])
df.to_csv('flipkart_product.csv')



    

    
  










