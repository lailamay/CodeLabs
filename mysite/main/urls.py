#This is where URLS from different views in views.py are defined

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]