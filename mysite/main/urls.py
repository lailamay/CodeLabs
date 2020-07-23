#This is where URLS from different views in views.py are defined

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.index, name='index'),
    path("", views.home, name='home'),
    path("create/", views.create, name="create"),
    #path('<int:scenariolist_id>/student/', views.student, name='student page'),
    #path('<int:scenariolist_id>/', views.scenario, name='scenarios')
]