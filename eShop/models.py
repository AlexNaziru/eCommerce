from django.db import models


class Product(models.Model):
    def __str__(self):  # Dynamic title in the admin page
        return self.title
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)


class Order(models.Model):
    items = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
