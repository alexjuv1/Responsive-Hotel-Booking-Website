from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import roomForm
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

def create(response):
    if response.method == "POST":
        form = roomForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = testmod(test1=n)
            t.save()
            response.user.tmod.add(t)
            

        return HttpResponseRedirect("/")

    else:
        form = roomForm()
    return render(response, "main/reservation.html", {"form" : form})

def roomShow(response):
    smoking = response.POST.get('Smoking', False)
    single = response.POST.get('Single', False)
    rooms = room.objects.all()
    return render(response, "main/roomShow.html", {"smoking":smoking, "single":single, "rooms":rooms}) 

def checkOut(response):
    roomid = response.POST.get('roomnum')
    roomObj = room.objects.get(room_number = roomid)
    return render(response, "main/checkOut.html", {"roomObj":roomObj})

def view(response):

    return render(response, "main/view.html")

def reserve(response):
    return render(response, "main/reservation.html")

