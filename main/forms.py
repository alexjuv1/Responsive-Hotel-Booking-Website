from django import forms

class roomForm(forms.Form):
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")

class roomRes(forms.Form):
    roomNum = forms.IntegerField(label = "roomnum")