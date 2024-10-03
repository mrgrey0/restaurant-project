from django.contrib import admin
from django.urls import path
from main.views import category, food_detail_view, menu, signup_view, login_view, buy_func, hotel_dashboard, mark_order_complete

urlpatterns = [
    path('menu/',menu, name='menu'),
    path('category/<str:category>/', category, name='category'),
    path('food/<str:food_name>/', food_detail_view, name='food_detail'),
    path('signup/', signup_view, name='signup'),
    path('login/',login_view, name='login'),
    path('buy/', buy_func, name='buy'),
    path('hotel_dashboard/',hotel_dashboard, name='hotel_dashboard'),
    path('complete/<str:order_id>/', mark_order_complete, name='mark_order_complete'),
]