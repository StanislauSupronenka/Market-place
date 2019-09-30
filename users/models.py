from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.signing import Signer



class Users(AbstractUser):
    signer = Signer()

    phone_number = models.CharField(max_length=20)
    email_verification_link = models.CharField(
        null=True,
        max_length=1024
    )
    is_email_verified = models.BooleanField(default=False)
    verification_email_sent_at = models.DateTimeField(null=True)
    incorrect_attempts = models.PositiveSmallIntegerField(default=0)
    initial_secret_key = models.CharField(max_length=256)