import string
import secrets
from .models import Coupon

def generate_coupon_code(length=10):

    characters = string.ascii_uppercase + string.digits

    while True:
        code = ' '.join(secrets.choice(characters)for _in range(length))

        if not Coupon.object.filter(code=code).exists():
            return code