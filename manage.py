#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SAE201Project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible de charger Django. Est-ce que l'environnement virtuel est bien activé ?\n"
            "Allez voir le README.md pour plus d'informations."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
