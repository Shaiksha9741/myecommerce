from django.contrib import admin
from ecommerceapp.models import Contact
from ecommerceapp.models import Product
from ecommerceapp.models import Order
from ecommerceapp.models import OrderUpdate

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)
