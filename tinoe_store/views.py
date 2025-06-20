from django.shortcuts import render
from .models import *

def tinoe_store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'tinoe_store/tinoe_store.html', context)

def cart(request):
    context = {}
    return render(request, 'tinoe_store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'tinoe_store/checkout.html', context)
