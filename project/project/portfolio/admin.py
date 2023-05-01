from django.contrib import admin
from .models import Contact,Blogs
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile_no','description']
    
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title','authname']