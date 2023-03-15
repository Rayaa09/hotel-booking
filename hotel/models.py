from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    password=models.CharField(max_length=80)

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    phone=models.EmailField(max_length=80)
    message=models.CharField(max_length=80)
