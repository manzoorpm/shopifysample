from http.server import ThreadingHTTPServer
from itertools import product
from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm, ProductForm, WarehouseForm


def home(request):
	orders = Order.objects.all()
	warehouse = Warehouse.objects.all()
	total_warehouse = warehouse.count()
	context = {'orders':orders, 'warehouse':warehouse }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()


	return render(request, 'accounts/products.html', {'products':products})

def warehouseList(request):
	warehouse = Warehouse.objects.all()


	return render(request, 'accounts/warehouse_list.html', {'warehouse':warehouse})

def warehouse(request, pk_test):
	warehouse = Warehouse.objects.get(id=pk_test)

	orders = warehouse.order_set.all()
	order_count = orders.count()

	context = {'warehouse':warehouse, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/warehouse.html',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

def createWarehouse(request):
	form = WarehouseForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = WarehouseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_warehouse.html', context)

def updateWarehouse(request, pk):

	warehouse = Warehouse.objects.get(id=pk)
	form = WarehouseForm(instance=warehouse)

	if request.method == 'POST':
		form = WarehouseForm(request.POST, instance=warehouse)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_warehouse.html', context)

def deleteWarehouse(request, pk):
	warehouse = Warehouse.objects.get(id=pk)
	if request.method == "POST":
		warehouse.delete()
		return redirect('/')

	context = {'item':warehouse}
	return render(request, 'accounts/delete_warehouse.html', context)

def createProduct(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/products')

	context = {'form':form}
	return render(request, 'accounts/add_product.html', context)

def updateProduct(request, pk):

	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/products')

	context = {'form':form}
	return render(request, 'accounts/add_product.html', context)

def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/products')

	context = {'item':product}
	return render(request, 'accounts/delete_product.html', context)