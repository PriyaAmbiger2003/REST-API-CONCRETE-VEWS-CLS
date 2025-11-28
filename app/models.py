from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    rating=models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)
