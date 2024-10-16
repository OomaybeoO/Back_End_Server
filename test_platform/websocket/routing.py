# websocket/routing.py
from django.urls import path
from . import consumers  # 引入消費者

websocket_urlpatterns = [
    path('ws/test/', consumers.TestConsumer.as_asgi()),  # 設定 WebSocket 路由
]
