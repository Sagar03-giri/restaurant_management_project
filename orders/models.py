from django.db import models
from django.contrib.auth.models import User

class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class OrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__name__in=['pending','processing'])

class Order(models.Model):
    user = ForeignKey(User,on_delete=models.CASCADE)
    
    total_price = models.DecimalField(max_digit=10,decimal_places=2)

    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True) 
    
    objects = OrderManager()

    def __str__(self):
    return f"Oreder{self,id}"

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digit=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DataField()
    valid_until = models.DataField()

    def __str__(self):
        return self.code