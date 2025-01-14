# loujinha/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator (0.01), MaxValueValidator(1000.00)
    ])
    description = models.TextField()
    quantity = models.IntegerField()
    cover = models.ImageField(upload_to='loujinha/covers/%Y%m%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null = True
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )
    def __str__(self):
        return self.author
