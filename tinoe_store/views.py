from django.shortcuts import render

def tinoe_store(request):
	context = {}
	return render(request, 'tinoe_store/tinoe_store.html', context)

def cart(request):
	context = {}
	return render(request, 'tinoe_store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'tinoe_store/checkout.html', context)