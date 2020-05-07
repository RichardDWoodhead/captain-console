from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    message = models.CharField(max_length=999)

    def __str__(self):
        return self.name