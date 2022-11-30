import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import roomForm
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from django.db.models import F

#def verifyAccount():

#from .forms import RegisterForm
# Create your views here.

# def index(response, email, password):
#     ls = users.objects.get(email == email and password == password)
def index(response, id):
    ls = room.objects.get(room_number=id)
    return render(response, "main/viewRoom.html", {"ls": ls})

def home(response):
    D = {}
    currentUser = response.user
    if currentUser.is_authenticated:
        D["username"] = response.user.username
        D["first_name"] = response.user.first_name
        D["last_name"] = response.user.last_name
        D["email"] = response.user.email
        return render(response, "main/homepages.html", D)
    else:
        return render(response, "main/homepages.html", D)
    

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


def confirmationPage(response, start_date, end_date):
    currentUser = response.user 
    start_date = response.POST.get("start_date")
    end_date = response.POST.get("end_date")
    return render(response, "main/confirmationPage.html")

def profile(response):
    currentUser = response.user 
    if(users.objects.filter(django_id = currentUser).exists()):
        exists = True
        ourTableUser = users.objects.get(django_id = currentUser)
        #ourTableUserList = users.objects.filter(django_id = currentUser)
        #for()
    else:
        ourTableUser = users(first_name = "UNKNOWN", last_name = "UNKNOWN", django_id = currentUser)
        ourTableUser.save()
        #exists = False
        exists = True
    
    D = {}
    #D["username"] = currentUser.username
    #D["djangoID"] = currentUser.id
    D["username"] = currentUser.username
    if(exists):
        D["firstName"] = ourTableUser.first_name
        D["lastName"] = ourTableUser.last_name
        D["hotelID"] = ourTableUser.id
    else:
        D["firstName"] = "No First Name Given"
        D["lastName"] = "No Last Name Given"
        D["hotelID"] = -1
    #ls = reservation.objects.filter(client_id = django.contrib.auth.get_user_model())
    ls = reservation.objects.filter(client_id = currentUser.id)

    D[ls] = ls

    #D = {}
    #i = 1
    #i = 0
    #TODO PASS ROOM ID IN DICTIONARY, figure out how to separate them in the for loop
    #SET THE KEY AS THE ROOM NUMBER AND SET THE VALUE AS A PAIR OF START AND END DATE
    # https://docs.djangoproject.com/en/4.1/ref/templates/builtins/
    #TODO in the profile, find a way to 
    # for res in ls:
    #     x = room.objects.get(id = res.room_id)
    #     D[x.room_number] = res
        #i+=1
    #D[0] = i
    # D[0] = currentUser.first_name
    # D[1] = currentUser.last_name
    #return render(response, "main/profile.html", {"firstName": currentUser.first_name, "lastName": currentUser.last_name, "ls": ls})
    #return render(response, "main/profile.html", {"username": currentUser.username, "firstName": ourTableUser.first_name, "lastName": ourTableUser.last_name, "ls": ls})
    return render(response, "main/profile.html", D)

def modifyInfo(response, id):
    D = {}
    if response.method == "POST":
        form = personalForm(response.POST)
        if(form.is_valid()):
            #x = users(first_name = form.firstName, last_name = form.lastName, djangoID = response.user.id)
            #x.save()
            x = users.get
def viewProfile(response):
    D = {}
    currentUser = response.User
    if(users.objects.filter(username = currentUser.username).exists()):
        ourDB = users.objects.get(username = currentUser.username)
    else:
        ourDB = users(first_name = "UNKNOWN", last_name = "UNKNOWN", username = currentUser.username)
    D["username"] = ourDB.username
    D["first_name"] = ourDB.first_name
    D["last_name"] = ourDB.last_name
    D["email"] = currentUser.email
    return render(response, "", D)

def viewRoom(response, id):
    room_num = id
    ls = room.objects.get(room_number = id)
    return render(response, "main/availability.html", {"room":ls})

def reservationFunction(response):
    D = {}
    #if response is post / form was submitted
    L = [] * 100
    if response.method == "POST":
        form = reservationForm(response.POST)
        #check that the form is valid (all inputs are valid)
        #if form.is_valid():
            #get start time, end time, smoking, and single info from form
        startTime = response.POST.get("start_date")
        endTime = response.POST.get("end_date")
        smoking = response.POST.get("Smoking")
        single = response.POST.get("Single")
        if (single == "True" and smoking == "True"):
            ls = room.objects.filter(smoking = True, single = True)
        elif (single == "True" and smoking == "False"):
            ls = room.objects.filter(smoking = True, single = False)
        elif (single == "False" and smoking == "True"):
            ls = room.objects.filter(smoking = False, single = True)
        else:
            ls = room.objects.filter(smoking = False, single = False)


            #filter all the rooms that match the requirements (apart from reservation dates)
        

        i = 0

            #for each room, check if reservation date coincides with an existing reservation
        for x in ls:
                #q = reservation.objects.filter(room_id = x.id).filter(end_time__gte=startTime).exclude(end_time__gte=endTime)
                #starts before end time, and ends after start time = collision
            q = reservation.objects.filter(room_id = x.id).filter(end_date1__gte=startTime).exclude(start_date1__gte=endTime)
                #available = True
            if not q:
                    # L[i] = x
                    # i+=1
                    #if no collisions,
                D[x.room_number] = x
            return render(response, "main/reservationPage.html", {"ls": D})
        return render(response, "main/reservationPage.html", {"ls": ls})
        # else:
        #     return render(response, "main/selectRoomTemp.html", {})
    #else:
        #return render(response, "main/selectRoomTemp.html", {})


def selectRoomTemp(response):
    return render(response, "main/selectRoomTemp.html", {})
def history(response):
    D = {}
    ls = reservation.objects.get()