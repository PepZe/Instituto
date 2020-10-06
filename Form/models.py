from django.db import models
from datetime import datetime

class Register(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    church = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    check_in = models.BooleanField(default=False)
    phone = models.CharField(max_length= 14)
 
