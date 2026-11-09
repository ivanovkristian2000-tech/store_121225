"""Экспорт представлений магазина для подключения в config.urls."""
from .category import CategoryViewSet

from .product import (ProductListCreateView
                    , ProductRetrieveUpdateDestroyAPIView
                    , ProductDetailRetrieveUpdateDeleteView
                    , ProductDetailListCreateView
                    , ProductViewSet
                    , ProductRetrieveUpdateDestroyAPIViewSet
                    , ProductListCreateViewSet
                    , ProductDetailListCreateViewSet)

from .address import  AddressViewSet

from .customer import (CustomerListCreateView
                        , CustomerDetailUpdateDeleteView
                        , OrderDetailUpdateDeleteView
                        , OrderListCreateView
                        , OrderItemDetailUpdateDeleteView
                        , OrderItemListCreateView
                        , CustomerViewSet)

