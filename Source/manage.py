#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    """
        Main Function for Administrative Tasks

        This 'main' function is responsible for running administrative tasks in a Django project.

        Function:
        - 'main()': Run administrative tasks for a Django project.
          - Sets the Django settings module.
          - Attempts to import and execute the Django management command line.

        Usage:
        - Call this function to perform administrative tasks such as database migrations, creating a superuser, and other Django management commands.

        Example:
            if __name__ == "__main__":
                main()
        """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsc23grassroots.settings')
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
