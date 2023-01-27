from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
import urllib3
import requests
    
def getdata(url):
    r = requests.get(url)
    return r.text


session = requests.Session()
session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
url = "https://skateboarding.transworld.net/news/"

list_of_links = []
titles = []
page = requests.get("https://skateboarding.transworld.net/news/")
page_soup = BeautifulSoup(page.content, 'html.parser')

content = session.get(url, verify=False).content

news = list(page_soup.find_all('h2', class_='article__title-main'))
for container in news:
    for link in container:
        sep = str(link).split('\n')
        for lynk in sep:
            if "</a>" in lynk:
                titles.append(str(lynk[16:-4]).strip())
            elif "</a>" not in lynk:
                list_of_links.append(str(lynk[9:-2]).strip())
    
htmldata = getdata("https://skateboarding.transworld.net/news/")
soup = BeautifulSoup(htmldata, 'html.parser')
search = soup.find_all('div', attrs={'class': 'ok-thumb ok-standard-thumb'})
imgs = list(search)

for x in range(len(list_of_links)):
    if '' in list_of_links:
        list_of_links.remove('')
            

print(imgs[5:])
