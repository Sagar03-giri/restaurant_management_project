import string
import secrets 
import logging
from decimal import Decimal, ROUND_HALF_UP
from django.db.models import Sum
from .models import Coupon, Order
from .models import Order, OrderStatus

logger = logging.getLogger(__name__)

def calculate_order_total(order_items):
    if not order_items:
        return Decimal("0.00")
    total = Decimal("0.00")

    for item in order_items:
        price = Decimal(item.get("price",0))
        quantity = int(item.get("quantity",0))

        if price < 0 or quantity <0:
            continue
        total += price * quantity
    return total


def generate_coupon_code(length=10):

    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exists():
            return code

def generate_order_id(length=8):
    characters = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.choice(characters) for _ in range(length))

        if not Order.objects.filter(order_id=order_id).exists():
            return order_id
        
def get_daily_sales_total(date):
    orders = Order.objects.filter(created_at__date=date)
    result = orders.aggregate(total_sum=Sum('total_price'))
    return result['total_sum'] or 0

def calculate_tip_amount(order_total, tip_percentage):
    order_total = Decimal(order_total)
    tip = order_total * (Decimal(tip_percentage) / Decimal(100))
    return tip.quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)

def update_order_status(order_id, new_status):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f"Order with ID {order_id} not found.")
        return {"error":"Order not found"}

    try :
        status_obj = OrderStatus.objects.get(name__iexact=new_status)
    except Orderstatus.DoesNotExist:
        logger.error(f"Invalid status provided:{new_status}")

            return {"error":"Invalid status provided"}

        Old_status = order.status.name if order.status else None

        order.status = status_obj
        order.save()

        logger.info(f"Order {order_id} status changed from '{old_status} ' to ' {new_status}' . ")
        return {"message":"Order status updated successfully"}