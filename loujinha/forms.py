# meu_app/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'quantity', 'cover']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
