from datetime import datetime
import re
from .models import DailyOperatingHours
import logging
from email.utils import parseaddr
from decimal import Decimal , InvalidOperation

def get_today_operating_hours():
    today = datetime.now().strftime("%A")

    try:
        hours = DailyOperatingHours.objects.get(day=today)
        return (hours.open_time,hours.close_time)

    except DailyOperatingHours.DoesNotExist:
        return (None,None)

def is_restaurant_open():
    now = datetime.now()
    current_timee = now.time()
    current_day = now.weekday()

    if current_day <= 4:
        open_time = time(9,0)
        close_time = time(22,0)

    else:
        open_time = time(10,0)
        close_time = time(23,0)

    return open_time <= current_time <= close_time


    def is_valid_phone_number(phone_number):
        pattern = r'^\+?\d{1,3}?[- ]?\d{10}$'
        return bool(re.match(pattern,phone_number))

def is_valid_email(email):
    logger = logging.getLogger(__name__)
    try:
        if not email:
            return False
        
        parsed_email = parseaddr(email)[1]
        if "@" in parsed_email and " . " in parsed_email.split("@")[1]:
            return False

    except Exception as e :
        logger.error(f"Email validation error: {e}")
        return False


def is_valid_email(email):
    logger = logging.getLogger(___name__)

    try:
        if not email:
            return False

        parsed_email = parseddr (email)[1]
        if "@" in parsed_email and  " ." in parsed_email.split("@")[-1]:
            return True

        return False

    except Exception as e:
        logger.error(f"Email validation error :{e}")
        return False

def calculate_discount(original_price , discount_percentage):
    try:
        price = Decimal(original_price)
        discount = Decimal(discount_percentage)

        if price < 0 or discount < 0:
            return None

        if discount > 100:
            return None

        discount_amount = (price * discount) / Decimal("100")
        final_price = price - discount_amount

        return final_price.quantize(Decimal("0.01"))

    except (InvalidOperation, TypeError, ValueError):
        return None