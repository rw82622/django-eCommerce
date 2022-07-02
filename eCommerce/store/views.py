from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os
import json



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
    return render(request, 'store/footwear.html')

def clothes(request):
    return render(request, 'store/clothes.html')

def electronics(request):
    return render(request, 'store/electronics.html')

def cart(request):
    return render(request, 'store/cart.html')