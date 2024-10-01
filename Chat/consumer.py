from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json 
from Chat.models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer"
        async_to_sync = (self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':"Connected"}))

    def sendMessage(self , event) : 
        print("ye wala bhi chal rha h ")
        message = event["message"]
        username = event["username"]
        self.send(text_data = json.dumps({"message":message ,"username":username}))
        

    def receive(self, text_data):
        print("chal rha h ")

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        self.channel_layer.group_send(
            self.room_group_name,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })
        

    def disconnect(self , close_code):
        print("disconnected")