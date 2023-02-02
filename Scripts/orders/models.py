from django.db import models
from django.utils import timezone
from product import Product
# Create your models here.
ORDER_STATUS =(
    ('Recieved','Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered','Delivered'),
)


class Order(models.Model):
    order_code=models.CharField(max_length=10)
    user = ''
    orderStatus= models.CharField(max_length=12,choices=ORDER_STATUS,default='Recieved')
    deliveryDate=models.DateTimeField(null=True,blank=True)
    orderDate=models.DateTimeField(default=timezone.LocalTimezone)


class Orderdetail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_Product',on_delete=models.SET_NULL,null=True,blank=True)

class Order2(models.Model):
    text=models.TextField()