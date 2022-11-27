from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
from django.db import models


class RegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]\

class roomForm(forms.Form):
    smoking = forms.BooleanField(label = "smoking")
    single = forms.BooleanField(label = "single")