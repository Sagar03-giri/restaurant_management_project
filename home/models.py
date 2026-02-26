from django.db import models

# Create your models here.


class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name    #i have done this in vs.code


class Restaurent(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    has_delivery = models.BooleanField(default=False)
    def__str__(self):
        return self.name        

class MenuItem(models.Model):
    name = modelss.CharField(max_length=100)
    price = models.DecimalField(max_digit=8,decimal_places=2)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def__str__(self):
        return self.name