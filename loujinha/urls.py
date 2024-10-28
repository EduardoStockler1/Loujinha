from django.urls import path
from loujinha import views

app_name = 'loujinha'

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('success/', views.success, name='success'),
]
