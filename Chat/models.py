from typing import Iterable
from django.db import models

from Employees.models import Employees
 
class ChatRoom(models.Model):
    User_1 = models.ForeignKey(Employees,on_delete=models.CASCADE,related_name="User_1")
    User_2 = models.ForeignKey(Employees,on_delete=models.CASCADE,related_name="User_2")
       
    class Meta:
       constraints=[models.UniqueConstraint(fields=['User_1','User_2'],name="unique_user_pair")]

    def save(self,*args,**kwargs):

        if self.User_1.Employee_id>self.User_2.Employee_id:
          self.User_1,self.User_2=self.User_2,self.User_1
        super().save(*args,**kwargs)

    
    def __str__(self):
        return self.User_1.Employee_name +'-'+ self.User_2.Employee_name



class Message(models.Model):
  ChatRoom=models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="ChatRoom")
  Sender = models.ForeignKey(Employees,on_delete=models.CASCADE,related_name="Sender")
  Receiver = models.ForeignKey(Employees,on_delete=models.CASCADE,related_name="Receiver")
  Message= models.TextField()
  time_stamp=models.DateTimeField(auto_now_add=True)


# class Message_status(models.Model):
#    Message = models.ForeignKey(Message,on_delete=models.CASCADE,related_name="inbox")
#    is_read = models.BooleanField(default=False)
#    is_sent = models.BooleanField(default=True)
#    is_read_timestamp = models.DateTimeField(auto_now=True)
#    is_sent_timestamp = models.DateTimeField(auto_now=True)    
  