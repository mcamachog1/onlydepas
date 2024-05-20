# app/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect


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
    
def logout(request):
    logout(request)
    return redirect(reverse_lazy('login'))

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