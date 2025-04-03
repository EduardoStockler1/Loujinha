from django.urls import path
from . import views

app_name = 'loujinha'

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/<int:id>/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
#    path('success/', views.success, name='success'), 

