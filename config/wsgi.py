"""Точка входа для WSGI-сервера.

Выбирает config.settings и предоставляет объект application для обработки запросов.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
