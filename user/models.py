from django.contrib.auth.models import AbstractUser
from django.db import models
import random
from django.core.mail import send_mail
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_verified = models.BooleanField(default=False)

    def send_otp_email(self, otp_code):
        subject = "Your OTP Code"
        message = f"Hello {self.username},\n\nYour OTP code is {otp_code}. Please enter this code to complete your registration."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otp')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()
