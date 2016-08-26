from datetime import datetime
from django.core.mail import send_mail

from celery.task.base import periodic_task
from celery.schedules import crontab

from authentication.models import User


@periodic_task(run_every=(crontab(minute='*/60')), name="send_email", ignore_result=True)
def send_email():
    """
    To run locally:
       1. celery -A taskmanager worker -l info
       2. celery -A taskmanager beat -l info
    """
    today = datetime.now().date()
    users = User.objects.all()
    for user in users:
        email = user.email
        tasks = user.task_set.filter(due_date=today)
        message = ['{0} - {1}'.format(task.title, task.due_date) for task in tasks]
        if tasks:
            send_mail(
                'The tasks which you should finish today',
                ''.join(message),
                'from@example.com',
                [email],
                fail_silently=False,
            )

