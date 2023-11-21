from django.shortcuts import render
from djangodashdash import views
import django 
import json
import requests

# Create your views here.  
def all_repos(request):
    response = requests.get("https://api.github.com/repos/kickstartcoding/django-kcproject-starter")
    repos = response.json()
    context = {
        'name': "django-kcproject-starter",
        'size': 1004,
        'stargazers_count': 14,
        'watchers_count': 14,
        'github_repos': repos,
    }   
    return render(request, "allrepos.html", context)

def tables(request):
    return render_repos(request, "tables.html")

def charts(request):
    return render_repos(request, "charts.html")

def homepage(request):
    return render_repos(request, "homepage.html")

def render_repos(request, template_name):
    response = requests.get("https://api.github.com/repos/kickstartcoding/django-kcproject-starter")
    repos = response.json()
    context = {
        'name': "django-kcproject-starter",
        'size': 1004,
        'stargazers_count': 14,
        'watchers_count': 14,
        "github_repos": repos,
    }   
    return render(request, template_name, context)
