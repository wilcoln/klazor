# Generated by Django 2.2.1 on 2019-06-06 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0005_auto_20190606_0314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]