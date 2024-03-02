from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'title', 'price', 'created_at', 'in_stock', 'image']

    def create(self, validated_data):
        validated_data['in_stock'] = True
        return super().create(validated_data)



