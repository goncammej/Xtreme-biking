from django.contrib import admin

from order.models import Order, OrderItem, ShippingAddress, CustomerReviews, CustomerClaims

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(CustomerReviews)
admin.site.register(CustomerClaims)