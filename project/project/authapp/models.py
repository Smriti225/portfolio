from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class verification_code(models.Model):
    email=models.EmailField()
    code=models.IntegerField()
    created_on=models.DateTimeField(default=datetime.now())
    expiry_on=models.DateTimeField(default=datetime.now() + timedelta(minutes=3))
    