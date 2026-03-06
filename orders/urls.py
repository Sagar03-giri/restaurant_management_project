from django.urls import path
from .views import *
from .views import CouponValidationView
from .views import OrderDetailView
from .views import PaymentMethodListAPIView
from .views import CancelOrderAPIView
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

    path(
        "cancel-order/<int:order_id>/",
        CancelOrderAPIView.as_view(),
        name="cancel-order"
    ),

    path(
        "update-order-status/",
        UpdateOrderStatusAPIView.as_view(),
        name="update-order-status"
    ),
]