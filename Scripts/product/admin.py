from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Reviews,Images

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Reviews)
admin.site.register(Images)
