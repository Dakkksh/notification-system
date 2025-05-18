from celery import Celery
from .email_service import send_email
from .sms_service import send_sms

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def send_email_task(email, subject, message):
    send_email(email, subject, message)

@celery.task
def send_sms_task(phone, message):
    send_sms(phone, message)
