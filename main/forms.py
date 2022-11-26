from django import forms

class Reservation(forms.Form):
    smoking = forms.CharField(label="Smoking", max_length=200)
    single = forms.CharField()
