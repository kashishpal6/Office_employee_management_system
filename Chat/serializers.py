from rest_framework import serializers
from .models import *




class chatSerializer(serializers.ModelSerializer):

   class Meta:
      model=ChatRoom
      fields=['id','User_1','User_2']


class messageSerializer(serializers.ModelSerializer):
   class Meta:
      model = Message
      field = ['ChatRoom','Sender','Receiver','Message']