from __future__ import unicode_literals, absolute_import
from celery.schedules import crontab
from celery.task import periodic_task
from demo.celery import app
from celery import shared_task
import requests, json

from datetime import datetime, timedelta
from django.db.models import Count, Sum, Max, Avg, Case, When, Value, IntegerField, BooleanField
from django.db.models.functions import ExtractYear, ExtractMonth,ExtractWeek, ExtractWeekDay
from django.db.models.functions import Extract
from django.db import connections



@shared_task
def print_hello():
    return 'umesh'


 # celery -A demo worker -l info -B
