# Generated by Django 2.2.2 on 2019-07-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0002_auto_20190705_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursepart',
            name='parent',
        ),
        migrations.AddField(
            model_name='coursepart',
            name='level',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursepart',
            name='sequence',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]