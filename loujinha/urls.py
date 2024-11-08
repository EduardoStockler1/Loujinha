from django.urls import path
from loujinha import views

app_name = 'loujinha'

urlpatterns = [
    path('', views.add_product, name='add_product'),
    path('success/', views.success, name='success'),
    path('list', views.list, name='list'),
]
