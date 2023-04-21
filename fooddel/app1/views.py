from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , logout , login as loginUser
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url="LoginPage")
def HomePage(request):
    return render(request, 'home.html')
def Signup(request):
    
    if request.method == 'POST':
        uname=request.POST.get('Name')
        email=request.POST.get("mail")
        dob=request.POST.get("dob")
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_p')
       
        if pass1!=pass2:
            return HttpResponse("p1 not equla to p2")
        else:
           my_user=User.objects.create_user(uname,email,pass1) 
           my_user.save()
           return redirect('LoginPage')
        
    
    return render(request, 'login.html')

def login(request):

       
    if request.method == 'POST':
         username = request.POST.get('uname') 
         password = request.POST.get('pass') 

         user = authenticate(request , username = username, password = password) 

         if user is not None:
            loginUser(request,user) 
            return redirect('HomePage') 
         else:
            return HttpResponse("User info Incorrect")
        
       
      
    return render(request, 'login.html')
   
def logoutPage(request):
    logout(request)
    
    return redirect('LoginPage')

def ksburger(request):
    return render(request,'ksbakers.html')


