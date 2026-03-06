from django.urls import path
from .views import *
from .views import CouponValidationView
from .views import OrderDetailView
from .views import PaymentMethodListAPIView

urlpatterns = [
    path(
        'coupons/validate/',CouponValidationView.as_view(),name='validate-coupon'
        ),
    

path(
    'orders/<int:pk>',
    OrderDetailView.as_view(),
    name='order-detail'
),    

path(
    'payment-method/' ,
    PaymentMethodListAPIView.as_view(),
    name = 'payment-methods'
),
]