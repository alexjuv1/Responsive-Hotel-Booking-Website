import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import roomForm
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
#import datetime
from datetime import *
from django.views.generic.edit import UpdateView
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

def viewRoom(response):
    room_number = response.POST.get("room_numb")
    ls = room.objects.get(room_number = room_number)
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
        startTime = datetime(response.POST.get("start_date"))
        endTime = datetime(response.POST.get("end_date"))
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
            q = reservation.objects.filter(room_number = x.room_number)
            #, end_date1__gte=startTime)
            #.exclude(start_date1__gte=endTime)
                #available = True
            if not q:
                    # L[i] = x
                    # i+=1
                    #if no collisions,
                D[x.room_number] = x
        #return render(response, "main/reservationPage.html", {"ls": D})
        return render(response, "main/reservationPage.html", {"ls": D})
        return render(response, "main/reservationPage.html", {"ls": ls})
        # else:
        #     return render(response, "main/selectRoomTemp.html", {})
    #else:
        #return render(response, "main/selectRoomTemp.html", {})

def isRoomValid(roomID, startDate, endDate):
    q = reservation.objects.filter(room_id = roomID)
    for x in q:
        if(x.start_date1 <= datetime.date(startDate)):
            if(x.end_date1 > datetime.date(startDate)):
                return False
        elif(x.start_date1 <= datetime.date(endDate)):
            return False
    return True

def selectDateOnly(response, id):
    return render(response, "main/selectDate.html", {"room_id": id})

def calculatePrice(response, id):
    if(response.method == "POST"):
        form = reserveRoomDateOnly(response.POST)
        formDict = form.data
        if 'start_date' in response.POST and 'end_date' in response.POST:
            date1 = formDict['start_date']
            #print(date1)
            date1Con = datetime.strptime(date1, "%Y-%m-%d")
            dateFormat = date1Con.strftime('%d-%m-%Y')
            startTime = datetime.strptime(dateFormat, "%d-%m-%Y")

            date2 = formDict["end_date"]
            date2Con = datetime.strptime(date2, "%Y-%m-%d")
            date2Format = date2Con.strftime('%d-%m-%Y')
            endTime = datetime.strptime(date2Format, "%d-%m-%Y")
        
        start = (((startTime.year * 100) + startTime.month) * 100 + startTime.day)
        end = (((endTime.year * 100) + endTime.month) * 100 + endTime.day)

        requestedRoom = room.objects.get(room_number = id)

        if(startTime > endTime or datetime.date(startTime) < date.today()):
            return render(response, "main/invalidDateInputs.html", {})
        
        if(not isRoomValid(requestedRoom.id, startTime, endTime)):
            return render(response, "main/invalidDateInputs.html", {})
        
        totalLength = endTime - startTime
        finalPrice = (totalLength.days + 1) * requestedRoom.price_per_night
        
        return render(response, "main/finalPrice.html", {"start": start, "end": end, "room": requestedRoom, "total_price": finalPrice})
    # else:
    #     startTime = startDate
    #     endTime = endDate
    # D = {}
    # D["room"] = requestedRoom
    # D["price"] = requestedRoom.price_per_night * lengthOfStay
    # return render()

