from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max length = 100)
    total_price = models.DecimalField(max_digit=10,decimal_places=2)

    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True) 

# Create your models here.


class OrderStatus(model.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name