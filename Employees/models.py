from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import UserManager


class Employees(AbstractBaseUser,PermissionsMixin):
  Employee_name=models.CharField(max_length=100)
  phone_number=models.CharField(max_length=100,unique=True)
  Profile_image =models.ImageField(upload_to="Profile",blank=True)
  email = models.EmailField(blank=True)
  Joining_date = models.DateField(default=datetime.now,blank=True)
  Skills =models.CharField(max_length=100,default='abc')
  Designation=models.CharField(max_length=100)
  is_active=models.BooleanField(default=True)
  is_superuser=models.BooleanField(default=False)
  is_staff=models.BooleanField(default=False)
  

  USERNAME_FIELD='phone_number'
  REQUIRED_FIELDS=[]
  objects=UserManager()

#   class Meta:
#       ordering =['Employee_name']
  
#   def __str__(self):
#        return self.Employee_name
  






