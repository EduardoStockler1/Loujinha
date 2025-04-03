from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .custom_user import CustomUser
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    description = models.TextField(max_length=255, null=True, blank=True)
    slug = models.SlugField(default="default-slug")
    quantity = models.IntegerField()
    cover = models.ImageField(upload_to='loujinha/covers/', null=True, blank=True)       
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

