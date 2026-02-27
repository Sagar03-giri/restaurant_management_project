import string
import secrets 
from decimal import Decimal, ROUND_HALF_UP
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

def calculate_tip_amount(order_total, tip_percentage):
    order_total = Decimal(order_total)
    tip = order_total * (Decimal(tip_percentage) / Decimal(100))

return tip.quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)