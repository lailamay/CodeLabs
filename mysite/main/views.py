from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ScenarioList, Scenario

#This is where we put what we want to show on our app

def index(response):
    scenario_list = ScenarioList.objects.order_by('-pub-date')[:5]
    #ls = ScenarioList.objects.get(id=id)
    return HttpResponse("<h1>Teacher's Page</h1>")

def student(response, scenariolist_id):
    return HttpResponse("<h1>Student's Page</h1> %" % scenario_list)
