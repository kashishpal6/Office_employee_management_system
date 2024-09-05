from django.db import models
from Projects.models import Project
from Employees.models import Employees

class Project_manager(models.Model):
    name = models.ForeignKey(Employees,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='employees')


    def __str__(self):
        return self.project.Project_name+"-"+self.name.Employee_name


