from django.shortcuts import render
from django.http import HttpResponse
from .models import users
# Create your views here.

def index(response, id):
    ls = users.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.first_name)
