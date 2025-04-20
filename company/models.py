from django.db import models


class Company(models.Model):
  Company_name = models.CharField(max_length=100)
  Location = models.CharField(max_length=100)
  Founding_date = models.DateField()
  Email = models.EmailField()
  Description= models.TextField()
  Founder = models.CharField(max_length=100)

  class Meta:
    ordering =['Company_name']
  
  def __str__(self):
    return self.Company_name
