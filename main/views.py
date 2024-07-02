from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
date = datetime.now()

# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        try:
            validate_password(password)
            if password==password1:
                
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username is already exists!!!")
                    return redirect('register')
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email is already exists!!!")
                    return redirect('register')
                
                else:
                    User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    messages.success(request,'success')
                    return redirect('register')
            
            else:
                messages.error(request,'password is not match!!!')
                return redirect('register')
        except ValidationError as e:
            for error in e.messages:
                messages.error(request,error)
                return redirect('register')
            
    return render(request,'auth/register.html')



def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"Login is sucessfully  !!! ")

            return redirect('index')
        
        messages.error(request,'Username not match !!! ')

    return render(request,'auth/login.html')

def change_password(request):
    return render(request,'auth/change_password.html')