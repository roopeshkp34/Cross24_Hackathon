from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.




class Peoples(models.Model):
    peoples = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    id=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=255)
    address=models.TextField()
    mobile_number=models.CharField(max_length=255)
    aadhaar_number=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    legislative_assembly=models.CharField(max_length=255)
    panchayath=models.CharField(max_length=255)
    pincord=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()





class Department(models.Model):
    peoples = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    id=models.AutoField(primary_key=True)
    place=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Complaints(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=255)
    status=models.IntegerField(default="0")
    complete=models.IntegerField(default="0")

    people_id=models.ForeignKey(Peoples,on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

