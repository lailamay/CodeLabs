from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(form.is_valid())
        if form.is_valid():
            print('I love kitty')
            form.save()
            print('It will be okay')
           
            
        return redirect("/")
        
    else:
        form = RegisterForm()
    print('testing testing 123')
    return render(response, "register/register.html", {"form":form})
