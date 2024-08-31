from django.db import models
from Employees.models import Employees


class Project(models.Model):
  Project_name = models.CharField(max_length=100)
  Project_image = models.ImageField(upload_to="Profile",blank=True)
  Description = models.CharField(max_length=500)
  Manager = models.ForeignKey(Employees,on_delete=models.CASCADE)
  Start_date = models.DateField()
  Deadline = models.DateField()
  Technology = models.CharField(max_length=50,default='SOME STRING')
  
  
  class Meta:
      ordering =['Project_name']
  
  def __str__(self):
      return self.Project_name
