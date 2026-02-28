from rest_framework import serializers
from .models import MenuCategory, MenuItem,ingredient
from orders.models import Order
from .models import Table

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']

class  MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def validate_price(self,value):
        if value <= 0 :
            raise serializers.ValidationError("price must be positive.")
        resturn value


class ingredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingredient
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number','capacity','is_available']