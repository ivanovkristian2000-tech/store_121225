from rest_framework import serializers
from store.models import Address, Customer, Order, OrderItem
import re

from store.serializers.product import ProductSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined']


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def validate_phone_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError('Номер телефона должен содержать от 10 до 15 цифр.')
        return value


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate_quantity(self, value):
        if value > 1000:
            raise serializers.ValidationError('Количество товара должно быть не больше тысячи.')
        return value






