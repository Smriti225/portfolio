from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import random
from .models import verification_code
from django.core.mail import send_mail
from django.shortcuts import render




def generate_random_no():
    return random.randint(1000,9999)
def handlelogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        user=authenticate(request,username=email,password=passw)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return render(request,'login.html')
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"successfully logout")
    return redirect('handlelogin')

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        passw=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        print(fname,lname,email,passw,cpass)
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Username already taken")
                return render(request,'signup.html')  
        except Exception as e:
            pass
        def validate_email(request,email):
            try:
                validator = EmailValidator()
                validator(email)
            except ValidationError as e:
                return {"valid":False,"error":str(e)}
            else:
                return {"valid":True}
        val=validate_email(request,email)
        if passw!=cpass:
            messages.info(request,message="Password and confirm password  doesn't match")
            return render(request,'signup.html')
        
        if(val['valid']==True):
            code=generate_random_no()
            email=email
            send_mail(
                "Verification code for further process",
                f'your verfication code is: {code}',
                'reenakimtee@outlook.com',
                [f'{email}']
            )
            myuser=User.objects.create_user(username=email,first_name=fname,last_name=lname,password=passw)
            myuser.save()
            data=verification_code.objects.create(email=email,code=code)
            data.save()
            return render(request,"verify.html",{"email":email})
        else:
             messages.info(request,message=val['error'])
             return render(request,'signup.html')
    return render(request,'signup.html')

def verifycode(request):
    email=request.GET.get('email')
    if request.method=='POST':
        code=request.POST.get('code')
        data=verification_code.objects.get(email=email)
        if str(data.code)==str(code):
            print("hello")
            messages.info(request,"verification done go for login")
            return redirect('handlelogin')
        else:
            messages.info(request,"Invalid verification code")
            return render(request,'verify.html',{"email":email})
    return render(request,'verify.html')
        