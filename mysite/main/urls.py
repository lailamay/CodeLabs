#This is where URLS from different views in views.py are defined

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:scenariolist_id>/student/', views.student, name='student page'),
    path('<int:scenariolist_id>/', views.scenario, name='scenarios')
]