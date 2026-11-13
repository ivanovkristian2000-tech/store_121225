"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


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
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('user-orders/', views.UserOrderListView.as_view(), name='user-order'),
    path('orders/', views.OrderListCreateView.as_view(), name='orders'),
    path('order-statistics/', views.OrderStatisticsView.as_view(), name='order-statistics'),
]
