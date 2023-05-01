from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    mobile_no=models.CharField(max_length=10)
    description=models.TextField()
    
class Blogs(models.Model):
   title=models.CharField(max_length=60)
   description= models.TextField()
   authname=models.CharField(max_length=20)
   image=models.ImageField(upload_to='blog',blank=True,null=True)
   timestamp=models.DateTimeField(auto_now_add=True,blank=True)