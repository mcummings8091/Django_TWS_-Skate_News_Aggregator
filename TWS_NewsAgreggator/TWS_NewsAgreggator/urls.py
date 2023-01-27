"""TWS_NewsAgreggator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from news.views import article_list, article_retrieve, article_create, scrape, getdata

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_list),
    path('articles/<pk>/', article_retrieve),
    path('add-article/', article_create),
    path('', getdata),
    path('scrape/', scrape, name="scrape"),
    path('', article_list, name="home")
]
