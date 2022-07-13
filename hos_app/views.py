from ast import IsNot
from audioop import add
from email import message
from multiprocessing import context
from telnetlib import LOGOUT
from django.urls import reverse 
from tkinter import Label
from tokenize import Name
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from accounts.decoraters import  unauthenicated_user , allowed_users , admins_only

import sys
sys.setrecursionlimit(1500)




# Create your views here.


 
@allowed_users(allowed_roles=['admin']) 
def admin(request):
     return render(request, 'pages/admin.html')
 

 
#-----------------------------bed---------------------------#
# def bed(request):
#     if request.method == "POST" :
#        add_bed= BedForm(request.POST)
#        if add_bed.is_valid():
#             add_bed.save()
    
#     context = {
#         'bed' : Bed.objects.all(),
#         'bed_form' : BedForm(),
#     }
#     return render(request, 'pages/bed.html',context)

# def bed_update(request,Id):
#     bed_id = Birth.objects.get(Id = Id)
#     if request.method == "POST" :
#         edit_bed = BedForm(request.POST,instance=bed_id)
#         if edit_bed.is_valid():
#             edit_bed.save()
#             return redirect('/bed')
#     else:
#         edit_bed = BedForm(instance=bed_id)
#     context = {
#         'bed_form':edit_bed
#     }            
#     return render(request, 'pages/bed_update.html',context)

# def bed_delete(request,Id):
#     bed_delete = Bed.objects.get(Id=Id)
#     if request.method == "POST" :
#         bed_delete.delete()
#         return redirect('/bed')
#     return render(request, 'pages/bed_delete.html')




