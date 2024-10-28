from django.shortcuts import render, redirect
from .forms import ProductsForm
from .models import Products

def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o produto no banco de dados
            return redirect('loujinha:success')  # Redireciona para a página de sucesso
    else:
        form = ProductsForm()
    
    return render(request, 'loujinha/add_product.html', {'form': form})

def success(request):
    return render(request, 'loujinha/success.html')
