# Generated by Django 2.2.1 on 2019-05-21 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='position',
        ),
    ]
