"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from datetime import datetime, timedelta, tzinfo
from time import timezone
from pytz import utc

from hnservice.tasks import get_latest_news, schedule_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hnservice.urls')),
]


# Call background tasks every 5 minutes
get_latest_news(schedule=5, repeat=300, repeat_until=schedule_task(), verbose_name="Get Latest News")
# get_latest_news(schedule=5, verbose_name="Get Latest News")
