from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.shop.serializers import ShopCreateSerializer


class ShopCreateView(CreateAPIView):
    serializer_class = ShopCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # 데코레이터로 빼기
        # kafka producer send
        print(response.data)
        return response
