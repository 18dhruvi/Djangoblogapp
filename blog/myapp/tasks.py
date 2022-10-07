from time import sleep
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
# from celery import Celery
import celery

from celery import shared_task

@shared_task()
def send_mail_func(email):
    print("-------******------")
    # users = get_user_model().objects.all()
    if email:
        print("hello ")
        subject = 'Welcome to Blog application '
        print(subject)
        message = f'Hi {email}, Thank you for register.'
        print(message)
        email_from = settings.DEFAULT_FROM_EMAIL
        print(email_from)
        recipient_list = [email]
        send_mail(subject,message,email_from,recipient_list,fail_silently=True,)    

# @shared_task(bind=True)
# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject="Welcome to Blog application"
#         message="Thank you for register!!"
#         to_email=user.email
#         send_mail(
#             subject= mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=True,
#         )
#     return "Done"