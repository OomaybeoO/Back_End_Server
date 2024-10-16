import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/test/"  # 替換為你的 WebSocket URL

    try:
        async with websockets.connect(uri) as websocket:
            # 構造一個測試訊息，包含 message 鍵
            test_message = {
                "message": {
                    "user": "test_user",
                    "action_code": "1234",
                    "args": ["0110"]
                }
            }

            # 將訊息轉換為 JSON 並發送
            await websocket.send(json.dumps(test_message))
            print(f"> Sent: {test_message}")

            # 接收來自伺服器的回應
            response = await websocket.recv()
            response_data = json.loads(response)
            print(f"< Received: {response_data}")

            # 確保伺服器的回應與預期的相符
            assert response_data['user'] == "test_user"
            assert response_data['action_code'] == "1234"
            assert response_data['args'] == ["0110"]

    except websockets.ConnectionClosed as e:
        print(f"Connection closed with code: {e.code}, reason: {e.reason}")

    except Exception as e:
        print(f"An error occurred: {e}")

# 啟動測試
asyncio.run(test_websocket())
