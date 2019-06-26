# Generated by Django 2.2.1 on 2019-06-26 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klazor', '0010_auto_20190626_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('fileitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.FileItem')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('nb_pages', models.SmallIntegerField(blank=True, null=True)),
                ('lang_alpha2', models.CharField(blank=True, max_length=2, null=True)),
                ('author_set', models.ManyToManyField(to='libr.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libr.Publisher')),
                ('topic_set', models.ManyToManyField(to='klazor.Topic')),
            ],
            options={
                'db_table': 'book',
            },
            bases=('klazor.fileitem',),
        ),
    ]
