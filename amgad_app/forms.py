from django import forms
from .models import *





class AppointmentForm(forms.ModelForm):
    class Meta :
        model = Appointment
        fields = ['YourName','YourPhone','YourDate','Department']
        widgets = {
                        
            
            'YourName':forms.TextInput(attrs={'class':'form-control'}),
            
            'YourPhone': forms.NumberInput(attrs={'class':'form-control'}),
            'YourDate': forms.DateInput(attrs={'class':'form-control'}),
            
            'Department':forms.Select(attrs={'class':'form-control'}),
            
            
            
            
            
        }     