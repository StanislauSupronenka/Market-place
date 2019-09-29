# Generated by Django 2.2.5 on 2019-09-29 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20190929_1905'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userdeals',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='caritem',
            name='user_deals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='market.UserDeals'),
        ),
    ]