from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import User,Verification,Forgetpass
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import secrets
import json
import dashboard.views

# Create your views here.

def create_key():
   key = secrets.token_urlsafe(15)
   return str(key)

def verify(request, key):
    flag = Verification.objects.filter(key = key)
    if len(flag)==1:
        a = Verification.objects.get(key = key)
        id = a.email
        u = User.objects.get(email=id)
        u.is_active = True
        u.save()
        dl = Verification.objects.get(email = id)
        dl.delete()
        return redirect(log_in)
    return HttpResponse(404)

def log_out(request):
    logout(request)
    return redirect(log_in)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        login_user = authenticate(request,username=username, password=password)
        if login_user is not None:
            login(request, login_user)
            return redirect('/dashboard')
        else:
            messages.info(request,'Invalid Login')
    return render(request, 'home/login.html')

def register(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        mobile = request.POST["mobile"]
        confirm_pass = request.POST["confirmpassword"]
        if User.objects.filter(email = email).exists():
            messages.info(request,'Email Already Used')
            return redirect(register)
        if password != confirm_pass:
            messages.info(request,'password mismatch')
            return redirect(register)
        if password == confirm_pass:
            if User.objects.filter(email  = email).exists() == False:
                 usr = User.objects.create_user(email = email, password=password,name = name,mobile = mobile)
                 usr.save()
                 key = create_key()
                 print('127.0.0.1:8000/verify/'+str(key))
                 v = Verification()
                 v.email =email
                 v.key = key
                 v.save()
    return render(request, 'home/register.html')

#change password
def change_pass(request,key):
    flag = Forgetpass.objects.filter(key = key)
    id = 0
    if len(flag)==1:
       inst = Forgetpass.objects.get(key=key)
       email = inst.email
       if request.method == 'POST': 
          usr = User.objects.get(email = email)
          password = request.POST['password']
          conf_pass = request.POST['confirmpassword']
          if password == conf_pass:
             usr.set_password(password)
             usr.save()
             inst.delete()
             id = 1
             messages.info(request,'Password Change Success')
          else:
             messages.info(request,'Password Mismatch')
       dict = {'is_verified':1,'alert':id}
       return render(request, 'home/forget.html',context = dict)
    return HttpResponse('404')   

#forget password
def forget(request):
    if request.method == 'POST':
          email = request.POST['email']
          flag = User.objects.filter(email = email)
          if len(flag) == 1:
              key = create_key()
              f = Forgetpass()
              f.email = email
              f.key = key 
              f.save()
              print('127.0.0.1:8000/changepass/'+str(key))
              messages.info(request,'Email Sent')
          else:
              messages.info(request,'Email Not Registered')
              return redirect(forget)
    dict = {'is_verified':0}
    return render(request, 'home/forget.html',context = dict)

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/aboutus.html')

def loginas(request, uid):
    if request.user.is_superuser:
        user = User.objects.get(id=uid)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(dashboard.index)
    else:
        return redirect(log_out)