# Generated by Django 2.2.1 on 2019-06-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0008_auto_20190606_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
