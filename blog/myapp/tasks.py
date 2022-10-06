from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail


from celery import shared_task

@shared_task(bind=True)
def send_mail_func(email):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=task=-=-=-=-=-=-=-")
    # users = get_user_model().objects.all()
    if email:
        subject = 'Welcome to Blog application '
        message = f'Hi {email}, Thank you for register.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject,
                  message,
                  email_from,
                  recipient_list,
                  fail_silently=True,
                  )    
    return "Done"