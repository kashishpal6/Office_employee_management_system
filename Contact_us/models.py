from django.db import models

class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email = models.EmailField(unique=True,blank=False)
    Subject=models.CharField(max_length=100)
    Message= models.TextField()

    class Meta:
      ordering =['Name']
  
    def __str__(self):
      return self.Name