def reservationFunction2(response):
    D = {}
    #if response is post / form was submitted
    L = [] * 100
    if not response.user.is_authenticated:
        return redirect("/login/")
    if response.method == "POST":
        # i = 0
        form = reservationForm(response.POST)
        #check that the form is valid (all inputs are valid)
        #if form.is_valid():
            #get start time, end time, smoking, and single info from form
        formDict = form.data
        if 'start_date' in response.POST and 'end_date' in response.POST:
            date1 = formDict['start_date']
            print(date1)
            date1Con = datetime.strptime(date1, "%Y-%m-%d")
            dateFormat = date1Con.strftime('%d-%m-%Y')
            startTime = datetime.strptime(dateFormat, "%d-%m-%Y")

            date2 = formDict["end_date"]
            date2Con = datetime.strptime(date2, "%Y-%m-%d")
            date2Format = date2Con.strftime('%d-%m-%Y')
            endTime = datetime.strptime(date2Format, "%d-%m-%Y")

        #startTime = response.POST.get("start_date")
        #endTime = response.POST.get("end_date")
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
        
        if(startTime > endTime or datetime.date(startTime) < date.today()):
            return render(response, "main/invalidDateInputs.html", {})
        for x in ls:
            if(isRoomValid(x.id, startTime, endTime)):
                # L[i] = x
                #D[x.room_number] = x
                D[x] = x.room_number
                # i+=1
        start = (((startTime.year * 100) + startTime.month) * 100 + startTime.day)
        end = (((endTime.year * 100) + endTime.month) * 100 + endTime.day)
        
        return render(response, "main/reservationPage.html", {"start": start, "end": end, "D": D})
        

def selectRoomTemp(response):
    return render(response, "main/selectRoomTemp.html", {})

# def bookRoomFinal(response, id, start_year, start_month, start_day, end_year, end_month, end_day):
#     currentUser = response.user
#     # if(response.method == "POST"):
#     #     startTime = response.POST.get("start_date")
#     #     endTime = response.POST.get("end_date")
#     #     id = response.POST.get("roomID")
#     #     r = reservation(room_id = id, client_id = currentUser, start_date1 = startTime, end_date1 = endTime)
    
    

#         #TODO add to reservation table

def calculateInvoice(response, id, start, end):
    temp = start
    startDay = (int)(temp % 100)
    temp = (temp - startDay) / 100
    startMonth = (int)(temp % 100)
    temp = (temp - startMonth) / 100
    startYear = (int)(temp)

    temp = end
    endDay = (int)(temp % 100)
    temp = (temp - endDay) / 100
    endMonth = (int)(temp % 100)
    temp = (temp - endMonth) / 100
    endYear = (int)(temp)

    startDate = datetime(year=startYear, month=startMonth, day=startDay)
    endDate = datetime(year=endYear, month=endMonth, day=endDay)
    currentRoom = room.objects.get(id = id)

    totalStayLength = endDate - startDate
    totalPrice = (totalStayLength.days + 1) * currentRoom.price_per_night

    return render(response, "main/finalPrice.html", {"start": start, "end": end, "room": currentRoom, "total_price": totalPrice})


def bookRoomFinal(response, id, start, end):
    currentUser = response.user
    startDay = (int)(start % 100)
    start = (start - startDay) / 100
    startMonth = (int)(start % 100)
    start = (start - startMonth) / 100
    startYear = (int)(start)

    endDay = (int)(end % 100)
    end = (end - endDay) / 100
    endMonth = (int)(end % 100)
    end = (end - endMonth) / 100
    endYear = (int)(end)

    startDate = datetime(year=startYear, month=startMonth, day=startDay)
    endDate = datetime(year=endYear, month=endMonth, day=endDay)
    currentRoom = room.objects.get(id = id)
    newReservation = reservation(room_id = currentRoom, client_id = currentUser, start_date1 = startDate, end_date1 = endDate)
    newReservation.save()

    return render(response, "main/mkTemp.html", {"startDay": startDay, "startMonth": startMonth, "startYear": startYear, "endDay": endDay, "endMonth": endMonth, "endYear": endYear, "id": id})
    return render(response, "main/book.html", {"start_time":startTime, "end_time":endTime})

    
def history(response):
    D = {}
    ls = reservation.objects.get()

def editProfile(response):
    user = response.user
    return render(response, "main/editprofile.html", {"ls":user})

def saveChanges(response):
    x = response.user
    x.set_username = response.POST.get("username")
    x.set_first_name = response.POST.get("first_name")
    x.set_last_name = response.POST.get("last_name")
    x.set_email = response.POST.get("new_email")
    x.save()
    return render(response, "main/homepages.html", {"ls":x})