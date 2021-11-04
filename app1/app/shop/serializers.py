from rest_framework import serializers

from app.shop.models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'description']

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance
