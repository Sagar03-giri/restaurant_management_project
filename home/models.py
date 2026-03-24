from django.db import models
import datetime
from django.db.models import Count
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class Reservation(models.Model):
    custmer_name = models.CharField(max_length = 100)
    reservation_time = models.datetimeField()
    duration = models.IntegerField(default=60)

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_time}"

    @staticmethod
    def get_available_slots(start_time, end_time , slot_duration=60):
        available_slots = []
        current_time = start_time

        while current_time < end_time:
            slot_end = current_time + timedelta(minutes=slot_duration)

            conflict = Reservation.objects.filter(
                reservation_time__lt=slot_end,
                reservation_time__gte=current_time
            ).exists()

            if not conflict:
                available_slots.append((current_time , end_time))

            current_time += timedelta(minutes=slot_duration)

        return available_slots



class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name    #i have done this in vs.code


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    has_delivery = models.BooleanField(default=False)
    operating_days = models.CharField(
        max_length=100,
        help_text="comma-saparated days like Mon,Tue,Wed"
        )
    def __str__(self):
        return self.name       

class MenuItemManager(models.Manager):
    def get_top_selling_items(self,num_items=5):
        return (self.annotate(order_count=Count('orderitem'))
        .order_by('-order_count')[:num_items]
        )        

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)
    is_daily_special = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    objects = MenuItemManager()
    
    def __str__(self):
        return self.name

class DailySpecialManager(models.Manager):
    def upcoming(self):
        today = datetime.date.today()
        return self.filter(date__gte=today)
        

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_random_special():
        special = DailySpecial.objects.order_by('?').first()
        

class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digit=5,decimal_places=2)
    fat_grams = models.DecimalField(max_digit=5,decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digit=5,decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} - {self.calories} kcal"        

class ContractFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"



class UserReview(models.model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rating = models.integerField()
    comment = models.TextField(blank=True , null=True)
    review_date = models.datetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.menu_item} ({self.rating})"