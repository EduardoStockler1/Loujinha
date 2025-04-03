from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import ProductForm, CustomAuthenticationForm, CustomUserCreationForm
from .models.product import Product
from .models.product import Product

def home(request):
    products = get_list_or_404(
        Product.objects.all().order_by('-id')
    )

    return render(request, 'loujinha/pages/home.html', context={
        'products': products,
        'is_home_page': True,
        'is_detail_page': False,
    }) 

def product(request, id):
    product = get_object_or_404(Product.objects.filter(id=id)
    ) 
    
    return render(request, 'loujinha/pages/product_view.html', context={
        'product': product,
        'is_detail_page': True,
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

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loujinha:home')
    else:
        form = ProductForm()
    return render(request, 'loujinha/pages/add_product.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loujinha:home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'loujinha/pages/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")

            return redirect('loujinha:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'loujinha/pages/register.html', {'form': form})

#def success(request):
#    return render(request, 'loujinha/success.html')
#
