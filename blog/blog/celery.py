
import os
from celery import Celery
# from django_celery_beat.models import PeriodicTask, IntervalSchedule


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
app = Celery("blog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'send_mail_func' : {
#         'task' : 'send_mail.tasks.send_mail_func',
#         'schedule' : 30.0
#     }
    
# }


# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=10,
#     period=IntervalSchedule.SECONDS,
# )