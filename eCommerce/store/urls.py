from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('footwear/', views.footwear, name='footwear'),
    path('fitness/', views.fitness, name='fitness'),
    path('electronics/', views.electronics, name='electronics'),
    path('books/', views.books, name='books'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('add/<int:id>', views.add_to_cart, name='addToCart'),
    path('cart/', views.cart, name='cart'),
]
