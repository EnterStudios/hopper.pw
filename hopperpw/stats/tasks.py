# coding=utf-8
from datetime import datetime
import logging
import pytz

from django.contrib.auth import get_user_model

from main.models import Host
from stats.models import StatisticsEntry
from hopperpw.celery import app


@app.task()
def save_user_count():
    try:
        last_count = StatisticsEntry.objects\
            .filter(stat_type='user_count')\
            .order_by('-created')[0].value
    except Exception as e:
        last_count = 0
        logging.warn('Dropped exception {0} in task save_user_count'.format(e))
    count = get_user_model().objects.all().count()
    if not count == last_count:
        StatisticsEntry.objects.create(stat_type='user_count', value=count)


@app.task
def save_host_count():
    try:
        last_count = StatisticsEntry.objects\
            .filter(stat_type='host_count')\
            .order_by('-created')[0].value
    except Exception as e:
        last_count = 0
        logging.warn('Dropped exception {0} in task save_user_count'.format(e))
    count = Host.objects.all().count()
    if not count == last_count:
        StatisticsEntry.objects.create(stat_type='host_count', value=count)


@app.task
def increment_ip_update_count():
    today = datetime.now(pytz.utc)
    (se, created) = StatisticsEntry.objects.get_or_create(
        stat_type='ip_update_count',
        created__year=today.year,
        created__month=today.month,
        created__day=today.day,
        defaults={'value': 0}
    )
    se.value += 1
    se.save()
