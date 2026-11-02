"""Сериализаторы категорий, товаров и их характеристик для чтения и записи."""
from rest_framework import serializers
from store.models import Product, ProductDetail, Category
from store.serializers.supplier import SupplierSerializer


class CategorySerializer(serializers.ModelSerializer):
    """Преобразует данные категории товаров для API.

    Поля соответствуют модели, указанной в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора CategorySerializer, включая ограничения записи, если заданы."""
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Преобразует данные товара для API.

    Поля category, supplier содержат вложенные данные и доступны только для чтения.
    """
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        """Модель и набор полей сериализатора ProductSerializer, включая ограничения записи, если заданы."""
        model = Product
        fields = '__all__'


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """Проверяет данные для создания и изменения товара.

    Связанные объекты принимаются по первичным ключам; состав полей задан в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора ProductCreateUpdateSerializer, включая ограничения записи, если заданы."""
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    """Преобразует данные характеристик товара для API.

    Поля product содержат вложенные данные и доступны только для чтения.
    """
    product = ProductSerializer(read_only=True)

    class Meta:
        """Модель и набор полей сериализатора ProductDetailSerializer, включая ограничения записи, если заданы."""
        model = ProductDetail
        fields = '__all__'


class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    """Проверяет данные для создания и изменения характеристик товара.

    Связанные объекты принимаются по первичным ключам; состав полей задан в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора ProductDetailCreateUpdateSerializer, включая ограничения записи, если заданы."""
        model = ProductDetail
        fields = '__all__'





