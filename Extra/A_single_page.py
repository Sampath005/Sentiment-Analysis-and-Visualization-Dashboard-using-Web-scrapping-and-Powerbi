# from bs4 import BeautifulSoup
# import requests
#
# User_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
#
# def getdata(url):
#
#     Page = requests.get(url,headers=User_agent)
#     soup = BeautifulSoup(Page.content,'lxml')
#     return soup
#     # print(soup.prettify())
#
#
# #title of the product
# # T_div_tag = soup.find('div',class_="a-section a-spacing-none")
# # Title = T_div_tag.find('span',class_="a-size-large product-title-word-break")
# # # print(T_div_tag)
# # print(Title.text.strip())
#
# #Rating
# # R_div_tag = soup.find('div',id='averageCustomerReviews')
# # print(R_div_tag)
# # Rating = R_div_tag.find('span',class_ = 'reviewCountTextLinkedHistogram noUnderline')
# # print(Rating.text.strip()[:3])
#
# #No of Rating
#
# # N_Rating = soup.find('span',class_='a-size-base')
# # print(N_Rating.text)
#
# # Reviews_tag = soup.findAll('a',{'class':"a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"})
# # div_t = soup.find_all('div',{'class':'a-row'})
# # a_tags = soup.find_all('a',{'class':'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold','data-hook':'review-title'})
# # print(div_t)
# # print(a_tags)
# # for solo in R/eviews_tag :
# #     reviews = solo.find('span')
# #     print(reviews.text)
# # next = soup.find('li',{'class':'a-last'})
# # print(next)
# # next_page = soup.select_one('[data-test=next-link]')
# # print(next_page)
#
#
# #Pagination
# # def getdata(url):
# #     r = requests.get(url)
# #     soup = BeautifulSoup(, 'html.parser')
# #     return soup
#
# def getnextpage(soup):
#     # this will return the next page URL
#     pages = soup.find('ul', {'class': 'a-pagination'})
#     if not pages.find('li', {'class': 'a-disabled a-last'}):
#         url = 'https://www.amazon.in' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
#         return url
#     else:
#         return
# URL='https://www.amazon.in/Vivo-1804-Supernova-Additional-Exchange/product-reviews' \
#         '/B07KRFNQDD/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&filterBy' \
#         'Star=critical&pageNumber=1&mediaType=media_reviews_only'
# while True:
#
#     soup=getdata(URL)
#     url = getnextpage(soup)
#     if not url:
#         break
#     URL=url
#     print(url)


