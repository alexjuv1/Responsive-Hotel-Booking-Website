from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserUpdateForm
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST) 
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

def profile(response):
    if response.method == 'POST':
        u_form = UserUpdateForm(response.POST,instance=response.user)
        if u_form.is_valid():
            u_form.save()
            return redirect("/")
    else:
        u_form = UserUpdateForm(instance=response.user.profile)

    context={'u_form': u_form}
    return render(response, 'main/editprofile.html',context )