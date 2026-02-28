from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import Coupon
from rest_framework.generics import RetrieveAPIView
from oreders.model import Oreders
from home.serializers import OrderSerializer

class CouponValidatonView(APIView):
    def post(self,request):
        code = request.data.get("code")

        if not code:
            return Response(
                {"error":"Coupon code required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            coupon = Coupon.object.get(code=code)
        except Coupon.DoesNotExist:
            return Response( 
                {"error":"invalid coupon"},
                status=status.HTTP_400_BAD_REQUEST
            )    
        today = now().date()

        if not coupon.is_active or not(coupon.valid_form <= today <=coupon.valid_until):
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
    serializers_class = OrderSerializer