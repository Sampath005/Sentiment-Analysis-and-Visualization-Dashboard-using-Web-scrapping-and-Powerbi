from bs4 import BeautifulSoup
import requests
import csv

#headers for not being blocked
User_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

# list for storing products links
product_links = []
#iterating pages by for loop
for i in range(1,40):
    # giving request to the website
    r = requests.get(f'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}',headers=User_agent)
    #getting content form website
    soup = BeautifulSoup(r.content,'lxml')
    #Tag contains product link
    product_a_tag = soup.find_all('a',{'class':"_1fQZEK"})
    #creating product link
    for link in product_a_tag:
        product_links.append('https://www.flipkart.com'+link['href'])
# print(product_links)
# print(len(product_links))

#list of dictionary for storing whole product details
Product_details_dict = []
One_star_rating = None
Two_star_rating=None
Three_star_rating=None
Four_star_rating=None
Five_star_rating=None
#iterating product links
for i in product_links:
    #giving request to the product page
    r=requests.get(i,headers=User_agent)
    # getting content form website
    soup = BeautifulSoup(r.content,'lxml')
    #Extracting product name
    try :
        Name = soup.find('span',{'class':'B_NuCI'}).text.strip()
    except :
        Name = None
    print(Name)
    # Extracting product price
    try:
        Actual_price = soup.find('div',{'class':'_3I9_wc _2p6lqe'}).text.strip()
    except:
        Actual_price = 0
    # print( Actual_price)
    try:
        Selling_price = soup.find('div',{'class':'_30jeq3 _16Jk6d'}).text.strip()
    except :
        Selling_price = 0
    # print(product_price)
    # Extracting product rating
    try:
       Overall_rating = soup.find('div',{'class':'_3LWZlK'}).text.strip()
    except :
        Overall_rating = 0
    # print(product_rating)
    # Extracting product review
    try :
        No_of_ratings_and_reviews = soup.find('span',{'class':'_2_R_DZ'}).text.strip()
    except :
        No_of_ratings_and_reviews = 0
    # print(product_review)
    try:
        Discount = soup.find('div',{'class':'_3Ay6Sb _31Dcoz'}).text.strip()
    except:
        Discount = '0% off'
    # print(product_discount)
    try:
        splitted_rating = soup.find_all('div',{'class':'_1uJVNT'})
        # print(splitted_rating)
    except :
        splitted_rating = []

    else:
        for No,ratings in enumerate(splitted_rating):
            # print(No,ratings)
            if No+1==1:
                One_star_rating = ratings.text.strip()
                print(One_star_rating)
            elif No+1 ==2:
                Two_star_rating = ratings.text.strip()
                # print(Two_star_rating)
            elif No+1 ==3:
                Three_star_rating = ratings.text.strip()
                # print(Three_star_rating)
            elif No+1 ==4:
                Four_star_rating = ratings.text.strip()
                # print(Four_star_rating)
            else:
                Five_star_rating = ratings.text.strip()
                # print(Five_star_rating)
    Reviews =''
    Reviews_tag = soup.find_all('p',{'class':'_2-N8zT'})
    for review in Reviews_tag:
        Reviews += ','+(review.text.strip())
    # print(Reviews)
    #dictionary for storing each product details
    product_details = {'Name':Name,'Actual_price':Actual_price, 'Selling_price':Selling_price,'Overall_rating':Overall_rating,
                       'No_of_ratings_and_reviews':No_of_ratings_and_reviews,'Reviews':Reviews,'Discount':Discount,
                       'One_star':One_star_rating,
                       'Two_star':Two_star_rating,'Three_star':Three_star_rating,'Four_star':Four_star_rating,
                       'Five_star':Five_star_rating}
    #appending product details to the list
    Product_details_dict.append(product_details)

print(Product_details_dict)
#file name to store
file_name = 'S:\Projects\Web scrapping\Scraper1.csv'
#filed name
field_names = ['Name','Actual_price','Selling_price','Overall_rating','No_of_ratings_and_reviews','Reviews','Discount','One_star',
               'Two_star','Three_star','Four_star','Five_star']


with open(file_name, 'w',newline='',encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(Product_details_dict)
