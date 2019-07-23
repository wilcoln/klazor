# Generated by Django 2.2.3 on 2019-07-21 07:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0004_auto_20190719_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2019, 7, 21, 7, 33, 0, 450914, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]