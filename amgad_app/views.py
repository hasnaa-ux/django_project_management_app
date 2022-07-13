import re
from os import path
from django.conf import settings
from django.shortcuts import redirect, render
from .models import  *
from .forms import  *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# from accounts.decoraters import  unauthenicated_user , allowed_users
from hos_app.models import *

import sys
sys.setrecursionlimit(1500)

# Create your views here.

def index(request):
    context = {
        'doctors': Doctor.objects.all(),
    }
    myInfo = Info.objects.first()
    if request.method=='POST':
        email = request.POST['email']
        subject =request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    
    return render(request,'pages\index.html',{'context':context,'myInfo':myInfo})


""" def signup(request):
    if request.method == 'POST':
        AdminName = request.POST.get('name')
        AdminMail = request.POST.get('email')
        AdminUserName = request.POST.get('username')
        AdminPassword = request.POST.get('password')
        data = SignUp(name=AdminName , email=AdminMail , username=AdminUserName , password=AdminPassword)
        data.save()
    return render(request,'pages\signup.html') """



""" @unauthenicated_user
def login(request):            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username= username,password=password)
        if user is not None:
            login(request , user)
            return redirect('index')
            
    return render(request,'pages\login.html') """








@login_required
def appointment(request):
    if request.method == 'POST':
        Your_Name = request.POST.get('name')
        Youe_Email = request.POST.get('email')
        Your_Phone = request.POST.get('phone')
        Your_Date = request.POST.get('date')
        Your_Message = request.POST.get('message')
        Your_Department = request.POST.get('department')
        Your_Doctor = request.POST.get('doctor')
        DATA = Appointment(YourName=Your_Name,YourEmail=Youe_Email,YourPhone=Your_Phone,YourDate=Your_Date,YourMessage=Your_Message,YourDepartment=Your_Department,YourDoctor=Your_Doctor)
        DATA.save()
    
    context = {
    'appointment' : Appointment.objects.all(),
    'appointment_form' : AppointmentForm(),
    }
        
    return render(request,'pages\\appointment.html',context)