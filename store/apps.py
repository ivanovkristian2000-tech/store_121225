"""Конфигурация приложения store для регистрации в Django."""
from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Регистрирует приложение магазина под именем store."""
    name = 'store'
