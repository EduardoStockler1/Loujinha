# loujinha/models.py
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)  # Ou use um ForeignKey para uma tabela de categorias
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
