# Generated by Django 2.2.1 on 2019-05-27 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0005_auto_20190526_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecontent',
            old_name='display_width',
            new_name='scale',
        ),
        migrations.RenameField(
            model_name='videocontent',
            old_name='display_width',
            new_name='scale',
        ),
    ]
