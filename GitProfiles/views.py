from django.http import HttpResponse
from django.shortcuts import render

import requests
import json

def home(request):
    return render(request,"home.html")


username = "Use-your-username"
token =    "generate-your-token"

def results(request):
    query = request.GET['username']
    print(query)
    url = '''https://api.github.com/users/''' + query
    r = requests.get(url,auth=(username,token))
    jsonObject = json.loads(r.text)

    print(jsonObject)

    return render(request,"results.html",context={"api":jsonObject})
