import requests

# 設定 API URL
url = "http://127.0.0.1:8000/api/test/"  # 替換為你的 API URL

# 發送 GET 請求
response = requests.get(url)

# 檢查響應狀態
if response.status_code == 200:
    data = response.json()  # 解析 JSON 響應
    print("Received data:", data)
else:
    print("Failed to retrieve data:", response.status_code)
