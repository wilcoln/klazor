# Generated by Django 2.2.4 on 2019-09-29 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='libr.Document')),
                ('nb_pages', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'document_file',
            },
            bases=('libr.document',),
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='narrator_set',
            field=models.ManyToManyField(blank=True, to='libr.Author'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='nb_pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]