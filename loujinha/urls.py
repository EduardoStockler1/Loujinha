from django.urls import path
from loujinha import views

urlpatterns = [
    path('', views.home),
]
