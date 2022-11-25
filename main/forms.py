from django import forms

class Reservation(forms.Form):
    smoking = forms.BooleanField()
    single = forms.CharField()
