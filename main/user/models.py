from django.db import models
from django.contrib.postgres.fields import ArrayField
#from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255, blank=True)
    searchhistory = ArrayField(models.CharField(max_length=140, default=list))
    # cardholder_name = models.CharField(max_length=255)
    # cardnumber = models.CharField(max_length=255)
    # exp = models.IntegerField()
    # cvv = models.CharField(max_length=5)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)