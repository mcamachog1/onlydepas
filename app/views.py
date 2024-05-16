# app/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {'user':request.user})

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('app/index'))
    else:
        return render(request, 'registration/login')

def register(request): 
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return HttpResponseRedirect(reverse('login')) 
    else:  
        form = UserCreationForm()  
        context = {  
            'form':form  
        }  
        return render(request, 'registration/register.html', context)  