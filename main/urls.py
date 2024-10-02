from django.contrib import admin
from django.urls import path
from main.views import category, food_detail_view, menu

urlpatterns = [
    path('menu/',menu, name='menu'),
    path('category/<str:category>/', category, name='category'),
    path('food/<str:food_name>/', food_detail_view, name='food_detail'),
]