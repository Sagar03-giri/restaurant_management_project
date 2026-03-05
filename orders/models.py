from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from home.models import MenuItem

class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class OrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__name__in=['pending','processing'])

    def by_status(self, status_name):
        return self.filter(status__name__iexact=status_name)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True) 
    
    objects = OrderManager()

    def calculate_total(self):
        total = Decimal("0.00")
        for item in self.orderitem_set.all():
            total += item.price*item.quantity
        return total

    def get_unique_item_names(self):
        unique_names = set()
        for order_item in self.orderitem_set.all():
            unique_names.add(order_item.menu_item.name)
        return list(unique_names)

    def __str__(self):
        return f"Order{self.id}"

class OrderItem(models.Model):
    Order = models.ForeignKey(order,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code


class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=50,unique=True)
    points_required = models.IntegerField(unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name