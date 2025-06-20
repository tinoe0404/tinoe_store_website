from django.urls import path

from . import views

urlpatterns = [

	path('', views.tinoe_store, name="tinoe_store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    

]