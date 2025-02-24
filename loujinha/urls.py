from django.urls import path
from . import views

app_name = 'loujinha'

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/<int:id>/', views.product, name="product"),
]
#    path('', views.add_product, name='add_product'),  
#    path('success/', views.success, name='success'), 