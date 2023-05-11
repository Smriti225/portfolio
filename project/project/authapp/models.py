from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class verification_code(models.Model):
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.IntegerField()
    created_on=models.DateTimeField(default=datetime.now())
    expiry_on=models.DateTimeField(default=datetime.now() + timedelta(minutes=3))
    