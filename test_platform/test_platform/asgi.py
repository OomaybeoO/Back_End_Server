# test_platform/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from websocket import routing  # 引入 websocket 的路由

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_platform.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # 使用 WebSocket 路由
        )
    ),
})
