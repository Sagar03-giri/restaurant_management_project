from django.contrib import admin

# Register your models here.
from  .models import Order, OrderStatus

def mark_orders_processed(modeladmin, request , queryset):
    try:
        processed_status = OrderStatus.objects.get(name="processed")
        query.update(status=processed_status)

    except OrderStatus.DoesNotExist:
        modeladmin.message_user(
            request,
            "processed status does not exist ."
        )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id' , 'customer_name', 'status')
    actions = [mark_orders_processed]

admin.site.register(Order , OrderAdmin)