# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET request received"}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        return Response({"message": "POST request received", "data": data}, status=status.HTTP_201_CREATED)
