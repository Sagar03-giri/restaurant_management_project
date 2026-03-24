from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'menu-categories' , MenuCategoryViewSet)

urlpatterns = [
    path(
        '' , include(router.urls)
    ),
    path(
        'menu-categories/',MenuCategoryListView.as_view(),
        name='menu-categories'),
    path(
        'api/menu-items/<int:pk>/ingredients/',
        MenuItemIngredientsView.as_view(),
        name = 'menuitem-ingredients'

    ),

    path('menu-items-by-category/' , 
    MenuItemsByCategoryView.as_view(),
    name='menu-items-by-category'
    ),
    
    path (
        'api/atbles/<int:pk/' ,
        TableDetailView.as_view()
        name = 'table-detail'
    ),

    path (
        'api/tables/available/',
        AvailableTablesAPIView.as_view(),
        name = 'available_tables_api'

    ),

    path(
        'contact/' , 
        ContactFormSubmissionView.as_View(),
        name='contact-form'),

    path(
        ('daily-specials/' ,
        DailySpecialListAPIView.as_View(), name='daily-specials'
        
    ),
    path(
        'review/create/' , CreateReviewAPIView(), name = 'create-review'
    ),
    path(
        'review/menu-item/<int:menu_item_id>/' ,
        MenuItemReviewListAPIView.as_view(),
        name = 'menu-item-reviews'
    ),

    path(
        'restaurant-info/' , RestaurantInfoAPIView.as_View(),'restaurant-info'
    ),

    path(
        'menu-items/<int:item_id>/availability/',
        update_menu_item_availability
    ),
]