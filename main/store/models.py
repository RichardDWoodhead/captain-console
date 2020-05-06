from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField()