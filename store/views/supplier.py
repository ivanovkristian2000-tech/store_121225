"""Набор API-действий для работы с поставщиками."""
from typing import ReadOnly

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS

from store.models import Supplier
from store.serializers.product import SupplierSerializer
from store.permission import ReadOnly



class SupplierViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление поставщика через API."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser | ReadOnly]
