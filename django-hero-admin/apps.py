from django import get_version
from django.apps import AppConfig
from django.contrib.admin.options import ModelAdmin
from . import VERSION

ALL_FIELDS = '__all__'


class DjangoHeroAdminConfig(AppConfig):
    name = 'django-hero-admin'
    verbose_name = 'Django Hero Admin'
    django_version = get_version()
    version = VERSION

    def __init__(self, app_name, app_module):
        super(DjangoHeroAdminConfig, self).__init__(app_name, app_module)

    def ready(self):
        super(DjangoHeroAdminConfig, self).ready()
