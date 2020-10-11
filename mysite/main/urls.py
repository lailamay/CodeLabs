#This is where URLS from different views in views.py are defined

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.index, name='index'),
    path("", views.home, name='home'),
    path("create/", views.create, name="create"),
    path("student/", views.IndexView.as_view(), name='student'),
    #path('<int:scenariolist_id>/', views.scenario, name='scenarios')
]