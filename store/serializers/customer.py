"""Сериализаторы адресов, клиентов, заказов и позиций с проверкой входных данных."""
from rest_framework import serializers
from store.models import Address, Customer, Order, OrderItem
import re

from store.serializers.product import ProductSerializer


class AddressSerializer(serializers.ModelSerializer):
    """Преобразует данные адреса для API.

    Поля соответствуют модели, указанной в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора AddressSerializer, включая ограничения записи, если заданы."""
        model = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    """Преобразует данные клиента для API.

    Поля address содержат вложенные данные и доступны только для чтения.
    """
    address = AddressSerializer(read_only=True)

    class Meta:
        """Модель и набор полей сериализатора CustomerSerializer, включая ограничения записи, если заданы."""
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined']


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    """Проверяет данные для создания и изменения клиента.

    Связанные объекты принимаются по первичным ключам; состав полей задан в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора CustomerCreateUpdateSerializer, включая ограничения записи, если заданы."""
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def validate_phone_number(self, value):
        """Проверяет телефон по шаблону из 10–15 цифр без префикса «+».

        Args:
            value: Проверяемая строка номера телефона.

        Returns:
            Исходная строка, если она соответствует регулярному выражению.

        Raises:
            serializers.ValidationError: Если номер не соответствует шаблону.
        """
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError('Номер телефона должен содержать от 10 до 15 цифр.')
        return value


class OrderSerializer(serializers.ModelSerializer):
    """Преобразует данные заказа для API.

    Поля customer содержат вложенные данные и доступны только для чтения.
    """
    customer = CustomerSerializer(read_only=True)

    class Meta:
        """Модель и набор полей сериализатора OrderSerializer, включая ограничения записи, если заданы."""
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    """Проверяет данные для создания и изменения заказа.

    Связанные объекты принимаются по первичным ключам; состав полей задан в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора OrderCreateUpdateSerializer, включая ограничения записи, если заданы."""
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


class OrderItemSerializer(serializers.ModelSerializer):
    """Преобразует данные позиции заказа для API.

    Поля product, order содержат вложенные данные и доступны только для чтения.
    """
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        """Модель и набор полей сериализатора OrderItemSerializer, включая ограничения записи, если заданы."""
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    """Проверяет данные для создания и изменения позиции заказа.

    Связанные объекты принимаются по первичным ключам; состав полей задан в Meta.
    """
    class Meta:
        """Модель и набор полей сериализатора OrderItemCreateUpdateSerializer, включая ограничения записи, если заданы."""
        model = OrderItem
        fields = '__all__'

    def validate_quantity(self, value):
        """Проверяет, что количество товара не превышает 1000.

        Args:
            value: Количество товара в позиции заказа.

        Returns:
            Переданное количество, если верхний предел не превышен.

        Raises:
            serializers.ValidationError: Если количество больше 1000.
        """
        if value > 1000:
            raise serializers.ValidationError('Количество товара должно быть не больше тысячи.')
        return value






