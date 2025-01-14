from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    ...

admin.site.register(Product, ProductAdmin)
