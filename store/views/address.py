"""Набор API-действий для работы с адресами клиентов."""
from rest_framework import viewsets
from store.models import Address
from store.serializers.customer import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление адреса через API."""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
