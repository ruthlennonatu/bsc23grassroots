"""
WSGI config for bsc23grassroots project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
"""
Django WSGI Application Configuration

This script configures the Django WSGI (Web Server Gateway Interface) application for the 'bsc23grassroots' project.

WSGI Application Initialization:
- Imports the necessary modules for WSGI application setup.
- Sets the 'DJANGO_SETTINGS_MODULE' environment variable to 'bsc23grassroots.settings'.
- Initializes the WSGI application using the `get_wsgi_application` function from `django.core.wsgi`.

Usage:
- Include this script in your project to configure the WSGI application.
- Ensure that the 'DJANGO_SETTINGS_MODULE' points to the correct Django settings module.

Example:
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsc23grassroots.settings')

    application = get_wsgi_application()
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsc23grassroots.settings')

application = get_wsgi_application()
