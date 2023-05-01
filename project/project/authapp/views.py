from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password

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
        print(fname,lname,email,passw)
        if passw!=cpass:
            messages.info(request,message="password and confirm password  doesn't match")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"username already taken")
                return render(request,'signup.html')  
        except Exception as e:
            pass
        myuser=User.objects.create_user(username=email,first_name=fname,last_name=lname,password=passw)
        myuser.save()
        messages.info(request,"registered successfully go for login")  
        return redirect('handlelogin')  
    return render(request,'signup.html')