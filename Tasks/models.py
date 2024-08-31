from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from Projects.models import Project
from Employees.models import Employees
status = (
    ('1', 'Pending'),
    ('2', 'Working'),
    ('3', 'Done'),
    ('4', 'Overdue')
)


class Tasks(models.Model):
  Task_name=models.CharField(max_length=100)
  Project_name = models.ForeignKey(Project,on_delete=models.CASCADE)
  Assigned_to = models.ForeignKey(Employees, on_delete=models.CASCADE,default='string')
  Start_date = models.DateField(auto_now_add=True)
  Deadline =models.DateField(default=datetime.now)
  Comments=models.CharField(max_length=100,blank=True)
  Status= models.CharField(max_length=7, choices=status, default=1)

  class Meta:
      ordering =['Task_name']
  
  def __str__(self):
       return self.Task_name

