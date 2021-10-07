from django.urls import path
from .views import NewsListView
from .views import homePageView, detailPageView

urlpatterns = [
    path('news/<str:item>', detailPageView, name='news_detail'),
    path('', homePageView, name='home'),
]
