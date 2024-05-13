# Torpedo proyecto Django
## Configuración Django
### 1. Clonar el repositorio en el directorio actual (colocar un punto al final)
`$ git clone https://github.com/mcamachog1/onlydepas.git .`
### 2. Crear entorno virtual y activar
`$ python -m venv env`

`$ source env/Scripts/activate`
### 3. Actualizar pip
`$ python -m pip install --upgrade pip`
### 4. Instalar librerías (este paso sustituye del 5 al 7)
`$ pip install -r requirements.txt`
### 5. Instalar Django 4.2
`$ pip install django==4.2`
### 6. Instalar librería psycopg2 para poder conectar a BD Postgres
`$ pip install psycopg2`
### 7. Instalar python-dotenv
`$ pip install python-dotenv`
### 8. Crear proyecto Django (colocar un punto al final)
`django-admin startproject onlydepas .`
### 9. Levantar aplicación y probar
`$ python manage.py runserver`


## Configuración para conectar a BD Postgres
### 1. Crear en la raíz del proyecto el archivo .env con los valores de conexión a la BD postgres
```
     DATABASE_NAME=onlydepas
     DATABASE_USER=postgres
     DATABASE_PASSWORD=postgres
     DATABASE_HOST=localhost
```
### 2. En settings.py importar os y load_dotenv y ejecutar load_dotenv para leer el archivo .env
```
import os
from dotenv import load_dotenv

load_dotenv()
```
### 3. En settings.py configurar la conexión a postgres sin exponer los passwords
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': '5432',
    }
}
```
### 4. Aplicar las migraciones por defecto
`$ python manage.py migrate`
### 5.- Crear superuser
`$ python manage.py createsuperuser`
- user: admin
- password: admin

## Crear aplicacion Django
### 1. Crear aplicación app
`python manage.py startapp app`
### 2. En settings.py incluir la aplicación en INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
```
## Configurar Usuarios para autenticación
### 1. En urls.py del proyecto incluir en urlpatterns
`path('accounts/', include('django.contrib.auth.urls')),`
`path('', index, name='index'),`
```
from django.contrib import admin
from django.urls import path, include
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
]
```
## 2. En views.py definir función index y función login
```
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('app/index'))
    else:
        return render(request, 'registration/login')
```
## 3. Crear la carpeta _templates_ y las plantillas .html según la siguiente estructura
- PROYECTO
    - app
        - templates
            - app
				- index.html
            - registration
				- login.html
				- logout.html
				- register.html
			- base.html
	- onlydepas
		- manage.py
		- etc.

### 4.- Código de los templates
base.html
```
<!-- base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}OnlyDepas{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```
app/index.html
```
<!-- app/index.html -->
{% extends "base.html" %}

{% block content %}
<h1>WELCOME</h1>
{% endblock %}
```
registration/login.html
```
<!-- registration/login.html -->
{% extends "base.html" %}
{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
{% endblock %}
```

## Extras
### 1.- Instalar django-extensions para ver las urls del proyecto
`$ pip install django-extensions`
### 2.- django-extensions en INSTALLED_APPS en settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'app',
]
```
### 3.- Correr el comando show_urls
`$ python manage.py show_urls`

### 4.- Agregar en settings.py
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)