from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loujinha:success')  # Usa o namespace do app
    else:
        form = ProductForm()
    return render(request, 'loujinha/add_product.html', {'form': form})

def success(request):
    return render(request, 'loujinha/success.html')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'loujinha/list_products.html', {'products': products})
