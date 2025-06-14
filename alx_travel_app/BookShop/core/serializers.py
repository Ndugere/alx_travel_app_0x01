# core/serializers.py
from rest_framework import serializers
from .models import User, Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    shop_name     = serializers.CharField(source="user.shop_name", read_only=True)

    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'quantity',
            'price',
            'category',
            'category_name',
            'shop_name',
            'in_stock',
        ]
        read_only_fields = ['in_stock', 'shop_name', 'category_name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'shop_name']
