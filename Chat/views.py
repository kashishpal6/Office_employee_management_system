

from django.shortcuts import render
from Chat import serializers
from Chat.serializers import chatSerializer,messageSerializer
from Employees.views import Employee
from rest_framework import generics,response
from .models import *
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from django.db.models import Q
# Create your views here.

class chatRoom_list(generics.ListAPIView):
   queryset=ChatRoom.objects.all()
   serializer_class= chatSerializer
   permission_classes = [IsAdminUser]


class GetAllChat(generics.ListAPIView):
   serializer_class=chatSerializer
   permission_classes=[IsAuthenticated]
   def get_queryset(self):
      user=self.request.user
      GetAllChat = ChatRoom.objects.filter(Q(User_1=user) | Q(User_2=user))
      return GetAllChat

 
class getAllMessages(generics.ListAPIView):
   serializer_class = messageSerializer
   permission_classes = [IsAuthenticated]
   def get_queryset(self):
      User_1=self.request.user
      User_2=self.request.data['user_2']

      GetChatRoomId = ChatRoom.objects.filter(Q(User_1=User_1 , User_2=User_2) | Q(User_1=User_2  , User_2=User_1)).first()

      if GetChatRoomId:
         return Message.objects.filter(ChatRoom=GetChatRoomId)
      return []
   


class sendMessage(generics.CreateAPIView):
   serializer_class=messageSerializer
   permission_classes =[AllowAny]
   def post(self,request):
      User_1=self.request.user
      Employee_id=request.data['Employee_id']
      User_2=Employees.objects.get(Employee_id=Employee_id)
 
      
      GetChatRoom = ChatRoom.objects.filter(Q(User_1=User_1 , User_2=User_2) | Q(User_1=User_2  , User_2=User_1))
      if not GetChatRoom.exists():
         ChatRoom.objects.create(User_1=User_1, User_2=User_2)
      
      chatRoom_id=GetChatRoom[0]
      Message.objects.create(ChatRoom=chatRoom_id,Sender=User_1,Receiver=User_2,Message=request.data['Message'])
      return response.Response({"success":"message sent"})

      

