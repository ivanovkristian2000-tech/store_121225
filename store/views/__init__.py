"""Экспорт представлений магазина для подключения в config.urls."""
from .category import CategoryViewSet

from .product import (ProductListCreateView
                    , ProductRetrieveUpdateDestroyAPIView
                    , ProductDetailRetrieveUpdateDeleteView
                    , ProductDetailListCreateView
                    , ProductViewSet
                    , ProductRetrieveUpdateDestroyAPIView
                    , ProductListCreateView
                    , ProductDetailListCreateView)

from .address import  AddressViewSet
from .supplier import SupplierViewSet

from .customer import (CustomerListCreateView
                        , CustomerDetailUpdateDeleteView
                        , OrderDetailUpdateDeleteView
                        , OrderListCreateView
                        , OrderItemDetailUpdateDeleteView
                        , OrderItemListCreateView
                        , CustomerViewSet)

