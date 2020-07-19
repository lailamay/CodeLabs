from django.shortcuts import render
from django.http import HttpResponse

#This is where we put what we want to show on our app

def index(response):
    return HttpResponse('Finance App')

