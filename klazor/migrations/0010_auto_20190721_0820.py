# Generated by Django 2.2.3 on 2019-07-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0009_auto_20190721_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='view_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='view_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
