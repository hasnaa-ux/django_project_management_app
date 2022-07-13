from distutils.command.upload import upload
from django.db import models
from datetime import datetime

from django.forms import EmailField
# Create your models here.


class LogIn(models.Model):
    account_username =models.CharField(max_length=50,verbose_name='UserName')
    account_password =models.CharField(max_length=50,verbose_name='Password')
    def __str__(self):
        return self.account_username
    
    class Meta:
        ordering = ['account_username']


class SignUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Appointment(models.Model):
    Departments=[
        ('Cardiology','Cardiology'),
        ('Neurology','Neurology'),
        ('Hepatology','Hepatology'),
        ('Pediatrics','Pediatrics'),
        ('Eya Care','Eya Care')
    ]

    YourName = models.CharField(max_length=50,null=True,blank=True,verbose_name='Name')
    YourEmail = models.CharField(max_length=100,null=True,blank=True,verbose_name='Email')
    YourPhone = models.IntegerField(null=True,blank=True,verbose_name='Phone')
    YourDate = models.DateTimeField(default=datetime.now(),null=True,blank=True,verbose_name='Date')
    YourMessage = models.TextField(null=True,blank=True,verbose_name='Message')
    Department = models.CharField(max_length=50,choices=Departments,null=True,blank=True)
    YourDoctor = models.CharField(max_length=50,null=True,blank=True,verbose_name='Doctor')
    def __str__(self):
        return self.YourName
      
    class Meta:
        ordering = ['YourName']

class Info(models.Model):
    place = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=254,null=True)

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email


""" class Doctor(models.Model):
    Photo_Doctor = models.ImageField(upload_to=('photo'),null=True)
    Name_Doctor = models.CharField(max_length=50,null=True)
    Bio_Doctor = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.Name_Doctor
    
    class Meta:
        ordering = ['Name_Doctor'] """