from django.contrib import admin

from client.models import CustomerShipping, CustomerPaymentMethod

# Register your models here.
admin.site.register(CustomerPaymentMethod)
admin.site.register(CustomerShipping)