from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('footwear/', views.footwear, name='footwear'),
    path('fitness/', views.fitness, name='fitness'),
    path('electronics/', views.electronics, name='electronics'),
    path('books/', views.books, name='books'),
]