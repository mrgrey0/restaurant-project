from django.contrib import admin
from django.urls import path
from main.views import menu

urlpatterns = [
    path('menu/',menu, name='menu')
]