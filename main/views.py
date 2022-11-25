from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CreateNewList
from django.http import HttpResponseRedirect
#from .forms import RegisterForm
# Create your views here.

# def index(response, email, password):
#     ls = users.objects.get(email == email and password == password)
def index(response, id):
    ls = User.objects.get(id = id)
    #return HttpResponse("<h1>%s</h1>" % ls.first_name)
    return render(response, "main/viewUserData.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = testmod(test1=n)
            t.save()
            response.user.tmod.add(t)
            

        return HttpResponseRedirect("/")

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form" : form})

def view(response):
    return render(response, "main/view.html")

def reserve(response):
    return render(response, "main/reservation.html")

