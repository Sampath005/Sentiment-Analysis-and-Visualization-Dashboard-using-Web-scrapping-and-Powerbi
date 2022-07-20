
from bs4 import BeautifulSoup
import requests
User_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
product_links = []
for i in range(1,21):
    r = requests.get(f'https://www.amazon.in/s?k=laptop&page={i}&qid=1656605295&sprefix=la%2Caps%2C334&ref=sr_pg_{i}',headers=User_agent)
    soup = BeautifulSoup(r.content,'lxml')
    product_a_tag = soup.find_all('a',{'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    for link in product_a_tag:
        product_links.append('https://www.amazon.in'+link['href'])
print(product_links)

Product_details_list = []
for i in product_links:
    r=requests.get(i,headers=User_agent)
    soup = BeautifulSoup(r.content,'lxml')

    product_name = soup.find('span',{'class':'a-size-large product-title-word-break'}).text.strip()
    product_price = soup.find('span',{'class':'a-price-whole'}).text.strip()
    product_rating = soup.find('span',{'class':'a-icon-alt'}).text.strip()
    try :
        product_review = soup.find('span',{'id':'acrCustomerReviewText'}).text.strip()
    except :
        product_review = 'No ratings'
    product_details = {'product_name':product_name,'product_price':product_price,'product_rating':product_rating,
                       'product_reviews':product_review}
    Product_details_list.append(product_details)
print(Product_details_list)
