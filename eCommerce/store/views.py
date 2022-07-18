from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import requests
import os
import json


def getCartTotal(request):
    user_cart = Cart.objects.filter(user_id=request.user.id)
    cart_total = 0
    for item in user_cart:
        cart_total += item.quantity
    return cart_total


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'store/signup.html')
    elif request.method == 'POST':
        try:
            body = request.POST
            username = body['username']
            password = body['password']
            first_name = body['firstname']
            last_name = body['lastname']
            email = body['email']

            TheUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email)
            return redirect('home')
        except:
            return render(request, 'store/signup.html', {'msg': 'Username already exists'})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'store/login.html')
    elif request.method == 'POST':
        body = request.POST
        user = authenticate(
            username=body['username'],
            password=body['password'])

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/login.html', {'msg': "Username or Password is Incorrect"})


def log_out(request):
    logout(request)
    return redirect('login')

# send store item info to be displayed on the Home Page


@login_required(login_url='login')
def index(request):
    data = Product.objects.filter(category='homepage')
    return render(request, 'store/index.html', {'data': data, 'user': request.user, 'cart_total': getCartTotal(request)})

# send store item info to be displayed on the Footwear (Category) Page


@login_required(login_url='login')
def footwear(request):
    data = Product.objects.filter(category='footwear')
    return render(request, 'store/footwear.html', {'data': data, 'cart_total': getCartTotal(request)})

# send store item info to be displayed on the Fitness (Category) Page


@login_required(login_url='login')
def fitness(request):
    data = Product.objects.filter(category='fitness')
    return render(request, 'store/fitness.html', {'data': data, 'cart_total': getCartTotal(request)})

# send store item info to be displayed on the Electronics (Category) Page


@login_required(login_url='login')
def electronics(request):
    data = Product.objects.filter(category='electronics')
    return render(request, 'store/electronics.html', {'data': data, 'cart_total': getCartTotal(request)})

# send store item info to be displayed on the Books (Category) Page


@login_required(login_url='login')
def books(request):
    data = Product.objects.filter(category='books')
    return render(request, 'store/books.html', {'data': data, 'cart_total': getCartTotal(request)})

# allow user to search for an item by name.


@login_required(login_url='login')
def search(request):
    # show user the search page
    if request.method == 'GET':
        return render(request, 'store/search.html')
    # check if the product the user searched for is available in the store
    elif request.method == 'POST':
        result = []
        search_item = request.POST.get('name').lower()
        data = Product.objects.all()
        for item in data:
            item_name = item.name.lower()
            if item_name.find(search_item) >= 0:
                result.append(item)
        # send the product to the searchResult page to be displayed if it's available
        if len(result) > 0:
            return render(request, 'store/searchResult.html', {'data': result})
        # if the product is not available, get an image of it from the noun project api and send it to the frontend
        else:
            load_dotenv()
            auth = OAuth1(os.environ['apiKey'], os.environ['apiSecret'])
            endpoint = f"http://api.thenounproject.com/icon/{search_item}"

            response = requests.get(endpoint, auth=auth)
            data = {'response': json.loads(response.content)}
            return render(request, 'store/outOfStock.html', data)


@login_required(login_url='login')
def add_to_cart(request, id):
    if request.method == 'GET':
        cart = Cart.objects.filter(user_id=request.user.id)
        item_found = False
        for item in cart:
            if item.product_id == id:
                item.quantity += 1
                item.save()
                item_found = True
        if item_found == False:
            new_item = Cart(product_id=id,
                            user_id=request.user.id, quantity=1)
            new_item.save()
        return JsonResponse({'cart_total': getCartTotal(request)})


def cart_info(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    cartList = []
    for item in cart:
        cartList.append(item.__dict__)
    cartList = f"{cartList}"
    return JsonResponse({'cart': cartList})
