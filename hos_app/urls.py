from turtle import update
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

urlpatterns = [
    
    # path('', views.logindashboard,name='logindashboard'),
    path('logoutdashboard/', views.logoutdashboard,name='logoutdashboard'),
    path('',views.admin,name='admin'),
   
    
    path('searchbar', views.searchbar, name="searchbar"),
    path('depsearch', views.depsearch, name="depsearch"),
    path('docsearch', views.docsearch, name="docsearch"), 
    path('patsearch', views.patsearch, name="patsearch"), 
    path('empsearch', views.empsearch, name="empsearch"), 
    path('blosearch', views.blosearch, name="blosearch"), 
    path('roomsearch', views.roomsearch, name="roomsearch"), 
    path('machsearch', views.machsearch, name="machsearch"), 
    path('labsearch', views.labsearch, name="labsearch"),
    path('birthsearch', views.birthsearch, name="birthsearch"), 
    path('deathsearch', views.deathsearch, name="deathsearch"), 
    path('flosearch', views.flosearch, name="flosearch"), 
    path('invsearch', views.invsearch, name="invsearch"),
    
    
    
    
    
    # path('bed',views.bed,name='bed'),
    # path('bed_update/<int:Id>',views.bed_update,name='bed_update'),
    # path('bed_delete/<int:Id>',views.bed_delete,name='bed_delete'),
    
    
    
    path('birth',views.birth,name='birth'),
    path('birth_update/<int:Id>',views.birth_update,name='birth_update'),
    path('birth_delete/<int:Id>',views.birth_delete,name='birth_delete'),
    
    path('blood',views.blood,name='blood'),
    path('blood_update/<int:Id>',views.blood_update,name='blood_update'),
    path('blood_delete/<int:Id>',views.blood_delete,name='blood_delete'),
 
    
    path('death',views.death,name='death'),
    path('update/<int:Id>',views.update,name='update'),
    path('delete/<int:Id>',views.delete,name='delete'),
 
    
    path('medicine',views.medicine,name='medicine'),
    path('medicine_update/<int:Code>',views.medicine_update,name='medicine_update'),
    path('medicine_delete/<int:Code>',views.medicine_delete,name='medicine_delete'),
 
    
    path('department',views.department,name='department'),
    path('department_update/<int:Id>',views.department_update,name='department_update'),
    path('department_delete/<int:Id>',views.department_delete,name='department_delete'),
    
 
    path('doctor',views.doctor,name='doctor'),
    path('update_doctor/<int:Id>',views.doctor_update,name='doctor_update'),
    path('delete_doctor/<int:Id>',views.doctor_delete,name='doctor_delete'),
    
    
    path('employee',views.employee,name='employee'),
    path('employee_update/<int:Id>',views.employee_update,name='employee_update'),
    path('employee_delete/<int:Id>',views.employee_delete,name='employee_delete'),
    
    
    path('floor',views.floor,name='floor'),
    path('floor_update/<int:Id>',views.floor_update,name='floor_update'),
    path('floor_delete/<int:Id>',views.floor_delete,name='floor_delete'),
    
    
    path('machiens',views.machiens,name='machiens'),   
    path('machiens_update/<int:Id>',views.machiens_update,name='machiens_update'),
    path('machiens_delete/<int:Id>',views.machiens_delete,name='machiens_delete'),
    
    path('lab',views.lab,name='lab'),
    path('lab_update/<int:Code>',views.lab_update,name='lab_update'),
    path('lab_delete/<int:Code>',views.lab_delete,name='lab_delete'),
    
    
    
    
    path('invoice',views.invoice,name='invoice'),
    path('invoice_update/<int:Id>',views.invoice_update,name='invoice_update'),
    path('invoice_delete/<int:Id>',views.invoice_delete,name='invoice_delete'),
    
       
    path('patient',views.patient,name='patient'),
    path('patient_update/<int:Id>',views.patient_update,name='patient_update'),
    path('patient_delete/<int:Id>',views.patient_delete,name='patient_delete'),
    
    
    
    path('room',views.room,name='room'),
    path('room_update/<int:Id>',views.room_update,name='room_update'),
    path('room_delete/<int:Id>',views.room_delete,name='room_delete'),
]
