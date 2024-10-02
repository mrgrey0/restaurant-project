from django.contrib import admin
from django.urls import path
from main.views import category, menu

urlpatterns = [
    path('menu/',menu, name='menu'),
    path('category/<str:category>/', category, name='category'),
]