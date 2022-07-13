from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

# class BedForm(forms.ModelForm):
#     class Meta:
#          model = Bed
#          fields = [
#              'Id',             
#              'Alloted_Time',
#              'Discharge_Time',
#          ]
#          widgets = {
#               'Id': forms.NumberInput(attrs={'class':'form-control'}),            
#               'Alloted_Time': forms.TimeInput(attrs={'class':'form-control'}),
#               'Discharge_Time': forms.TimeInput(attrs={'class':'form-control'}),
#         } 
        
class DeathForm(forms.ModelForm):
    class Meta:
        model = Death
        fields = [
            'Id',
            'Gender',
            'Birth_Date',
            'Death_time',
            'Death_Date',
        ]
        
        widgets = {
            'Id'         : forms.NumberInput(attrs={'class':'form-control'}),
            'Gender'     : forms.Select(attrs={'class':'form-control'}),
            'Birth_Date' : forms.DateInput(attrs={'class':'form-control'}),
            'Death_time' : forms.TimeInput(attrs={'class':'form-control'}),
            'Death_Date' : forms.DateInput(attrs={'class':'form-control'}),
        }     
        

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'Code',
            'Name',
            'Avilable_or_not',
            'Cost_per_unit',
            
        ]
        
        widgets = {
            'Code'                : forms.NumberInput(attrs={'class':'form-control'}),
            'Name'                :forms.TextInput(attrs={'class':'form-control'}),
            'Avilable_or_not'     : forms.Select(attrs={'class':'form-control'}),
            'Cost_per_unit'       : forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }         
   
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'Id',
            'name',
            'description',
            
            
        ]
        
        widgets = {
            'Id'           : forms.NumberInput(attrs={'class':'form-control'}),
            'name'         :forms.TextInput(attrs={'class':'form-control'}),
            'description'  :forms.TextInput(attrs={'class':'form-control'}),
            
            
            
        }                        


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'Id',
            'Name',
            'Email',
            'Gender',
            'Salary',
            'Address',
            'Phone',
            'Status_from_Date',
            'Status_to_Date',
            'Image',
            'Bio',
            'Department',
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Salary': forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Phone': forms.NumberInput(attrs={'class':'form-control'}),
            'Status_from_Date': forms.DateInput(attrs={'class':'form-control'}),
            'Status_to_Date': forms.DateInput(attrs={'class':'form-control'}),
            
            'Bio': forms.TextInput(attrs={'class':'form-control'}),
            'Department': forms.NumberInput(attrs={'class':'form-control'}),
            
            
            
        }                        
 
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'Id',
            'Name',
            'Email',
            'Gender',
            'Salary',
            'Address',
            'Job',
            'Phone',
            'Status_from_Date',
            'Status_to_Date',
            
            
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Salary': forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Job': forms.TextInput(attrs={'class':'form-control'}),
            'Phone': forms.NumberInput(attrs={'class':'form-control'}),
            'Status_from_Date': forms.DateInput(attrs={'class':'form-control'}),
            'Status_to_Date': forms.DateInput(attrs={'class':'form-control'}),
            
            
            
            
        }                        
 
class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = [
            'Id',
            'No_packets_used',
            'No_packets_present',
            'Blood_Group',
            
        ]
        
        widgets = {
            'Id'                : forms.NumberInput(attrs={'class':'form-control'}),
            'No_packets_used'                :forms.NumberInput(attrs={'class':'form-control'}),
            'No_packets_present'     : forms.NumberInput(attrs={'class':'form-control'}),
            'Blood_Group'       : forms.TextInput(attrs={'class':'form-control'}),
            
            
        }   
 
 
class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = [
            'Id',
            'Num_of_Rooms',
           
            
        ]
        
        widgets = {
            'Id'           :forms.NumberInput(attrs={'class':'form-control'}),
            'Num_of_Rooms' :forms.NumberInput(attrs={'class':'form-control'}),  
        }              
        
        
class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        fields = [
            'Id',
            'Father_Name',
            'Mother_Name',
            'Gender',
            'Blood_Group',
            'Birth_time',
            'Birth_Date',
            #'patient_id',
            
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Father_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mother_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Blood_Group': forms.TextInput(attrs={'class':'form-control'}),
            'Birth_time':forms.TimeInput(attrs={'class':'form-control'}),
            'Birth_Date': forms.DateInput(attrs={'class':'form-control'}),
            #'patient_id': forms.NumberInput(attrs={'class':'form-control'}), 
        }      
        
        
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'Id',
            'Num_of_Bed',
            'floor_id',          
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Num_of_Bed':forms.NumberInput(attrs={'class':'form-control'}),
            'floor_id':forms.NumberInput(attrs={'class':'form-control'}),
        }      
        
class MachiensForm(forms.ModelForm):
    class Meta:
        model = Machiens
        fields = [
            'Id',
            'Name',
            'department_id',          
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'department_id':forms.NumberInput(attrs={'class':'form-control'}),
        }      
        
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'Id',
            'Name',
            'Email',
            'Gender',
            'Age',
            'Address',
            'Phone',
            'Blood',
            'Bio',
            
            
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Age': forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Phone': forms.NumberInput(attrs={'class':'form-control'}),
            'Blood': forms.TextInput(attrs={'class':'form-control'}),
            'Bio': forms.TextInput(attrs={'class':'form-control'}),
            
            
            
            
        }                        
         
 
class Invoiceform(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'Id',
            'Operation_Cost',
            'Bed_Cost',
            'Service_Cost',
            'Medical_Cost',
            'Lab_Cost',
            'Blood_Cost',
            'Total',
            'Status',
            'Patient_id',          
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Operation_Cost':forms.NumberInput(attrs={'class':'form-control'}),
            'Bed_Cost':forms.NumberInput(attrs={'class':'form-control'}),
            'Service_Cost': forms.NumberInput(attrs={'class':'form-control'}),
            'Medical_Cost':forms.NumberInput(attrs={'class':'form-control'}),
            'Lab_Cost': forms.NumberInput(attrs={'class':'form-control'}),
            'Blood_Cost': forms.NumberInput(attrs={'class':'form-control'}),
            'Total': forms.NumberInput(attrs={'class':'form-control'}),
            'Status': forms.Select(attrs={'class':'form-control'}),
            'Patient_id': forms.TextInput(attrs={'class':'form-control'}),
            
        }                        
         
class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = [
            'Id',
            'Test_type',
            'Cost', 
            'Bio',          
            
            
        ]
        
        widgets = {
                        
            'Id' : forms.NumberInput(attrs={'class':'form-control'}),
            'Test_type':forms.TextInput(attrs={'class':'form-control'}),
            'Cost':forms.NumberInput(attrs={'class':'form-control'}),
            'Bio':forms.TextInput(attrs={'class':'form-control'}),
        }        
         
         
        
        