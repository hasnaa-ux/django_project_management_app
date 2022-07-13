from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm , UserForm, ProfileForm
from django.contrib.auth import authenticate , login
from .decoraters import  unauthenicated_user , allowed_users
from amgad_app.models import *
from amgad_app.views import *
from amgad_app.urls import *
from .models import Profile
import sys
sys.setrecursionlimit(1500)
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    
    return render(request,'registration/signup.html',{'form':form})


@unauthenicated_user
def login(request):            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username= username,password=password)
        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            message.info(request, 'error')
    context = {}        
    return render(request,'pages\login.html', context)





def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    return render (request,'accounts/profile.html',{'profile':profile})
    




def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile/'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render (request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})



    