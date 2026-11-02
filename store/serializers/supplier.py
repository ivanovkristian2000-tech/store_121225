"""Сериализатор контактных данных поставщиков магазина."""
from rest_framework import serializers
from store.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Преобразует данные поставщика для API.

    Поля соответствуют модели, указанной в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора SupplierSerializer, включая ограничения записи, если заданы."""
        model = Supplier
        fields = '__all__'