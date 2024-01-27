from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)

