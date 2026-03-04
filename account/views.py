from django.shortcuts import render
from rest_framework.response import response
from django.contrib.auth.models import User
from home.serializers import UserProfileSerializer

class UserProfileViewSet(viewset.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def update(self,request,pk=None):
        user = request.user

        if user.id != int(pk):
            return Response(
                {"error": "you can only update your own profile"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = UserProfileSerializer (user , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_REQUEST)
# Create your views here.
