from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os
import json


my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "./data/inventory.json")
    
with open(file_path) as f:
    data = json.load(f)
    content = {"inventory": data}
    
def index(request):
    
    data = {}
    return render(request, 'store/index.html', data)

def search(request):
    if request.method == 'GET':
        return render(request, 'store/search.html')
    elif request.method == 'POST':
        search_item = request.POST.get('name')
        load_dotenv()
        auth = OAuth1(os.environ['apiKey'], os.environ['apiSecret'])
        endpoint = f"http://api.thenounproject.com/icon/{search_item}"

        response = requests.get(endpoint, auth=auth)
        print(response.content)
        data = {'response': json.loads(response.content)}
        return render(request, 'store/searchResult.html', data)
    
def footwear(request):
    return render(request, 'store/footwear.html', content)

def fitness(request):
    return render(request, 'store/fitness.html', content)

def electronics(request):
    return render(request, 'store/electronics.html', content)

def books(request):
    return render(request, 'store/books.html', content)

def cart(request):
    return render(request, 'store/cart.html')