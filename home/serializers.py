from rest_framework import serializers
from .models import MenuCategory, MenuItem,Ingredient,Table
from orders.models import Order
from orders.models import OrderStatus
from orders.models import PaymentMethod
#from .models import Table

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'

class  MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def validate_price(self,value):
        if value <= 0 :
            raise serializers.ValidationError("price must be positive.")
        return value


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number','capacity','is_available']

class ContatFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatFormSubmission
        fields = '__all__'

class OrderStatusUpdateSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    status = serializers.CharField()

    def validate_status(self, value):
        if not OrderStatus.objects.filter(name__iexact=value).exist():
            raise serializers.ValidationError("Invalid status provided.")

        return value

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id' , 'name', 'price', 'category']