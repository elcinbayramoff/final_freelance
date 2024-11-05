from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def notify_inactive_users():
    threshold_date = timezone.now() - timedelta(days=2)
    inactive_users = User.objects.filter(last_login__lt=threshold_date, is_active=True)
    for user in inactive_users:
        send_mail(
            "We Miss You!",
            f"Hello {user.username},\n\nIt looks like you haven't logged in for a while. We miss you!",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
