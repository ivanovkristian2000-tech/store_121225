"""API-представления клиентов, заказов и позиций заказа для чтения и изменения данных."""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from store.models import  Customer, Order, OrderItem
from store.serializers.customer import (CustomerSerializer, CustomerCreateUpdateSerializer
                                        , OrderSerializer,OrderCreateUpdateSerializer
                                        , OrderItemCreateUpdateSerializer, OrderItemSerializer)

from store.permission import IsCustomerOrReadOnly, CanViewStatistics


class CustomerViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление клиента через API.

    Поддерживает фильтрацию по имени и фамилии.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ('first_name', 'last_name')

class CustomerListCreateView(ListCreateAPIView):
    """Возвращает список записей клиента по GET и создаёт запись по POST."""
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает CustomerSerializer;
        для остальных методов — CustomerCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class CustomerDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Получает запись клиента по GET, изменяет по PUT/PATCH и удаляет по DELETE."""
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает CustomerSerializer;
        для остальных методов — CustomerCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class OrderListCreateView(ListCreateAPIView):
    """Возвращает список записей заказа по GET и создаёт запись по POST."""
    queryset = Order.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает OrderSerializer;
        для остальных методов — OrderCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Получает запись заказа по GET, изменяет по PUT/PATCH и удаляет по DELETE."""
    queryset = Order.objects.all()
    permission_classes = [IsCustomerOrReadOnly]

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает OrderSerializer;
        для остальных методов — OrderCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderItemListCreateView(ListCreateAPIView):
    """Возвращает список записей позиции заказа по GET и создаёт запись по POST."""
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает OrderItemSerializer;
        для остальных методов — OrderItemCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


class OrderItemDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Получает запись позиции заказа по GET, изменяет по PUT/PATCH и удаляет по DELETE."""
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает OrderItemSerializer;
        для остальных методов — OrderItemCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


class UserOrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


class OrderStatisticsView(APIView):
    permission_classes = [CanViewStatistics]

    def get(self, request, *args, **kwargs):
        total_orders = Order.objects.count()
        data = {
            "total_orders": total_orders,
        }
        return Response(data)
