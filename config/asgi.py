"""Точка входа для ASGI-сервера.

Выбирает config.settings и предоставляет объект application для обработки запросов.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
