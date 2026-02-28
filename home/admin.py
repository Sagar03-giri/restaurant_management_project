from django.contrib import admin
from .models import MenuCategory , MenuItem,Resturant

class ResturantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','phone_number','email')
    search_fields = ('name','address')
    list_filter = ('is_active',)

admin.site.register(MenuCategory,   MenuCategoryAdmin)
admin.site.site.register(Resturant,ResturantAdmin)

# Register your models here.
