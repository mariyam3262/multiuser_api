from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'casa.settings')
app = Celery('casa',)
app.conf.enable_utc = False

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.conf.update(timezone = 'Asia/KolKata')
app.config_from_object(settings, namespace='')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-2-hour' : {
        'task' : 'send_notification',
        'schedule' : crontab(minute ='*/1' )
    }
}



# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))