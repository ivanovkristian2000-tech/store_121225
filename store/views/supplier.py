"""Набор API-действий для работы с поставщиками."""
from rest_framework import viewsets
from store.models import Supplier
from store.serializers.product import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление поставщика через API."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
