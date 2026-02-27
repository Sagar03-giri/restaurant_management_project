from datetime import datetime
import re
from .models import DailyOperatingHours

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




