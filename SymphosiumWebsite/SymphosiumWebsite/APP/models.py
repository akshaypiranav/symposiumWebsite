from django.db import models
import datetime
# Create your models here.
class Register(models.Model):
    uniqueNumber=models.CharField(max_length=20,null=True,blank=True)
    collegeName=models.CharField(max_length=20,null=True,blank=True)
    collegeEmail=models.EmailField(null=True,blank=True)
    contactNumber=models.CharField(max_length=20,null=True,blank=True)
    counsellingCode=models.CharField(max_length=10,null=True,blank=True)
    whatsappContact=models.CharField(max_length=20,null=True,blank=True)
    mapLink=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=200,null=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    collegeImage=models.ImageField(upload_to="collegeImages",default="defaultImages/college.jpeg")
    accountCreated=models.DateField(default=datetime.datetime.now)


class Details(models.Model):
    symName=models.CharField(max_length=20,null=True,blank=True)
    guest=models.TextField(max_length=200)
    Caption=models.CharField(max_length=50,null=True,blank=True)
    collegeName=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=50,null=True,blank=True)
    uniqueNumber=models.CharField(max_length=20,null=True,blank=True)
    RegistrationFee=models.IntegerField()
    startdate=models.CharField(max_length=20,null=True,blank=True)
    enddate=models.CharField(max_length=20,null=True,blank=True)
    lastDate=models.CharField(max_length=20,null=True,blank=True)
    eventType=models.CharField(max_length=20,null=True,blank=True)
    Category=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    locationLink=models.CharField(max_length=100,null=True,blank=True)
    eventLink=models.CharField(max_length=100,null=True,blank=True)
    chatLink=models.CharField(max_length=100,null=True,blank=True)
    about=models.TextField(max_length=200)
    contact=models.CharField(max_length=20,null=True,blank=True)
    Brouchure=models.ImageField(upload_to="brochureImages",default="defaultImages/college.jpeg")
    postedDate=models.DateField(default=datetime.datetime.now)
    
class StudentMail(models.Model):
    studentMail=models.EmailField(null=True,blank=True)
    yesOrNo=models.BooleanField(default=True)
  
    
    
    
    
    
    
    
    

   
    

# class details(models.Model):
#     pass
