from datetime import datetime
from django.shortcuts import render, HttpResponse
from background_task import background

# Create your views here.


def background_view(request):
    hello(repeat=10, verbose_name="Hello World", repeat_until=datetime(2021, 10, 7, 13, 42, 0))
    return HttpResponse('<h1>Hello World</h1>')


@background()
def hello():
    print('Hello World!')
