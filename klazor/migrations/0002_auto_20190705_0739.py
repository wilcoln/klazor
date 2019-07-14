# Generated by Django 2.2.2 on 2019-07-05 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepart',
            name='type',
            field=models.CharField(default='Week', max_length=32),
        ),
        migrations.AlterField(
            model_name='coursepart',
            name='parent',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='klazor.CoursePart'),
        ),
        migrations.AlterField(
            model_name='coursepart',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
