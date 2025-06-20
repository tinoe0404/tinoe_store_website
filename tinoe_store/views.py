from django.shortcuts import render
from .models import * 

def tinoe_store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'tinoe_store/tinoe_store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []

	context = {'items':items, 'order':order}
	return render(request, 'tinoe_store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'tinoe_store/checkout.html', context)