#-----------------------------birth---------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def birth(request):
    if request.method == "POST" :
       add_birth= BirthForm(request.POST)
       if add_birth.is_valid():
            add_birth.save()
    
    context = {
        'birth' : Birth.objects.all(),
        'birth_form' : BirthForm(),
    }
    return render(request, 'pages/birth.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def birth_update(request,Id):
    birth_id = Birth.objects.get(Id = Id)
    if request.method == "POST" :
        edit_birth = BirthForm(request.POST,instance=birth_id)
        if edit_birth.is_valid():
            edit_birth.save()
            return redirect('/myadmin/birth')
    else:
        edit_birth = BirthForm(instance=birth_id)
    context = {
        'birth_form':edit_birth
    }            
    return render(request, 'pages/birth_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def birth_delete(request,Id):
    birth_delete = Birth.objects.get(Id=Id)
    if request.method == "POST" :
        birth_delete.delete()
        return redirect('/myadmin/birth')
    return render(request, 'pages/birth_delete.html')





#-------------------------blood------------------#

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def blood(request):
    
    if request.method == "POST" :
       add_blood = BloodForm(request.POST)
       if add_blood.is_valid():
            add_blood.save()
    
    context = {
        'blood' : Blood.objects.all(),
        'blood_form' : BloodForm(),
    }
    return render(request, 'pages/blood.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def blood_update(request,Id):
    blood_id = Blood.objects.get(Id = Id)
    if request.method == "POST" :
        edit_blood = BloodForm(request.POST,instance=blood_id)
        if edit_blood.is_valid():
            edit_blood.save()
            return redirect('/myadmin/blood')
    else:
        edit_blood = BloodForm(instance=blood_id)
    context = {
        'blood_form':edit_blood
    }            
    return render(request, 'pages/blood_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def blood_delete(request,Id):
    blood_delete = Blood.objects.get(Id=Id)
    if request.method == "POST" :
        blood_delete.delete()
        return redirect('/myadmin/blood')
    return render(request, 'pages/blood_delete.html')





#----------------------------death--------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def death(request):
    
    if request.method == "POST" :
       add_death = DeathForm(request.POST)
       if add_death.is_valid():
            add_death.save()
    
    context = {
        'death' : Death.objects.all(),
        'form' : DeathForm(),
    }
    
    return render(request, 'pages/death.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def update(request,Id):
    death_id = Death.objects.get(Id = Id)
    if request.method == "POST" :
        edit_death = DeathForm(request.POST,instance=death_id)
        if edit_death.is_valid():
            edit_death.save()
            return redirect('/myadmin/death')
    else:
        edit_death = DeathForm(instance=death_id)
    context = {
        'form':edit_death
    }            
    return render(request, 'pages/update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def delete(request,Id):
    death_delete = Death.objects.get(Id = Id)
    if request.method == "POST" :
        death_delete.delete()
        return redirect('/myadmin/death')
    return render(request, 'pages/delete.html')


#-----------------------------department---------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 
def department(request):
    if request.method == "POST" :
       add_department = DepartmentForm(request.POST)
       if add_department.is_valid():
            add_department.save()
    
    context = {
        'department' : Department.objects.all(),
        'department_form' : DepartmentForm(),
    }
    
    return render(request, 'pages/department.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 
  
def department_update(request,Id):
    department_id = Department.objects.get(Id = Id)
    if request.method == "POST" :
        edit_department = DepartmentForm(request.POST,instance=department_id)
        if edit_department.is_valid():
            edit_department.save()
            return redirect('/myadmin/department')
    else:
        edit_department = DepartmentForm(instance=department_id)
    context = {
        'department_form':edit_department
    }            
    return render(request, 'pages/department_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def department_delete(request,Id):
    department_delete = Department.objects.get(Id = Id)
    if request.method == "POST" :
        department_delete.delete()
        return redirect('/myadmin/department')
    return render(request, 'pages/department_delete.html')



#---------------------------doctor---------------------#

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def doctor(request):
    if request.method == "POST" :
       add_doctor = DoctorForm(request.POST)
       if add_doctor.is_valid():
            add_doctor.save()
    
    context = {
        'doctor' : Doctor.objects.all(),
        'doctor_form' : DoctorForm(),
    }
    return render(request,'pages/doctor.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def doctor_update(request,Id):
    doctor_id = Doctor.objects.get(Id = Id)
    if request.method == "POST" :
        edit_doctor = DoctorForm(request.POST,instance=doctor_id)
        if edit_doctor.is_valid():
            edit_doctor.save()
            return redirect('/myadmin/doctor')
    else:
        edit_doctor = DoctorForm(instance=doctor_id)
    context = {
        'doctor_form':edit_doctor
    }            
    return render(request, 'pages/doctor_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def doctor_delete(request,Id):
    doctor_delete = Doctor.objects.get(Id = Id)
    if request.method == "POST" :
        doctor_delete.delete()
        return redirect('/myadmin/doctor')
    return render(request, 'pages/doctor_delete.html')




#---------------------------employee------------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def employee(request):
    if request.method == "POST" :
       add_employee = EmployeeForm(request.POST)
       if add_employee.is_valid():
            add_employee.save()
    
    context = {
        'employee' : Employee.objects.all(),
        'employee_form' : EmployeeForm(),
    }
    return render(request,'pages/employee.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def employee_update(request,Id):
    employee_id = Employee.objects.get(Id = Id)
    if request.method == "POST" :
        edit_employee = EmployeeForm(request.POST,instance=employee_id)
        if edit_employee.is_valid():
            edit_employee.save()
            return redirect('/myadmin/employee')
    else:
        edit_employee = EmployeeForm(instance=employee_id)
    context = {
        'employee_form':edit_employee
    }            
    return render(request, 'pages/employee_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def employee_delete(request,Id):
    employee_delete = Employee.objects.get(Id = Id)
    if request.method == "POST" :
        employee_delete.delete()
        return redirect('/myadmin/employee')
    return render(request, 'pages/employee_delete.html')

#-------------------------------floor------------------------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def floor(request):
    if request.method == "POST" :
       add_floor = FloorForm(request.POST)
       if add_floor.is_valid():
            add_floor.save()
    
    context = {
        'floor' : Floor.objects.all(),
        'floor_form' : FloorForm(),
    }
    return render(request,'pages/floor.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def floor_update(request,Id):
    floor_id = Floor.objects.get(Id = Id)
    if request.method == "POST" :
        edit_floor = FloorForm(request.POST,instance=floor_id)
        if edit_floor.is_valid():
            edit_floor.save()
            return redirect('/myadmin/floor')
    else:
        edit_floor = FloorForm(instance=floor_id)
    context = {
        'floor_form':edit_floor
    }            
    return render(request, 'pages/floor_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def floor_delete(request,Id):
    floor_delete = Floor.objects.get(Id = Id)
    if request.method == "POST" :
        floor_delete.delete()
        return redirect('/myadmin/floor')
    return render(request, 'pages/floor_delete.html')




#-------------------------------Lab------------------------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def lab(request):
    if request.method == "POST" :
       add_lab = LabForm(request.POST)
       if add_lab.is_valid():
            add_lab.save()
    
    context = {
        'lab' : Lab.objects.all(),
        'lab_form' : LabForm(),
    }
    return render(request,'pages/lab.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def lab_update(request,Id):
    lab_id = Lab.objects.get(Id = Id)
    if request.method == "POST" :
        edit_lab = LabForm(request.POST,instance=lab_id)
        if edit_lab.is_valid():
            edit_lab.save()
            return redirect('/myadmin/lab')
    else:
        edit_lab = LabForm(instance=lab_id)
    context = {
        'floor_form':edit_lab
    }            
    return render(request, 'pages/lab_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def lab_delete(request,Id):
    lab_delete = Floor.objects.get(Id = Id)
    if request.method == "POST" :
        lab_delete.delete()
        return redirect('/myadmin/lab')
    return render(request, 'pages/lab_delete.html')



#---------------------machiens---------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def machiens(request):    
    if request.method == "POST" :
       add_machiens = MachiensForm(request.POST)
       if add_machiens.is_valid():
            add_machiens.save()
    
    context = {
        'machiens' : Machiens.objects.all(),
        'mach_form' : MachiensForm(),
    }
    return render(request, 'pages/machiens.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def machiens_update(request,Id):
    machiens_id = Machiens.objects.get(Id = Id)
    if request.method == "POST" :
        edit_machiens= MachiensForm(request.POST,instance=machiens_id)
        if edit_machiens.is_valid():
            edit_machiens.save()
            return redirect('/myadmin/machiens')
    else:
        edit_machiens = MachiensForm(instance=machiens_id)
    context = {
        'mach_form':edit_machiens
    }            
    return render(request, 'pages/machiens_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def machiens_delete(request,Id):
    machiens_delete = Machiens.objects.get(Id = Id)
    if request.method == "POST" :
        machiens_delete.delete()
        return redirect('/myadmin/machiens')
    return render(request, 'pages/machiens_delete.html')
 


#-------------------medicine---------------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def medicine(request):
    
    if request.method == "POST" :
       add_medicine = MedicineForm(request.POST)
       if add_medicine.is_valid():
            add_medicine.save()
    
    context = {
        'medicine' : Medicine.objects.all(),
        'medicine_form' : MedicineForm(),
    }
    return render(request, 'pages/medicine.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def medicine_update(request,Code):
    medicine_code = Medicine.objects.get(Code = Code)
    if request.method == "POST" :
        edit_medicine = MedicineForm(request.POST,instance=medicine_code)
        if edit_medicine.is_valid():
            edit_medicine.save()
            return redirect('/myadmin/medicine')
    else:
        edit_medicine = MedicineForm(instance=medicine_code)
    context = {
        'medicine_form':edit_medicine
    }            
    return render(request, 'pages/medicine_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def medicine_delete(request,Code):
    medicine_delete = Medicine.objects.get(Code = Code)
    if request.method == "POST" :
        medicine_delete.delete()
        return redirect('/myadmin/medicine')
    return render(request, 'pages/medicine_delete.html')



#-------------------patient--------------------------#

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def patient(request):
    if request.method == "POST" :
       add_patient = PatientForm(request.POST)
       if add_patient.is_valid():
            add_patient.save()
    
    context = {
        'patient' : Patient.objects.all(),
        'patient_form' : PatientForm(),
    }
    return render(request,'pages/patient.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def patient_update(request,Id):
    patient_id = Patient.objects.get(Id = Id)
    if request.method == "POST" :
        edit_patient = PatientForm(request.POST,instance=patient_id)
        if edit_patient.is_valid():
            edit_patient.save()
            return redirect('/myadmin/patient')
    else:
        edit_patient = PatientForm(instance=patient_id)
    context = {
        'patient_form':edit_patient
    }            
    return render(request, 'pages/patient_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def patient_delete(request,Id):
    patient_delete = Patient.objects.get(Id = Id)
    if request.method == "POST" :
        patient_delete.delete()
        return redirect('/myadmin/patient')
    return render(request, 'pages/patient_delete.html')

#------------------------room-----------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def room(request):
    if request.method == "POST" :
       add_room = RoomForm(request.POST)
       if add_room.is_valid():
            add_room.save()
    
    context = {
        'room' : Room.objects.all(),
        'room_form' : RoomForm(),
    }
    return render(request,'pages/room.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def room_update(request,Id):
    room_id = Room.objects.get(Id = Id)
    if request.method == "POST" :
        edit_room = RoomForm(request.POST,instance=room_id)
        if edit_room.is_valid():
            edit_room.save()
            return redirect('/myadmin/room')
    else:
        edit_room = RoomForm(instance=room_id)
    context = {
        'room_form':edit_room
    }            
    return render(request, 'pages/room_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def room_delete(request,Id):
    room_delete = Room.objects.get(Id = Id)
    if request.method == "POST" :
        room_delete.delete()
        return redirect('/myadmin/room')
    return render(request, 'pages/room_delete.html')


#--------------------------invoice--------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def invoice(request):
    if request.method == "POST" :
       add_invoice = Invoiceform(request.POST)
       if add_invoice.is_valid():
            add_invoice.save()
    
    context = {
        'invoice' : Invoice.objects.all(),
        'invoice_form' : Invoiceform(),
    }
    return render(request,'pages/invoice.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def invoice_update(request,Id):
    invoice_id = Invoice.objects.get(Id = Id)
    if request.method == "POST" :
        edit_invoice = Invoiceform(request.POST,instance=invoice_id)
        if edit_invoice.is_valid():
            edit_invoice.save()
            return redirect('/myadmin/invoice')
    else:
        edit_invoice = Invoiceform(instance=invoice_id)
    context = {
        'invoice_form':edit_invoice
    }            
    return render(request, 'pages/invoice_update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def invoice_delete(request,Id):
    invoice_delete = Invoice.objects.get(Id = Id)
    if request.method == "POST" :
        invoice_delete.delete()
        return redirect('/myadmin/invoice')
    return render(request, 'pages/invoice_delete.html')




#----------------------------searchbar------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def searchbar(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Medicine.objects.filter(Name__contains = searched)
        return render(request, 'pages/searchbar.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/searchbar.html') 


#----------------------------depsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def depsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Department.objects.filter(name__contains = searched)
        return render(request, 'pages/depsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:    
        return render(request, 'pages/depsearch.html') 
    
#----------------------------docsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def docsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Doctor.objects.filter(Name__contains = searched)
        return render(request, 'pages/docsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/docsearch.html') 

#----------------------------patsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def patsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Patient.objects.filter(Name__contains = searched)
        return render(request, 'pages/patsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/patsearch.html')      


#----------------------------empsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def empsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Employee.objects.filter(Name__contains = searched)
        return render(request, 'pages/empsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/empsearch.html')      


#----------------------------blosearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def blosearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Blood.objects.filter(Blood_Group__contains = searched)
        return render(request, 'pages/blosearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/blosearch.html')      

#----------------------------roomsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def roomsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Room.objects.filter(Id__contains = searched)
        return render(request, 'pages/roomsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/roomsearch.html')   

#----------------------------machsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def machsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Machiens.objects.filter(Name__contains = searched)
        return render(request, 'pages/machsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/machsearch.html') 


#----------------------------labsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def labsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Lab.objects.filter(Test_type__contains = searched)
        return render(request, 'pages/labsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/labsearch.html') 

#----------------------------birthsearch------------------#
@login_required(login_url='logindashboard')

def birthsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Birth.objects.filter(Father_Name__contains = searched)
        return render(request, 'pages/birthsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/birthsearch.html') 
     
#----------------------------deathsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def deathsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Death.objects.filter(Id__contains = searched)
        return render(request, 'pages/deathsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/deathsearch.html')      

#----------------------------flosearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def flosearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Floor.objects.filter(Id__contains = searched)
        return render(request, 'pages/flosearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/flosearch.html') 
     
#----------------------------invsearch------------------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 

def invsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        venues = Invoice.objects.filter(Id__contains = searched)
        return render(request, 'pages/invsearch.html' , {'searched' :searched , 'venues':venues})
     
    else:
         return render(request, 'pages/invsearch.html')      
     
     
 #----------------------------logindashboard------------------#    
def logindashboard(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            myadmin = authenticate(request ,username= username,password=password)
            if myadmin is not None:
                login(request , myadmin)
            
    return render(request,'pages\logindashboard.html')    



def logoutdashboard(request):
    logout(request)
    return render(request,'pages\index.html') 
    
       
     
     
     
     