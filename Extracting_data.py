from bs4 import BeautifulSoup
import requests
page = requests.get('https://github.com/topics').text
response = BeautifulSoup(page,'lxml')
# print(response.prettify())

p_tags = response.find_all('p')
# print(p_tags)


Topics = []
p_tags_Topics = response.find_all('p',{'class':"f3 lh-condensed mb-0 mt-1 Link--primary"})
for i in p_tags_Topics :
    Topics.append(i.text)
print(Topics)

Topics_des = []
p_tags_des = response.find_all('p',{'class':"f5 color-fg-muted mb-0 mt-1"})
for i in p_tags_des :
    Topics_des.append(i.text.strip())
print(Topics_des)

Tags = []
Tag_links = response.find_all('a',{'class':"no-underline flex-grow-0"})
for i in Tag_links :
    Tags.append('https://github.com'+ i['href'])
print(Tags)