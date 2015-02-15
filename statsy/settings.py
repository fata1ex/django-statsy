# coding: utf-8

from django.conf import settings


CACHE_TIMEOUT = getattr(settings, 'STATSY_CACHE_TIMEOUT', 60)
ASYNC = getattr(settings, 'STATSY_ASYNC', False)

STATS_VIEW_PERMISSION = 'statsy.stats_view'
