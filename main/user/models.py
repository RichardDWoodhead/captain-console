from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import ForeignKey
import django.contrib.auth.models
from store.models import Product

# Create your models here.


class User(models.Model):
    user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone_number = models.IntegerField(blank=True)
    profile_pic = models.CharField(max_length=255, blank=True)
    search_history = ArrayField(models.CharField(max_length=140, default=list, blank=True))


class ProfilePicture(models.Model):
    image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    search_history = models.ForeignKey(SearchHistory, on_delete=models.CASCADE)
    profile_pic = models.ForeignKey(ProfilePicture, on_delete=models.CASCADE)