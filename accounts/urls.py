from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('warehouse/<str:pk_test>/', views.warehouse, name="warehouse"),
    path('warehouse_list', views.warehouseList, name="warehouse_list"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('create_warehouse/', views.createWarehouse, name="create_warehouse"),
    path('update_warehouse/<str:pk>/', views.updateWarehouse, name="update_warehouse"),
    path('delete_warehouse/<str:pk>/', views.deleteWarehouse, name="delete_warehouse"),

    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),

]