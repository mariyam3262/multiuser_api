from celery import shared_task
import datetime
from django.core.mail import send_mail
from account.models import CustomeUser
from django.conf import settings
from casa.celery import app


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print("hello",i)
    return "Done"


@app.task(name="send_notification")
def send_notifications():
    try:
        time_thresold = datetime.datetime.now() + datetime.timedelta(minutes=10)

        profile_objs = CustomeUser.objects.all()
        
        for profile_obj in  profile_objs:
          subject = "Notification you account is not verified"
          message = "You account is not verified"
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [profile_obj.email]
          send_mail(subject , message,email_from, recipient_list)

          
    except Exception as e:
        print(e) 