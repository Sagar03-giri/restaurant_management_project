from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import viewset , status
from rest_framework.response import Response
from .models import MenuCategory , MenuItem
from rest_framework.permission import IsAdminUser
from .serializers import MenuCategorySerializer , MenuItemSerializer
from .serializers import (MenuCategorySerializer,MenuItemSerializer,IngredientSerializer,)
from rest_framework.views import ListAPIView
from .models import Table
from .serializer import TableSerializer
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


class MenuItemIngredientsView(RetrieveAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        menu_item = MenuItem.objects.get(pk=self.kwargs["pk"])
        return menu_item.ingredients.all()

class MenuItemsByCategoryView(APIView):
    def get(self,request):
        category_name = request.query_params.get('category')

        if category_name :
            items = MenuItem.objects.filter(
                category__name__iexact=category_name
                )

        else :
            items = MenuItem.objects.all()

        serializer = MenuItemSerializer(items, many = True)
        rerurn Response (serializer.data)

class TableDetailView(RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer