from django.contrib import admin

from orders.models import OrderItem, Orders

admin.site.register(Orders)
admin.site.register(OrderItem)