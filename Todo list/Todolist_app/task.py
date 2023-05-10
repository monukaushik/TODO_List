# tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email():
    send_mail(
        'Notification Related to Your Workout ', 
        'Your workout time is finished', 
        'monu.k@devtrust.biz', 
        ['monukaushik51@gmail.com'], 
        fail_silently=False,
    )
