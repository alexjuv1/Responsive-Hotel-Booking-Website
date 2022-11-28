from django import forms

class roomForm(forms.Form):
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")

class roomRes(forms.Form):
    roomNum = forms.IntegerField(label = "roomnum")

class personalForm(forms.Form):
    firstName = forms.CharField(label = "First Name", max_length = 100)
    lastName = forms.CharField(label = "Last Name", max_length = 100)