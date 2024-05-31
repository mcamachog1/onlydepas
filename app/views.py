# app/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from django.contrib.auth import get_user_model

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
        CustomUser = get_user_model()
        usuario = CustomUser.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"]
        )
        usuario.save()
        profile = Profile()
        profile.user = usuario
        profile.tipo = request.POST["tipo"]
        profile.save()
        return HttpResponseRedirect(reverse('login')) 
        
        # form = UserCreationForm(request.POST)  
        # if form.is_valid():  
        #     form.save() 
        #     return HttpResponseRedirect(reverse('login')) 
    else:  
        # form = UserCreationForm()  
        # context = {  
        #     'form':form  
        # }  
        # return render(request, 'registration/register.html', context)  
        return render(request, 'registration/register.html')  