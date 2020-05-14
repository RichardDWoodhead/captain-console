from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=9999)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=CASCADE)
    description = models.TextField()
    year_published = models.CharField(max_length=255)
    status = models.BooleanField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.status


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    main_image = models.BooleanField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Order(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10)


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
        return str(self.product)
