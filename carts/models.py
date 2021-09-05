from django.db import models
from shopapp.models import *
# Create your models here.
class cartlist(models.Model):
    cartid=models.CharField(max_length=225,unique=True)
    cartdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cartid
class item(models.Model):
    prd=models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    qlt=models.IntegerField()


    active=models.BooleanField(default=True)
    def __str__(self):
        return self.prd
    def total(self):
        return self.prd.price*self.qlt
