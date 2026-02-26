from django.urls import path
from .views import *

urlpatterns = [
    path('menu-categories/',MenuCategoryListView.as_view(),name='menu-categories'),
    
]