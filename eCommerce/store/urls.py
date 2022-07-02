from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('footwear/', views.footwear, name='footwear'),
    path('clothes/', views.clothes, name='clothes'),
    path('electronics/', views.electronics, name='electronics'),
    path('cart/', views.cart, name='cart'),
]