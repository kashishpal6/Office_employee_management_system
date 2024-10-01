from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json 
from Chat.models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        room=self.scope['url_route']['kwargs']['room']
        self.room_name = f"{room}"
        self.room_group_name = f"{room}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':"Connected"}))

    def sendMessage(self , event) : 
        print("ye wala bhi chal rha h ")
        message = event["message"]
        username = event["username"]
        self.send(text_data = json.dumps({"message":message ,"username":username}))
        

    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)
        username = text_data_json["username"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })
        

    def disconnect(self , close_code):
        print("disconnected")