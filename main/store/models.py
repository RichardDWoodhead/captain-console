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


class Order(models.Models):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product