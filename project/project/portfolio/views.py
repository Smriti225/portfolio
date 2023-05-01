from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Contact,Blogs
from django.contrib import messages
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mob=request.POST.get('mob')
        des=request.POST.get('des')
        print(name,request.user,mob,des)
        created=Contact(name=name,email=request.user,mobile_no=mob,description=des)
        created.save()
        messages.info(request,"your request for contact has been made")
        return redirect('contact')
    return render(request,'contact.html',{"user":request.user})