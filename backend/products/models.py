from decimal import Decimal
from django.db import models


class Product (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    def __str__ (self):   
        return self.title
    def my_discount(self):
        decimal_1= Decimal(.1)   
        discount = decimal_1*self.price
        discount = round(discount,ndigits=2)
        return discount

