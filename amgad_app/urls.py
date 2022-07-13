from django.urls import path 
from . import views


urlpatterns = [

    path('',views.index,name='index'),
    
    # path('logins',views.login,name='logins'),
    
    # path('signup',views.signup,name='signup'),
    
    path('appointment',views.appointment,name='appointment'),


]