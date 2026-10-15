import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import *
from django.db.models import Sum, F, Avg, Min, Max, Count, ExpressionWrapper, DurationField

# avg_price = Product.objects.values('category__name').annotate(avg_price=Avg('price')).order_by('category__name')
#
# for item in avg_price:
#     print(item['category__name'], item['avg_price'])


# min_max_prices = Product.objects.aggregate(min_price=Min('price'), max_price=Max('price'))
#
# print(f'Min: {round(min_max_prices['min_price'], 2)}, Max: {round(min_max_prices['max_price'], 2)}')


# order_by_customer = Order.objects.values(
#     'customer__first_name', 'customer__last_name').annotate(
#     order_count=Count('id'),
#     total_sum=Sum(F('items__price') * F('items__quantity')),
# ).order_by('customer__first_name', 'customer__last_name')
#
# for entry in order_by_customer:
#  print(f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
#        f"Заказов:{entry['order_count']}, Общая сумма: {entry['total_sum']}")


# total_weight = Product.objects.values('category__name').annotate(
#     total_weight=Sum(F('detail__weight') * F('quantity'))
# )
#
# for item in total_weight:
#     print(item['category__name'], item['total_weight'])


# count_prods_by_supplier = Product.objects.values('supplier__name').annotate(
#     count=Count('id'),
# )
#
# for supplier in count_prods_by_supplier:
#     print(supplier['supplier__name'], supplier['count'])


# avg_lifetime = Product.objects.annotate(
#     lifetime=ExpressionWrapper(F('detail__expiration_date') - F('detail__manufacturing_date'), output_field=DurationField())
# ).aggregate(life_avg=Avg('lifetime'))['life_avg']
#
# print(avg_lifetime)


# total_sum = Order.objects.values('customer__first_name', 'customer__last_name').annotate(
#     total=Sum(F('items__price') * F('items__quantity')),
# )
#
# for item in total_sum:
#     print(f"{item['customer__first_name']} {item['customer__last_name']} {round(item['total'], 2)}")


# sort = Product.objects.all().order_by('-price')
#
# for item in sort:
#     print(item.name, item.price)


# total_sum = Order.objects.annotate(
#     total=Sum(F('items__price') * F('items__quantity'))).order_by('-total')

# print(type(total_sum))
# for order in total_sum:
#     print(f"Заказ {order.id}, Общая стоимость: {order.total}")


# sorted_address = Address.objects.all().order_by('country', 'city')
#
# for address in sorted_address:
#     print(address.country, "  ", address.city)


orders_sorted = Order.objects.annotate(
    count_items=Count('items')
).order_by('count_items')
for order in orders_sorted:
    print(order, order.count_items)













