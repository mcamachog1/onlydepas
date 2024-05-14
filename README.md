# Torpedo proyecto Django
## Configuración Django
### 0. Crear una carpeta para el proyecto y abrirla con VS Code
### 1. Clonar la rama 'base' (colocar un punto al final)
`$ git clone -b base https://github.com/mcamachog1/onlydepas.git .`
### 2. Renombrar rama base a main para tu proyecto
` $ git branch -m base main`
### 3. Crear entorno virtual y activar
`$ python -m venv env`

`$ source env/Scripts/activate`
### 4. Actualizar pip
`$ python -m pip install --upgrade pip`
### 5. Instalar librerías (este paso sustituye del 6 al 8)
`$ pip install -r requirements.txt`
### 6. Instalar Django 4.2
`$ pip install django==4.2`
### 7. Instalar librería psycopg2 para poder conectar a BD Postgres
`$ pip install psycopg2`
### 8. Instalar python-dotenv
`$ pip install python-dotenv`
### 9. Crear proyecto Django (colocar un punto al final)
`$ django-admin startproject onlydepas .`
### 10. Levantar aplicación y probar
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
### 1. En urls.py del proyecto incluir en urlpatterns las rutas:
`path('accounts/', include('django.contrib.auth.urls')),`
`path('', index, name='index'),`
### e importar las vistas de la aplicación
`from app.views import index`

```
# urls.py
from django.contrib import admin
from django.urls import path, include
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
]
```
## 2. En app/views.py definir función index y función login
```
# app/views.py
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
## 3. Crear la carpeta _templates_ dentro de app y las plantillas base.html, index.html y login.html según la siguiente estructura
- PROYECTO
    - app
        - templates
            - app
				- index.html
            - registration
				- login.html
			- base.html
	- onlydepas
		- manage.py
		- etc.

### 4.- Código de los templates
### base.html
```
<!-- templates/base.html -->
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
### app/index.html
```
<!-- templates/app/index.html -->
{% extends "base.html" %}

{% block content %}
{% if user.is_authenticated %}
    <h1>WELCOME {{ user.username }}</h1>
{% else %}
    <h1>WELCOME</h1>
{% endif %}
{% endblock %}
```
### registration/login.html
```
<!-- templates/registration/login.html -->
{% extends "base.html" %}
{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
{% endblock %}
```
### 5.- Setear la variable LOGIN_REDIRECT_URL en settings.py
```
# URL a la que se redirige si un usuario hace login exitoso
LOGIN_REDIRECT_URL = 'index'
```
### 6. Levantar aplicación y probar
`$ python manage.py runserver`

### 7. Colocar la URL localhost:8000/accounts/login/
Ingresar con el usuario admin password: admin y debe redirigirte al index.html


## Extras (estos pasos no son necesarios para que corra el proyecto)
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

### 4.- Puede ser necesario agregar en settings.py
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
```
# URL a la que se redirige si un usuario hace login exitoso
LOGIN_REDIRECT_URL = 'index'
# URL a la que se redirige si un usuario no está autenticado y trata de acceder a una vista protegida
LOGIN_URL = 'login'  
# URL a la que se redirige si un usuario hace logout exitoso
LOGOUT_URL = 'logout' 
```