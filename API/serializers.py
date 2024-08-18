from rest_framework import serializers
from Goods.models import Category, Product, Cart

from Goods.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'img']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'description']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'author', 'is_active', 'shopping_date']
