# Generated by Django 2.2.1 on 2019-05-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0002_auto_20190523_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='item',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
