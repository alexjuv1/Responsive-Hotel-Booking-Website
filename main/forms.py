from django import forms

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