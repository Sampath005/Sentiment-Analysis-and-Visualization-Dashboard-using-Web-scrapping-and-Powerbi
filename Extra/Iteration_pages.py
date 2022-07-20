import requests
from bs4 import BeautifulSoup
#
#
# url = 'https://www.amazon.co.uk/s?k=dslr+camera&i=black-friday&ref=nb_sb_noss'
#
# def getdata(url):
#     r = s.get(url)
#     soup = BeautifulSoup(r.content, 'lxml')
#     return soup
#
# def getnextpage(soup):
#     # this will return the next page URL
#     pages = soup.find('ul', {'class': 'a-pagination'})
#     if not pages.find('li', {'class': 'a-disabled a-last'}):
#         url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
#         return url
#     else:
#         return
#
#
# while True:
#     data = getdata(url)
#     url = getnextpage(data)
#     if not url:
#         break
#     print(url)
User_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
url = 'https://www.amazon.in/Lenovo-IdeaPad-Warranty-Platinum-81WB01BPIN/dp/B09JC1WJ5L/ref=sr_1_20?keywords=laptop&qid=1656605273&sprefix=la%2Caps%2C334&sr=8-20&th=1'
r=requests.get(url,headers=User_agent)
soup = BeautifulSoup(r.content,'lxml')

product_name = soup.find('span',{'class':'a-size-large product-title-word-break'}).text.strip()
# print(product_name)
product_price = soup.find('span',{'class':'a-price-whole'}).text.strip()
# print(product_name)
product_rating = soup.find('span',{'class':'a-icon-alt'}).text.strip()
# print(product_name)
try :
    product_review = soup.find('span',{'id':'acrCustomerReviewText'}).text.strip()
except :
    product_review = 'No ratings'
# print(product_name)
Asin = soup.find('td',{'class':'a-size-base prodDetAttrValue'})
print(Asin.parent)
product_details = {'product_name':product_name,'product_price':product_price,'product_rating':product_rating,
                   'product_reviews':product_review,'ASIN':Asin}
