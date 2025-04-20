from django.db import models
from django.utils import timezone
from Project_management.models import Project_manager


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
]

class Tasks(models.Model):
  task_name =models.CharField(max_length=100)
  Assigned_to = models.ForeignKey(Project_manager, on_delete=models.CASCADE,null=True)
  Start_date = models.DateField(auto_now_add=True)
  Deadline =models.DateField(default=timezone.now)
  Comments=models.CharField(max_length=100,blank=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

  class Meta:
      ordering =['task_name ']
  
  def __str__(self):
       return self.task_name 

