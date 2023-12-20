"""
Django Application Configuration

This module defines the configuration for the 'grassroots' Django application.

Application Configuration:
- Extends the base `AppConfig` class from `django.apps`.
- Sets the default auto-generated field to 'django.db.models.BigAutoField'.
- Specifies the name of the application as 'grassroots'.

Usage:
- Include this module in your Django project to configure the 'grassroots' application.
- Use the 'GrassrootsConfig' class as the application configuration in the Django settings.

Example:
    from django.apps import AppConfig

    class GrassrootsConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'grassroots'
"""


from django.apps import AppConfig


class GrassrootsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grassroots'


