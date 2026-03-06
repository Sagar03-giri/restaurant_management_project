from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import Coupon
from rest_framework.generics import RetrieveAPIView
from orders.models import Order , OrderStatus
from home.serializers import OrderSerializer
from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from home.serializers import PaymentMethodSerializer

class CouponValidationView(APIView):
    def post(self,request):
        code = request.data.get("code")

        if not code:
            return Response(
                {"error":"Coupon code required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response( 
                {"error":"invalid coupon"},
                status=status.HTTP_400_BAD_REQUEST
            )    
        today = now().date()

        if not coupon.is_active or not(coupon.valid_from <= today <=coupon.valid_until):
            return Response(
                {"error":"coupon expired or invalid"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            "success":True,
            "discount_percentage":coupon.discount_percentage
        })    

class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UpdateOrderStatusAPIView(APIView):
    def put(self, request):
        serializer = OrderUpdateSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validate_data["order_id"]
            status_name = serializer.validate_data["status"]

            try:
                order = Order.objects.get(id=order_id)

            except Order.DoesNotExist:
                return Response(
                    {"error":"Order not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            order_status = OrderStatus.objects.get(name__iexact=status_name)
            order.status=order_status
            order.save()
            
            return Response(
                {"message":"Order status updated successfully"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PaymentMethodListAPIView(ListAPIView):
    serializer_class = PaymentMethodSerializer

    def get_queryset(self):
        return PaymentMethod.objects.filter(is_active=True)

class CancelOrderApiView(APIView):
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id):
        except Order.DoesNotExist:
            return Response(
                {"error":"order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if order.user != request.user:
            return Response(
                {"error":"you are not allowed to cancel this order},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            cancelled_status = OrderStatus.objects.get(name__iexact="cancelled")
        except OrderStatus.DoesNotExist:
            return Response(
                {"error":"Cancel status not configured"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = cancelled_status
        order.save()

        return Response(
            {"message":"Order cancelled successfully"},
            status=status.HTTP_200_OK
        )

class UpdateOrderStatusAPIView(APIView):
    def post(self, request):
        order_id = request.data.get("order_id")
        new_status = request.data.get("status")

        if not order_id or not new_status:
            return Response(
                {"error":"order_id and status are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {"error":"Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            status_obj = OrderStatus.objects.get(name__iexact=new_status)
        except OrderStatus.DoesNotExist:
            return Response(
                {"error":"invalid status provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = status_obj
        order.save()

        return Response(
            {"message":"Order status updated successfully"},
            status=status.HTTP_200_OK
        )