import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import roomForm
from .forms import *
from django.http import HttpResponseRedirect
#from .forms import RegisterForm
# Create your views here.

# def index(response, email, password):
#     ls = users.objects.get(email == email and password == password)
def index(response, id):
    ls = room.objects.get(room_number=id)
    return render(response, "main/viewRoom.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def roomShow(response):
    smoking = response.POST.get('Smoking', False)
    single = response.POST.get('Single', False)
    rooms = room.objects.all()
    return render(response, "main/roomShow.html", {"smoking":smoking, "single":single, "rooms":rooms}) 

def checkOut(response, id):
    form = response.POST.get
    roomObj = room.objects.get(room_number = id)
    return render(response, "main/checkOut.html", {"roomObj":roomObj, })

def view(response):

    return render(response, "main/view.html")

def reserve(response):
    return render(response, "main/reservation.html")


def confirmationPage(response):
    currentUser = response.user 
    return render(response, "main/confirmationPage.html")

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