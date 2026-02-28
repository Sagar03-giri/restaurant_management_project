from django.urls import path
from .views import *
from .views import CouponValidationView
from .views import OrderDetailView

urlpatterns = [path('coupons/validate/',CouponValidationView.as_view(),name='validate-coupon'),
    

path(
    'orders/<int:pk>',
    OrderDetailView.as_view(),
    name='order-detail'
),    
]