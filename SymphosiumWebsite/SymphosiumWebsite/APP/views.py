from django.shortcuts import render,redirect
from SymphosiumWebsite import settings
from .models import Register,Details,StudentMail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages
import smtplib
from django.http import JsonResponse
import random


otp=12345


def index(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        message=request.POST["message"]
        print(firstname,lastname,email,mobile,message)
        sender_email = "akshaypiranavb@gmail.com"
        receiver_email = "akshaypiranavb@gmail.com"
        subject = "Message from user - Sympho Website"
        body = "Customer Name : "+str(firstname)+" "+str(lastname)+'\n'+'Email : '+str(email)+'\n'+"Contact Number : "+str(mobile)+"\n"+"Customer Message : \n"+str(message)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com" 
        smtp_port = 587  
        smtp_username = "akshaypiranavb@gmail.com"  
        smtp_password = "ddld flec vggd ovve"

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                messages.success(request, 'Email Sent Successfully')

        except Exception as e:
            print(f"Error sending email: {e}")
            messages.success(request,'Check Your Network Connection')
    return render(request,"main/index.htm",{"title":"Home"})

def events(request):
    if(Details.objects.filter(Category="Events").exists()):
        data=Details.objects.filter(Category="Events")
        return render(request,"main/events.htm",{"title":"Events","data":data})
    else:
        return render(request,"main/events.htm",{"title":"Events"})


def conference(request):
    if(Details.objects.filter(Category="Conference").exists()):
        print("INSIDE")
        data=Details.objects.filter(Category="Conference")
        return render(request,"main/conference.htm",{"title":"Conference","data":data})
    else:
        return render(request,"main/conference.htm",{"title":"Conference"})

def hackathon(request):
    if(Details.objects.filter(Category="Hackathon").exists()):
        print("INSIDE")
        data=Details.objects.filter(Category="Hackathon")
        return render(request,"main/hackathon.htm",{"title":"Hackathon","data":data})
    else:
        return render(request,"main/hackathon.htm",{"title":"Hackathon"})


def symphosium(request):
    if(Details.objects.filter(Category="Symposium").exists()):
        print("INSIDE")
        data=Details.objects.filter(Category="Symposium")
        return render(request,"main/symphosium.htm",{"title":"Symphosium","data":data})
    else:
        return render(request,"main/symphosium.htm",{"title":"Symphosium"})
    
def add(request):
    value= request.session.get("uniqueNumber","Guest")
    print(value)
    if value=="Guest":
        return redirect("login")
    else:
        if request.method=="POST":
            uniqueNumber=request.POST["uniqueNumber"]
            symName=request.POST["symName"]
            guest=request.POST["guest"]
            Caption=request.POST["Caption"]
            collegeName=request.POST["collegeName"]
            Department=request.POST["Department"]
            RegistrationFee=request.POST["RegistrationFee"]
            startdate=request.POST["startdate"]
            enddate=request.POST["enddate"]
            lastDate=request.POST["lastDate"]
            eventType=request.POST["eventType"]
            Category=request.POST["Category"]
            location=request.POST["location"]
            locationLink=request.POST["locationLink"]
            eventLink=request.POST["eventLink"]
            chatLink=request.POST["chatLink"]
            about=request.POST["about"]
            contact=request.POST["contact"]
            if "Brouchure" in request.FILES :
                Brouchure=request.FILES["Brouchure"]
                if bool(Brouchure):
                    form=Details.objects.create(uniqueNumber=uniqueNumber,symName=symName,guest=guest,Caption=Caption,collegeName=collegeName,Department=Department,RegistrationFee=RegistrationFee,startdate=startdate,enddate=enddate,lastDate=lastDate,eventType=eventType,Category=Category,location=location,locationLink=locationLink,eventLink=eventLink,chatLink=chatLink,about=about,contact=contact,Brouchure=Brouchure)
                else:
                    form=Details.objects.create(uniqueNumber=uniqueNumber,symName=symName,guest=guest,Caption=Caption,collegeName=collegeName,Department=Department,RegistrationFee=RegistrationFee,startdate=startdate,enddate=enddate,lastDate=lastDate,eventType=eventType,Category=Category,location=location,locationLink=locationLink,eventLink=eventLink,chatLink=chatLink,about=about,contact=contact)
                    form.save()
            print(symName,guest,Caption,collegeName,Department,RegistrationFee,startdate,enddate,lastDate,eventType,Category,location,locationLink,eventLink,chatLink,about,contact)
        
    return render(request,"main/add.htm",{"title":"Add Sympho"})

def login(request):
    value= request.session.get("uniqueNumber","Guest")
    print(value)
    if value!="Guest":
        return redirect("index")
    if request.method=="POST":
        uniqueNumber=request.POST['uniqueNumber']
        password=request.POST['password']
        print(uniqueNumber,password)
        if(Register.objects.filter(uniqueNumber=uniqueNumber).exists()):
            user=Register.objects.get(uniqueNumber=uniqueNumber)
            uniqueNumber=user.uniqueNumber
            id=user.pk
            userPassword=user.password
            print(userPassword)
            if(password==userPassword):
                print("GOING TO REDIRECT")
                request.session['uniqueNumber'] = uniqueNumber
                request.session["id"]=id
                return redirect("add")
            else:
                print("Wrong password")
        else:
            print("No user with yhis number")
            
            
    return render(request,"main/login.htm",{"title":"College Login Portal"})

def register(request):
    value= request.session.get("uniqueNumber","Guest")
    print(value)
    if value!="Guest":
        return redirect("index")
    if request.method=="POST":
        uniqueNumber=request.POST["uniqueNumber"]
        collegeName=request.POST['collegeName']
        collegeEmail=request.POST["collegeEmail"]
        contactNumber=request.POST["contactNumber"]
        counsellingCode=request.POST["counsellingCode"]
        whatsappContact=request.POST["whatsapp"]
        mapLink=request.POST["map"]
        address=request.POST["address"]
        password=request.POST["password"]
        confirm=request.POST["confirm"]
        if 'image' in request.FILES:
            collegeImage=request.FILES["image"]
        
            if(password==confirm):
                print("password ok")
                if bool(collegeImage):
                    form=Register.objects.create(uniqueNumber=uniqueNumber,collegeName=collegeName,collegeEmail=collegeEmail,contactNumber=contactNumber,counsellingCode=counsellingCode,whatsappContact=whatsappContact,mapLink=mapLink,address=address,password=password,collegeImage=collegeImage)
                    print("Sved")
                    form.save()
                else:
                    print("no image")
        else:
            if(password==confirm):
                print("password ok")
                form=Register.objects.create(uniqueNumber=uniqueNumber,collegeName=collegeName,collegeEmail=collegeEmail,contactNumber=contactNumber,counsellingCode=counsellingCode,whatsappContact=whatsappContact,mapLink=mapLink,address=address,password=password)
                print("Saved")
                form.save()
            else:
                print("password not ok")

            

    return render(request,"main/register.htm",{"title":"College Registration Portal"})

def details(request,id):
    if(Details.objects.filter(id=id).exists()):
        data=Details.objects.get(id=id)
        return render(request,"main/details.htm",{"title":"Programme Details","data":data})
    else:
        return redirect("/")

def profile(request,id):
    value= request.session.get("uniqueNumber","Guest")
    print(value)
    if value=="Guest":
        print("No value")
        return redirect("index")
    print("INSIDE")
    if(Register.objects.filter(id=id).exists()):
        print("INSIDE")
        data=Register.objects.get(id=id)
        uNum=data.uniqueNumber
        uploads=Details.objects.filter(uniqueNumber=uNum)
        print(uploads)
        if  request.method=="POST":
            print("inside")
            uniqueNumber=request.POST["uniqueNumber"]
            collegeName=request.POST['collegeName']
            collegeEmail=request.POST["collegeMail"]
            contactNumber=request.POST["contactNumber"]
            counsellingCode=request.POST["code"]
            whatsappContact=request.POST["wcontactNumber"]
            mapLink=request.POST["map"]
            address=request.POST["address"]
            password=request.POST["password"]
            print('image' in request.FILES)
            if 'image' in request.FILES :
                collegeImage=request.FILES["image"]
                data.uniqueNumber=uniqueNumber
                data.collegeName=collegeName
                data.collegeEmail=collegeEmail
                data.contactNumber=contactNumber
                data.counsellingCode=counsellingCode
                data.whatsappContact=whatsappContact
                data.mapLink=mapLink
                data.address=address
                data.password=password
                data.collegeImage=collegeImage
                data.save()
                print("saved")
            else:
                data.uniqueNumber=uniqueNumber
                data.collegeName=collegeName
                data.collegeEmail=collegeEmail
                data.contactNumber=contactNumber
                data.counsellingCode=counsellingCode
                data.whatsappContact=whatsappContact
                data.mapLink=mapLink
                data.address=address
                data.password=password
                data.save()
                print("saved")

                
            return render(request,"main/profile.htm",{"title":"Profile","data":data,"uploads":uploads})
            
        return render(request,"main/profile.htm",{"title":"Profile","data":data,"uploads":uploads})
    else:
        return redirect("/")
    


def clearSession(request):
    request.session.clear()
    print("Clear Panniten Boss")
    return redirect("/")

def update(request,id):
    value= request.session.get("uniqueNumber","Guest")
    print(value)
    if value=="Guest":
        return redirect("index")
    if(Details.objects.filter(id=id).exists()):
        data=Details.objects.get(id=id)
        if request.method=="POST":
            uniqueNumber=request.POST["uniqueNumber"]
            symName=request.POST["symName"]
            guest=request.POST["guest"]
            Caption=request.POST["Caption"]
            collegeName=request.POST["collegeName"]
            Department=request.POST["Department"]
            RegistrationFee=request.POST["RegistrationFee"]
            startdate=request.POST["startdate"]
            enddate=request.POST["enddate"]
            lastDate=request.POST["lastDate"]
            eventType=request.POST["eventType"]
            Category=request.POST["Category"]
            location=request.POST["location"]
            locationLink=request.POST["locationLink"]
            eventLink=request.POST["eventLink"]
            chatLink=request.POST["chatLink"]
            about=request.POST["about"]
            contact=request.POST["contact"]
            if "Brouchure" in request.FILES :
                Brouchure=request.FILES["Brouchure"]
                if bool(Brouchure):
                    data.uniqueNumber=uniqueNumber
                    data.symName=symName
                    data.guest=guest
                    data.Caption=Caption
                    data.Department=Department
                    data.collegeName=collegeName
                    data.RegistrationFee=RegistrationFee
                    data.startdate=startdate
                    data.enddate=enddate
                    data.eventType=eventType
                    data.lastDate=lastDate
                    data.Category=Category
                    data.location=location
                    data.locationLink=locationLink
                    data.eventLink=eventLink
                    data.chatLink=chatLink
                    data.about=about
                    data.contact=contact
                    data.Brouchure=Brouchure
                    data.save()
                    print("SAVED WITH IMAGE")
                else:
                    data.uniqueNumber=uniqueNumber
                    data.symName=symName
                    data.guest=guest
                    data.Caption=Caption
                    data.Department=Department
                    data.collegeName=collegeName
                    data.RegistrationFee=RegistrationFee
                    data.startdate=startdate
                    data.enddate=enddate
                    data.eventType=eventType
                    data.lastDate=lastDate
                    data.Category=Category
                    data.location=location
                    data.locationLink=locationLink
                    data.eventLink=eventLink
                    data.chatLink=chatLink
                    data.about=about
                    data.contact=contact
                    data.save()
                    print("SAVED WITHOUT IMAGE")
            else:
                data.uniqueNumber=uniqueNumber
                data.symName=symName
                data.guest=guest
                data.Caption=Caption
                data.Department=Department
                data.collegeName=collegeName
                data.RegistrationFee=RegistrationFee
                data.startdate=startdate
                data.enddate=enddate
                data.eventType=eventType
                data.lastDate=lastDate
                data.Category=Category
                data.location=location
                data.locationLink=locationLink
                data.eventLink=eventLink
                data.chatLink=chatLink
                data.about=about
                data.contact=contact
                data.save()
                print("SAVED WITHOUT IMAGE")
                     
        return render(request,"main/updateprogramme.htm",{"title":"Update","data":data})
    else:
        return redirect("/")
    
def delete(request,id):
    if(Details.objects.filter(id=id)):
        data=Details.objects.get(id=id)
        data.delete()
    return redirect("/")

def notify(request):
    if request.method=="POST":
        global email
        email=request.POST["email"]
        global otp
        otp=random.randrange(100000,999999)
        print(otp)
        message = MIMEMultipart()
        message["From"] = "akshaypiranavb@gmail.com"
        message["To"] = email
        message["Subject"] = "OTP FOR EMAIL VERIFICATION"
        body=f"Dear student kindly enter the below attached otp to verify your Email so that you can receive email when a College/School post a programme\nYour OTP:{otp}"

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com" 
        smtp_port = 587  
        smtp_username = "akshaypiranavb@gmail.com"  
        smtp_password = "ddld flec vggd ovve"

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(smtp_username, smtp_password)
                server.sendmail("akshaypiranavb@gmail.com", email, message.as_string())
                messages.success(request, 'Email Sent Successfully')
                return redirect("verify")

        except Exception as e:
            print(f"Error sending email: {e}")
            messages.success(request,'Check Your Network Connection')

    return render(request,"main/notifyMe.htm",{"title":"Notify Me"})


def faq(request):
    return render(request,"main/faq.htm",{"title":"FAQ"})

def verify(request):
    if otp!=12345:
        if request.method=="POST":
            otpCheck=request.POST["otp"]

            if(otp==int(otpCheck)):
                print("in smail")
                if(not(StudentMail.objects.filter(studentMail=email).exists())):
                    sMail=StudentMail.objects.create(studentMail=email)
                    sMail.save()
                    return redirect("/")
                else:
                    print("mail already in use")
                    return redirect("deleteMyEmail")
        return render(request,"main/verify.htm",{"title":"Verify Me"})
    else:
        return redirect("/")
        
        
def deleteMyEmail(request):
    if request.method=="POST":
        mail=request.POST["mail"]
        if(StudentMail.objects.filter(studentMail=mail).exists()):
            particularMail=StudentMail.objects.get(studentMail=mail)
            particularMail.delete()
            return redirect("/")
    return render(request,"main/deletemyMail.htm",{"title":"DELETE MY EMAIL","mailData":email})