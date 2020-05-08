from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.CharField(max_length=999)
    def __str__(self):
        return self.name