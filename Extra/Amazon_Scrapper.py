
from bs4 import BeautifulSoup
import requests

User_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
URL = 'https://www.amazon.in/s?k=laptop&sprefix=la%2Caps%2C334&ref=nb_sb_ss_ts-doa-p_1_2'
def getdata(url):

    Page = requests.get(url,headers=User_agent)
    soup = BeautifulSoup(Page.content,'lxml')
    return soup

def next_page(Soup):
    page = Soup.find('span',{'class':'s-pagination-strip'})
    if page.find('a',{'class':"s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"}):
        url = 'https://www.amazon.in'+page.find('a',{'class':"s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"})['href']
        return url
    else :
        return

while True:
    soup=getdata(URL)
    url = next_page(soup)
    if not url:
        break
    URL=url
    print(url)

# soup=getdata(URL)
# Products = soup.find_all('span',{'class':'a-size-medium a-color-base a-text-normal'})
# products_link = soup.find_all('a',{'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

# print(Products)
# print(len(Products))
# for product in products_link :
#     link = 'https://www.amazon.in'+product['href']
#     print(link)
