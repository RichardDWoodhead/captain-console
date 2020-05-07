from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField()
    def __str__(self):
        return self.status

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    mainimage = models.BooleanField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class ProductOrder(models.Model):
    cardholder_name = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=255)
    exp = models.IntegerField()
    cvv = models.CharField(max_length=5)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)