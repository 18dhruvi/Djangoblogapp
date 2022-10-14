
import os
from celery import Celery
# from django_celery_beat.models import PeriodicTask, IntervalSchedule


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
app = Celery("blog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


