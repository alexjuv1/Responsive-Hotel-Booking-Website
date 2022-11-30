from django import forms
from django.contrib.auth.models import User 

class roomForm(forms.Form):
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")
    start_date = forms.DateField(label = "start_date")
    end_date = forms.DateField(label = "end_date")

class roomRes(forms.Form):
    roomNum = forms.IntegerField(label = "roomnum")

class DateInput(forms.DateInput):
    input_type = 'date'

class personalForm(forms.Form):
    firstName = forms.CharField(label = "First Name", max_length = 100)
    lastName = forms.CharField(label = "Last Name", max_length = 100)

class reservationForm(forms.Form):
    start_date = forms.DateField(widget = DateInput, label = "start_date", required = True)
    end_date = forms.DateField(widget = DateInput, label = "end_date", required = True)
    smoking = forms.BooleanField(label = "smoking", initial=False)
    single = forms.BooleanField(label = "single", initial=False)

class reservationDateHidden(forms.Form):
    start_date = forms.DateField(widget = forms.HiddenInput(), label = "start_date")
    end_date = forms.DateField(widget = forms.HiddenInput(), label = "end_date")
    roomID = forms.IntegerField(widget = forms.HiddenInput(), label = "roomID")

class roomNumb(forms.Form):
    room_numb = forms.IntegerField(label = "room_numb")

class usernamePass(forms.Form):
    username = forms.CharField(label = "username")


class reserveRoomDateOnly(forms.Form):
    start_date = forms.DateField(widget = DateInput, label = "start_date")
    end_date = forms.DateField(widget = DateInput, label = "end_date")