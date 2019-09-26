from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum


class Status(Enum):
    denied = 'denied'
    accepted = 'accepted'

    @classmethod
    def get_choices(cls):
        return [
            (el.value, name)
            for name, el in cls.__members__.items()
        ]

class Deals(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=3)
    currency = models.DecimalField(max_digits=10, decimal_places=4)
    write_of_acc = models.CharField(max_length=30)
    receipt_acc = models.CharField(max_length=30)
    status = models.CharField(
        max_length=10,
        choices=Status.get_choices()
    )
# Create your models here.
    class Meta:
        pass

    def create(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.user