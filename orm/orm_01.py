import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import *
from django.db.models import Sum, F


total_value = Product.objects.aggregate(
    total_value=Sum(F('price') * F('quantity'))
)['total_value']
print(round(total_value, 2))

