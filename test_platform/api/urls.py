# api/urls.py
from django.urls import path
from .views import TestAPIView

urlpatterns = [
    path('api/test/', TestAPIView.as_view(), name='test_api'),  # 設定 RESTful API 路由
]
