import string
import secrets 
from django.db.model import Sum
from .models import Coupon, Order

def generate_coupon_code(length=10):

    characters = string.ascii_uppercase + string.digits

    while True:
        code = ' '.join(secrets.choice(characters)for _in range(length))

        if not Coupon.object.filter(code=code).exists():
            return code

def get_daily_sales_total(date):
    orders = Order.objects.filter(created_at__date=date)
    result = orders.aggregate(total_sum=Sum('total_price'))
    return result['total_sum'] or 0