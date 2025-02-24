from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from utils.products.factory import make_product
from .models import Product

def home(request):
    ...
    products = Product.objects.all()
    return render(request, 'loujinha/pages/home.html', context={
        'products': products,
        'is_home_page': True,
        'is_detail_page': False,
    }) 
def product(request, category_id):
    ...
    products = Product.objects.filter(
        category_id=category_id,
        is_published = True,
    ).order_by('-id')
    return render(request, 'loujinha/pages/product-view.html', context={
        'products': products,
        'is_detail_page': True,
        'is_home_page': False,
    })

def inventory(request):
    ...
    products = Product.objects.all()
    return render(request, 'loujinha/pages/inventory.html', context={
        'products': products,
        'is_home_page': False,
        'is_detail_page': False,
        'is_inventory_page': True,
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
