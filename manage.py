#!/usr/bin/env python
"""Запуск административных команд Django с настройками config.settings."""
import os
import sys


def main():
    """Настраивает Django и выполняет команду из аргументов командной строки.

    Raises:
        ImportError: Если Django недоступен в текущем окружении Python.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
