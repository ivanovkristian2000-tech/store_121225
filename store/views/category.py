"""Набор API-действий для работы с категориями товаров."""
from rest_framework import viewsets
from store.models import Category
from store.serializers.product import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление категории товаров через API."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
