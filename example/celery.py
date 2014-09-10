# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from celery import Celery
#from celery.schedules import crontab

from django.conf import settings


# Working through:
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
app = Celery('example')

# Config in one of three ways:
# 1) settings on the app
# app.conf.BROKER_URL = 'redis://localhost:6379/0'
# app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# 2) dedicated config module ('project/celeryconfig.py')
# app.config_from_object('project.celeryconfig')
# 3) read from the django settings
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
