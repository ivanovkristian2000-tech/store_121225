"""API-представления товаров и характеристик с выбором сериализатора по HTTP-методу."""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from store.models import Product, ProductDetail
from store.serializers.product import (ProductSerializer, ProductCreateUpdateSerializer
                                        , ProductDetailSerializer, ProductDetailCreateUpdateSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    """Предоставляет список, получение, создание, изменение и удаление товара через API.

    Поддерживает фильтрацию по категории и цене.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['category', "price"]


class ProductListCreateView(ListCreateAPIView):
    """Возвращает список записей товара по GET и создаёт запись по POST."""
    queryset = Product.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает ProductSerializer;
        для остальных методов — ProductCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Получает запись товара по GET, изменяет по PUT/PATCH и удаляет по DELETE."""
    queryset = Product.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает ProductSerializer;
        для остальных методов — ProductCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class  ProductDetailListCreateView(ListCreateAPIView):
    """Возвращает список записей характеристик товара по GET и создаёт запись по POST."""
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает ProductDetailSerializer;
        для остальных методов — ProductCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductCreateUpdateSerializer


class ProductDetailRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Получает запись характеристик товара по GET, изменяет по PUT/PATCH и удаляет по DELETE."""
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        """Выбирает класс сериализатора по HTTP-методу запроса.

        Для GET возвращает ProductDetailSerializer;
        для остальных методов — ProductDetailCreateUpdateSerializer.
        """
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer



