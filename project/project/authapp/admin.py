from django.contrib import admin
from .models import verification_code
# Register your models here.
@admin.register(verification_code)
class Adminverificationcode(admin.ModelAdmin):
    list_display=['email','code','created_on','expiry_on']   