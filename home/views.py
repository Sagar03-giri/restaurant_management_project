from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewset , status
from rest_framework import Response
from .models import MenuCategory , MenuItem
from .serializers import MenuCategorySerializer , MenuItemSerializer

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemUpdateViewSet(viewset.ViewSet):
    permission_classes = [IsAdminUser]

    def update(self , request ,pk=None):
        try:
            item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response(
                {"error":"Menu item not found"},
                status = status.HTTP_404_NOT_FOUND
                )
        serializer = MenuItemSerializer(item,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)