from django import forms

class roomForm(forms.Form):
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")

class roomRes(forms.Form):
    roomNum = forms.IntegerField(label = "roomnum")

class DateInput(forms.DateInput):
    input_type = 'date'

class reservationTimes(forms.Form):
    start_date = forms.DateField(widget = DateInput, label = "start_date")
    end_date = forms.DateField(widget= DateInput , label = "end_date")

class personalForm(forms.Form):
    firstName = forms.CharField(label = "First Name", max_length = 100)
    lastName = forms.CharField(label = "Last Name", max_length = 100)

class reservationForm(forms.Form):
    start_date = forms.DateField(widget = DateInput, label = "start_date")
    end_date = forms.DateField(widget = DateInput, label = "end_date")
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")