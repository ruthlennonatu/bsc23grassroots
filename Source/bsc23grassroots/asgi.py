"""
ASGI config for bsc23grassroots project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
"""
Django ASGI Application Configuration

This module configures the Django ASGI (Asynchronous Server Gateway Interface) application for the 'bsc23grassroots' project. It sets the default Django settings module and initializes the ASGI application using the `get_asgi_application` function from `django.core.asgi`.

Usage:
- Import this module to configure the ASGI application for the 'bsc23grassroots' project.
- The 'DJANGO_SETTINGS_MODULE' environment variable is set to 'bsc23grassroots.settings'.

Example:
    import os
    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsc23grassroots.settings')

    application = get_asgi_application()
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsc23grassroots.settings')

application = get_asgi_application()

