"""Маршруты административной панели и API магазина.

Роутер регистрирует наборы представлений; ниже добавлены отдельные API-представления.
При совпадении путей используется первый подходящий маршрут.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store import views


router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'suppliers', views.SupplierViewSet, basename='supplier')
router.register(r'addresses', views.AddressViewSet, basename='address')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'customers', views.CustomerViewSet, basename='customer')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('product-details/', views.ProductDetailListCreateView.as_view(), name='product-details'),
    path('product-details/<int:pk>/'
         , views.ProductDetailRetrieveUpdateDeleteView.as_view()
         , name='product-details-update'),
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailUpdateDeleteView.as_view(), name='customer-detail'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailUpdateDeleteView.as_view(), name='order-detail'),
    path('order-items/', views.OrderItemListCreateView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailUpdateDeleteView.as_view(), name='order-item-detail'),

]