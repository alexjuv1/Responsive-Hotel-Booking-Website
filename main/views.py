import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import users
from .models import reservation
from .forms import CreateNewList
from django.http import HttpResponseRedirect
#from .forms import RegisterForm
# Create your views here.

# def index(response, email, password):
#     ls = users.objects.get(email == email and password == password)
def index(response, id):
    ls = users.objects.get(id = id)
    #return HttpResponse("<h1>%s</h1>" % ls.first_name)
    return render(response, "main/viewUserData.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = users(first_name=n, age=0)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form" : form})

def profile(response):
    currentUser = response.user
    #ls = reservation.objects.filter(client_id = django.contrib.auth.get_user_model())
    ls = reservation.objects.filter(client_id = currentUser.id)
    D = {}
    #i = 1
    i = 0
    #TODO PASS ROOM ID IN DICTIONARY, figure out how to separate them in the for loop
    #SET THE KEY AS THE ROOM NUMBER AND SET THE VALUE AS A PAIR OF START AND END DATE
    # https://docs.djangoproject.com/en/4.1/ref/templates/builtins/
    #TODO in the profile, find a way to 
    for res in ls:
        D[i] = res
        i+=1
    #D[0] = i
    return render(response, "main/profile.html", {"ls": ls})