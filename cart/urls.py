from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart', views.view_cart, name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove', views.remove_from_cart, name='remove_from_cart'),
    path('clear', views.clear_cart, name='clear_cart'),
]
