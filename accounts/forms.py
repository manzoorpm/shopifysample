from django.forms import ModelForm
from .models import Order, Warehouse


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class WarehouseForm(ModelForm):
	class Meta:
		model = Warehouse
		fields = '__all__'

class ProductsForm(ModelForm):
	class Meta:
		model = Warehouse
		fields = '__all__'