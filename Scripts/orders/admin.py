from django.contrib import admin

# Register your models here.
from .models import Order,Orderdetail,Cart,Cartdetail

admin.site.register(Order)
admin.site.register(Orderdetail)

admin.site.register(Cart)
admin.site.register(Cartdetail)