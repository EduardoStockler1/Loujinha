from django.contrib import admin
from .models.product import Category, Product
from .models.custom_user import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    ...

admin.site.register(CustomUser, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    ...

admin.site.register(Product, ProductAdmin)
