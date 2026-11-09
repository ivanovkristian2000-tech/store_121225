"""Модели базы данных магазина и связи между товарами, клиентами и заказами."""
from django.db import models


class Category(models.Model):
    """Категория с уникальным названием для группировки товаров."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        """Названия и порядок сортировки записей модели Category в Django."""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        """Возвращает название категории для отображения объекта."""
        return self.name


class Supplier(models.Model):
    """Поставщик товаров с названием, контактным email и номером телефона."""
    name = models.CharField(max_length=150, verbose_name='Название')
    contact_email = models.EmailField(verbose_name='Email для связи')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        """Названия и порядок сортировки записей модели Supplier в Django."""
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        """Возвращает название поставщика для отображения объекта."""
        return self.name


class Product(models.Model):
    """Товар с категорией, поставщиком, ценой, остатком и уникальным артикулом."""
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория'
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name='products', verbose_name='Поставщик'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    available = models.BooleanField(default=True, verbose_name='В наличии')

    class Meta:
        """Названия и порядок сортировки записей модели Product в Django."""
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        """Возвращает название товара и его артикул для отображения объекта."""
        return f'{self.name} ({self.article})'


class ProductDetail(models.Model):
    """Дополнительные характеристики одного товара: описание, даты и вес."""
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='detail', verbose_name='Товар'
    )
    description = models.TextField(verbose_name='Описание')
    manufacturing_date = models.DateField(verbose_name='Дата изготовления')
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Срок годности')
    weight = models.DecimalField(max_digits=8, decimal_places=3, verbose_name='Вес, кг')

    class Meta:
        """Названия и порядок сортировки записей модели ProductDetail в Django."""
        verbose_name = 'Характеристики товара'
        verbose_name_plural = 'Характеристики товаров'
        ordering = ['product']

    def __str__(self):
        """Возвращает описание ссылки на товар для отображения объекта."""
        return f'Детали товара: {self.product}'


class Address(models.Model):
    """Почтовый адрес с указанием страны, города, улицы и дома."""
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом')

    class Meta:
        """Названия и порядок сортировки записей модели Address в Django."""
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['country', 'city']

    def __str__(self):
        """Возвращает полный адрес одной строкой для отображения объекта."""
        return f'{self.country}, {self.city}, {self.street} {self.house}'


class Customer(models.Model):
    """Клиент с контактными данными, необязательным адресом и датой регистрации."""
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='customers', verbose_name='Адрес'
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        """Названия и порядок сортировки записей модели Customer в Django."""
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """Возвращает имя и фамилию клиента для отображения объекта."""
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    """Заказ клиента с датой оформления; состав хранится в связанных позициях."""
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент'
    )
    order_date = models.DateTimeField(verbose_name='Дата заказа')

    class Meta:
        """Названия и порядок сортировки записей модели Order в Django."""
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']

    def __str__(self):
        """Возвращает номер заказа и клиента для отображения объекта."""
        return f'Заказ №{self.pk} от {self.customer}'


class OrderItem(models.Model):
    """Позиция заказа: товар, количество и сохранённая цена за единицу."""
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')

    class Meta:
        """Названия и порядок сортировки записей модели OrderItem в Django."""
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        ordering = ['order']

    def __str__(self):
        """Возвращает товар и количество в позиции заказа для отображения объекта."""
        return f'{self.product} x{self.quantity}'