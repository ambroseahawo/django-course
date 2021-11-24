from django.urls import path
from .views import (
    product_list_view, 
    product_create_view, 
    product_update_view, 
    product_detail_view, 
    product_delete_view
)

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:pk>/', product_detail_view, name='product-detail'),
    path('<int:pk>/edit/', product_update_view, name='product-edit'),
    path('<int:pk>/delete/', product_delete_view, name='product-delete'),
]