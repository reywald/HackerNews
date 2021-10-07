from django.urls import path
from .views import background_view

urlpatterns = [
    path('', view=background_view, name='background')
]
