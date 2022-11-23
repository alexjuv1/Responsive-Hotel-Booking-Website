from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from gfg import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == 'POST':
        #username = request.POST.get('Username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('home')
        if len(username)>20:
            messages.error(request, "Username must be under 20 characters")    
        if password != confirmpassword:
            messages.error(request,"Passwords do not match!")
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account has been successfully created. We have sent you a confirmation email")

        #WELCOME EMAIL

        subject = "Welcome to our Hotel"
        message = "HELLO " + myuser.username + " !! \n" + "Thank you for visiting our website \n We have sent you a confirmation email, please confirm your email address in order to activate your account. \n\n   Thank You" 
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        #Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ Hotel Login"
        message2 = render_to_string('emailconfirmation.html',{
            'name' :myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()


        return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):
    
    if request.method == 'Post':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password = password)   
        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Wrong Info!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request,'activationfailed.html')    
    