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