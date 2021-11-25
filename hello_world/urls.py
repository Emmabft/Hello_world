"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from. import views 

urlpatterns = [
    path('', views.helloWorld),
    path('tal/', views.tal),
    path('recette/', views.recette),
    path('bonjour/', views.bonjour),
    path('welcome/', views.welcome, name='welcome'), #"name" fait le lien entre backend et frontend, le nom doit être le même que dans "form" dans la page bonjour.html
    path('compteur/',views.compteur),
    path('afficher/',views.affiche, name='afficher')
]

