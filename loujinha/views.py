from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from utils.products.factory import make_product

def home(request):
    ...
    return render(request, 'loujinha/pages/home.html', context={
        'products': [make_product() for _ in range(20)],
        'is_home_page': True,
        'is_detail_page': False,
    })

def product(request, id):
    ...
    return render(request, 'loujinha/pages/product-view.html', context={
        'product': make_product(),
        'is_detail_page': True,
        'is_home_page': False,
    })
#
#def add_product(request):
#    if request.method == 'POST':
#        form = ProductForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('loujinha:success')
#    else:
#        form = ProductForm()
#    return render(request, 'loujinha/add_product.html', {'form': form})
#
#def success(request):
#    return render(request, 'loujinha/success.html')
#
#def list_products(request):
#    products = Product.objects.all()
#    return render(request, 'loujinha/list_products.html', {'products': products})
#