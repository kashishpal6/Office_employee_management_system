from django.urls import path
from .views import GetAllChat,chatRoom_list,getAllMessages,sendMessage

urlpatterns = [
   path('chatroom_list/',chatRoom_list.as_view(),name="list_chatroom"),
   path('chat_list/',GetAllChat.as_view(),name="chat_list"),
   path('message_list/',getAllMessages.as_view(),name="message_list"),
   path('sendMessage/',sendMessage.as_view(),name="message_send")
]
