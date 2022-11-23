from django.shortcuts import render
from django.http import HttpResponse
from .models import users, room
# Create your views here.

def index(response, id):
    a = users.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % a.first_name)
