# Django 測試平台

這是一個使用 Django 和 Channels 建立的測試平台，支援 WebSocket 和 RESTful API。

## 目錄

- [功能](#功能)
- [技術棧](#技術棧)
- [安裝](#安裝)
- [使用方式](#使用方式)
- [測試](#測試)
- [貢獻](#貢獻)
- [許可證](#許可證)

## 功能

- 提供 RESTful API 進行資料操作。
- 使用 WebSocket 實現即時通訊功能。

## 技術棧

- Django
- Django Channels
- Django REST framework
- WebSockets
- Python 3.x
- Requests (用於發送 HTTP 請求)

## 安裝

### 1. 克隆專案

```bash
git clone <你的專案網址>
cd <專案資料夾>
```

### 2. 建立虛擬環境

```bash
python -m venv .venv
```

### 3. 啟用虛擬環境

- Windows:

```bash
.\.venv\Scripts\activate
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方式

1. 啟動 Django 開發伺服器：

```bash
python manage.py runserver
```

2. WebSocket 連接：

   - 使用以下 URL 進行 WebSocket 連接：
   ```plaintext
   ws://127.0.0.1:8000/ws/test/
   ```

3. RESTful API 測試：

   - 使用 Postman 或 curl 測試 RESTful API 端點。

## 測試

要運行測試，請使用以下命令：

```bash
python manage.py test
```

## 貢獻

如果你想為此專案做出貢獻，請遵循以下步驟：

1. Fork 此專案。
2. 創建你的特性分支 (`git checkout -b feature/YourFeature`)。
3. 提交你的更改 (`git commit -m 'Add some feature'`)。
4. 推送到分支 (`git push origin feature/YourFeature`)。
5. 提交拉取請求。

## 許可證

本專案使用 MIT 許可證。詳情請參見 [LICENSE](LICENSE) 文件。
