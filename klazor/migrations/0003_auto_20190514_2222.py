# Generated by Django 2.2.1 on 2019-05-14 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klazor', '0002_auto_20190514_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Resource')),
                ('file', models.FileField(upload_to='resources/files')),
            ],
            options={
                'db_table': 'file_resource',
            },
            bases=('klazor.resource',),
        ),
        migrations.RenameField(
            model_name='imagecontent',
            old_name='video',
            new_name='image',
        ),
        migrations.DeleteModel(
            name='DocumentResource',
        ),
    ]
