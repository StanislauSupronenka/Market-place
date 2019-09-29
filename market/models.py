from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum
from users.models import Users


class Status(Enum):
    denied = 'Denied'
    accepted = 'Sccepted'
    saved = 'Saved'

    @classmethod
    def get_choices(cls):
        return [
            (el.value, name)
            for name, el in cls.__members__.items()
        ]


class UserDeals(models.Model):
    date_creating = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        Users,
        null=True,
        related_name='carts',
        on_delete=models.SET_NULL
    )

    @property
    def price(self):
        return self.items.all().values_list('price')



class AbstractDeal(models.Model):
    currency_code = models.CharField(max_length=3)
    currency = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True



class CarItem(AbstractDeal):
    user_deals = models.ForeignKey(
        UserDeals,
        related_name='items',
        on_delete=models.PROTECT
    )





class Deals(models.Model):
    write_of_acc = models.CharField(max_length=30)
    receipt_acc = models.CharField(max_length=30)
    status = models.CharField(
        max_length=10,
        choices=Status.get_choices()
    )