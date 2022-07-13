from pickle import NONE
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from amgad_app.models import *
from amgad_app.views import *
from amgad_app.urls import *
import sys
sys.setrecursionlimit(1500)



def unauthenicated_user(view_func):
    def wrapper_func(request , *args, **kwargs):        
        if request.user.is_authenticated:
           return redirect('index')
        else:
            return view_func(request , *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request , *args, **kwargs):            
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
               
            if group in allowed_roles:   
                return view_func(request , *args, **kwargs)
            
            else:
                return render(request,'pages\index.html')
        return wrapper_func
    return decorator


def admins_only(view_func):
    def wrapper_function(request , *args, **kwargs):            
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
               
            if group =="users":   
                return render(request,'pages\index.html')
            
            if group =="admin":   
                return view_func(request , *args, **kwargs)
    return wrapper_function
   


