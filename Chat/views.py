from django.shortcuts import render
from Chat import serializers
from Chat.serializers import chatSerializer,messageSerializer
from rest_framework import generics
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
      user_1=self.request.user
      user_2_id=self.request.data['user_2']
      user_2=Employees.objects.get(Employee_id=user_2_id)

      GetChatRoomId = ChatRoom.objects.filter(Q(User_1=user_1 , User_2=user_2) | Q(User_1=user_2  , User_2=user_1))
      import pdb
      pdb.set_trace()
      try:
         getAllMessages = Message.objects.filter(ChatRoom__id=GetChatRoomId)
      except:
         return []
      return getAllMessages
   


class sendMessage(generics.CreateAPIView):
   serializer_class=messageSerializer
   permission_classes =[IsAuthenticated]
   def post(self,request):
      sender=self.request.user
      receiver_id=self.request.data
      receiver=Employees.objects.get(Employee_id=receiver_id)

      GetChatRoomId = ChatRoom.objects.get_or_create(Q(User_1=sender , User_2=receiver) | Q(User_1=receiver  , User_2=sender))

      

