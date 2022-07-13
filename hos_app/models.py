
from asyncio.windows_events import NULL
from datetime import date
from re import U
from tkinter import CASCADE
from xml.etree.ElementTree import Comment
from django import db
from django.db import models
from django.forms import ImageField

# Create your models here.



class Department(models.Model):
    Id = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField( null=True,blank=True)
       
    def __str__(self):
      return self.name

class Doctor(models.Model): 
    
    gen = [
        ('male' , 'male'),
        ('female' , 'female'),
    ]
    
    Id = models.IntegerField(null=False,primary_key=True)
    Name = models.CharField(max_length=255, null=True,blank=True)
    Email = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255, choices=gen)
    Salary = models.DecimalField(max_digits=7,decimal_places=2 ,null=True,blank=True)
    Address = models.CharField(max_length=255, null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Status_from_Date = models.DateField(null=True,blank=True) 
    Status_to_Date = models.DateField(null=True,blank=True) 
    Image = models.ImageField(upload_to=('photo'),null=True)
    Bio = models.CharField(max_length=255, null=True,blank=True)
    Department= models.ForeignKey(Department,unique=False ,on_delete=models.CASCADE)
    
    
    
class Patient(models.Model):
    
    gender = [
        ('male' , 'male'),
        ('female' , 'female'),
    ]
    
    Id = models.IntegerField(null=False)
    Name = models.CharField(max_length=255, null=True,blank=True)
    Email = models.EmailField( null=True,blank=True)
    Gender = models.CharField(max_length=255, null=True,blank=True,choices=gender)
    Age = models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=255, null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Blood = models.CharField(max_length=255, null=True,blank=True)
    Bio = models.CharField(max_length=255, null=True,blank=True)
    def __str__(self):
        return self.Name

class Birth(models.Model):  
     Id = models.IntegerField(null=False)
     Father_Name = models.CharField(max_length=255, null=True,blank=True)  
     Mother_Name = models.CharField(max_length=255, null=True,blank=True)
     Gender = models.CharField(max_length=255, null=True,blank=True)
     Blood_Group = models.CharField(max_length=255, null=True,blank=True)
     Birth_time =models.TimeField(null=True,blank=True)
     Birth_Date= models.DateField( null=True,blank=True) 
     #patient_id = models.ForeignKey(Patient, unique=True,on_delete=models.PROTECT)
    
     def __str__(self):
         return self.Father_Name
       
class Blood(models.Model): 
    Id = models.IntegerField(null=False)
    No_packets_used = models.IntegerField(null=True,blank=True)
    No_packets_present  =models.IntegerField(null=True,blank=True)
    Blood_Group = models.CharField(max_length=255)
    
class Death(models.Model):
    
     patient_gender = [
         ('male' , 'male' ),
         ('female' , 'female' ),
     ]
    
     Id = models.IntegerField(null=True)
     Gender = models.CharField(max_length=255, null=True,blank=True,choices=patient_gender)
     Birth_Date = models.DateField( null=True,blank=True) 
     Death_time =models.TimeField(null=True,blank=True)
     Death_Date= models.DateField( null=True,blank=True) 
    
class Employee(models.Model): 
    
    employee_gender = [
         ('male' , 'male' ),
         ('female' , 'female' ),
     ]
    
    Id = models.IntegerField(null=False)
    Name = models.CharField(max_length=255, null=True,blank=True)
    Email = models.EmailField( null=True,blank=True)
    Gender = models.CharField(max_length=255, null=True,blank=True,choices=employee_gender)
    Salary = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    Address = models.CharField(max_length=255, null=True,blank=True)
    Job = models.CharField(max_length=255, null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Status_from_Date = models.DateField(null=True,blank=True) 
    Status_to_Date = models.DateField(null=True,blank=True) 
           
class Machiens(models.Model):
    Id = models.IntegerField(null=False)
    Name = models.CharField(max_length=255, null=True,blank=True)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE )
    
    def __str__(self):
        return self.Name
    
    
class Medicine(models.Model):
    
    status = [
         ('Avaliable' , 'Avaliable' ),
         ('Not_Avilable' , 'Not_Avilable' ),
     ]
    
    Code = models.IntegerField(null=True)
    Name = models.CharField(max_length=255, null=True,blank=True)
    Avilable_or_not = models.CharField(max_length=255, null=True,blank=True,choices=status)
    Cost_per_unit = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    
class Floor(models.Model):
    Id = models.IntegerField(null=False)
    Num_of_Rooms = models.IntegerField(null=False,blank=False)
    
class Room(models.Model):
     
     Id = models.IntegerField(null=False)   
     Num_of_Bed = models.IntegerField(null=True,blank=True)
     floor_id = models.ForeignKey(Floor ,on_delete=models.CASCADE)
  
     
class Invoice(models.Model):
    
    s =[
        ('paid','paid'),
        ('unpaid','unpaid'),
    ]
    
    
    Id = models.IntegerField(null=False)   
    Operation_Cost =  models.IntegerField(null=False,blank=False,default=NULL)
    Bed_Cost = models.IntegerField(null=False,blank=False,default=NULL)
    Service_Cost =  models.IntegerField(null=False,blank=False,default=NULL)
    Medical_Cost =  models.IntegerField(null=False,blank=False,default=NULL)
    Lab_Cost =  models.IntegerField(null=False,blank=False,default=NULL)
    Blood_Cost =  models.IntegerField(null=False,blank=False,default=NULL)
    Total =  models.IntegerField(null=False,blank=False,default=NULL)
    Status = models.CharField(max_length=255, null=True,blank=True,choices=s)   
    Patient_id = models.OneToOneField(Patient,on_delete=models.CASCADE) 
    
    def __str__(self):
      return self.name
 
    
class Lab(models.Model):  
     Id = models.IntegerField(null=False, primary_key=True) 
     Test_type = models.CharField(max_length=255, null=True,blank=True)
     Cost = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
     Bio = models.CharField(max_length=255, null=True,blank=True)    
   
   
   
    
# class Bed(models.Model):    
#     Id =  models.IntegerField(null=False, primary_key=True)        
#     Alloted_time = models.TimeField(null=True,blank=True, editable=True)
#     Discharge_Time = models.TimeField( null=True,blank=True, editable=True)    
                        
                    
    
      
