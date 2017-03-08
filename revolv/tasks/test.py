from django.conf import settings
from django.db.models import Sum
from celery.task import task
from revolv.lib.mailer import send_revolv_email


@task
def test_mail():
    context= {}
    send_revolv_email(
        'Test',
        context, ['harshad.devale@tudip.nl']
    )
