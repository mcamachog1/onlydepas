# urls.py
from django.contrib import admin
from django.urls import path, include
from app.views import index, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name = 'register'),  
    path('', index, name='index'),
]