from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json 
from Chat.models import *

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer"
        async_to_sync = (self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':"Connected"}))

    def sendMessage(self,event):
        pass

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status':"We got you"}))
    def disconnect(self , close_code):
        print("disconnected")
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         import pdb
#         pdb.set_trace()
#         current_user_id = self.scope['user'].Employee_id
#         other_user_id = self.scope['url_route']['kwargs']['Employee_id']
#         self.room_name = (
#             f'{current_user_id}_{other_user_id}'
#             if int(current_user_id) > int(other_user_id)
#             else f'{other_user_id}_{current_user_id}'
#         )
#         self.room_group_name = f'chat_{self.room_name}'
#         self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         self.accept()
    
#     async def disconnect(self , close_code):
#         await self.channel.name.group_discard(
#             self.roomGroupName , 
#             self.channel_name 
#         )
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         username = text_data_json["username"]
#         await self.channel_layer.group_send(
#             self.roomGroupName,{
#                 "type" : "sendMessage" ,
#                 "message" : message , 
#                 "username" : username ,
#             })
#     async def sendMessage(self , event) : 
#         message = event["message"]
#         username = event["username"]
#         await self.send(text_data = json.dumps({"message":message ,"username":username}))
      