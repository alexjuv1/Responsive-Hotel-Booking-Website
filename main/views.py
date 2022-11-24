from django.shortcuts import render
from django.http import HttpResponse
from .models import users
# Create your views here.

# def index(response, email, password):
#     ls = users.objects.get(email == email and password == password)
def index(response, id):
    ls = users.objects.get(id = id)
    #return HttpResponse("<h1>%s</h1>" % ls.first_name)
    return render(response, "main/viewUserData.html", {"ls": ls})

def home(response):

    return render(response, "main/home.html", {})