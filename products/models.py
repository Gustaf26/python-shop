from django.db import models

# Representations of a real-life concept
# Create your models here.

# The Model class from db gives us capabilities to deal with db
# for instance (read / delete / update)


class Product(models.Model):
    name = models.CharField(max_length=255)  # Textual data
    price = models.IntegerField()   # Integer number
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # Maximum standard length
    # for links / urls

# Model for product offer


class Offer(models.Model):
    code = models.CharField(max_length=255)  # Textual data, coupon code
    description = models.CharField(max_length=1200)  # Integer number
    discount = models.FloatField()  # 20% of all products


