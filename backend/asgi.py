"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack 
from Chat.consumer import *
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()

ws_patterns = [
    path('ws/chat/',ChatConsumer.as_asgi()),
    path('ws/online/',ChatConsumer.as_asgi()),
    path('ws/notify/',ChatConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_patterns))
    
})
