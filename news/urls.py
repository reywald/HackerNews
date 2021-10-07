from django.urls import path
from .views import NewsListView
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
]
