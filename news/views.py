from django import shortcuts


from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.generic import ListView

import requests, json

# Create your views here.

class NewsListView(ListView):
    pass

def homePageView(request):
    # get the list of news items
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url=url)
    news_items = response.json()
    
    return render(request, 'home.html', {"news_items": news_items[:100]})
