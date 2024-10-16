# websocket/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # 接受 WebSocket 連接

    async def disconnect(self, close_code):
        pass  # 斷開連接時的邏輯

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # 確保正確提取信息
        message = text_data_json.get('message', {})
        user = message.get('user')
        action_code = message.get('action_code')
        args = message.get('args')

        # 發送消息回去
        await self.send(text_data=json.dumps({
            'user': user,
            'action_code': action_code,
            'args': args
        }))
