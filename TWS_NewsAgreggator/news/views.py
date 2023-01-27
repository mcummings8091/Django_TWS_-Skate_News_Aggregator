from multiprocessing import context
from re import L
import requests
import imp
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from bs4 import BeautifulSoup
import urllib3

# Create your views here.
# CRUD - create, retrieve, update, delete, list

requests.packages.urllib3.disable_warnings()

def article_list(request):
    articles = Article.objects.all()
    context ={
        "articles" : articles
    }
    return render(request, "articles.html", context)


def article_retrieve(request, pk):
    article = Article.objects.get(id=pk)
    context ={
        "article" : article
    }
    return render(request, "article.html", context)


def article_create(request):
    form = ArticleForm()
    context ={
        "form": form 
    }
    return render(request, "article_create.html", context)


def getdata(url):
    r = requests.get(url)
    return r.text


def scrape(request):
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
    # Imgs scraping currently broken. Returning NoneType when called.

    for x in range(len(list_of_links)):
        if '' in list_of_links:
            list_of_links.remove('')

    
    for t, l in zip(titles, list_of_links):
        new_article = Article()
        new_article.title = t
        new_article.link = l
        new_article.save()
    return redirect("../")
    
def articles_list(request):
    articles = Article.objects.all()[::1]
    context = {
        'object_list' : articles,
    }
    return render(request, "news/articles.html", context)

    