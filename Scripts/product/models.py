from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _ #as _ , um es als _ zu benutzen


PRODUCT_FLAG ={
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New'),
}

# Create your models here.
class Product(models.Model):
   name =models.CharField(_('Name'),max_length=150)
   img= models.ImageField(_('img'),upload_to='products/',default='default.png')
   flag=models.CharField(_('flag'),max_length=10,choices=PRODUCT_FLAG)
   price =models.FloatField(_('price'))
   sku= models.IntegerField(_('sku'))
   brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.CASCADE) #CASCADE delete all the related products ,if the brand is deleted
   tags = TaggableManager()
   subtitle = models.TextField(_('subtitle'),max_length=500)
   description = models.TextField(_('description'),max_length=200)

   def __str__ (self):
    return self.name
'''
name 
flag
img
price
sku
brand
tags
subtitle
description
'''

class Images(models.Model):
    pass
'''
img
product: foreignkey
'''

class Reviews(models.Model):
    pass
'''
rate
user
date
review
product
'''

class Brand(models.Model):
    pass
'''
name
img

'''
