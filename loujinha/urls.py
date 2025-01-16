from django.urls import path
from . import views

app_name = 'loujinha'

urlpatterns = [
    path('', views.home, name='home'),
#    path('', views.add_product, name='add_product'),  # Adiciona a rota principal
#    path('success/', views.success, name='success'),  # Rota para página de sucesso
#    path('list/', views.list_products, name='list_products'),  # Rota para listar produtos
]