# Generated by Django 2.2.1 on 2019-05-14 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('categories', models.ManyToManyField(blank=True, to='klazor.Category')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instructor',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'audio',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Note')),
                ('type', models.CharField(choices=[('CM', 'Cours magistral'), ('MC', 'Element Mooc'), ('TD', 'Travaux dirigés'), ('TP', 'Travaux pratiques')], default='CM', max_length=2)),
                ('status', models.CharField(choices=[('UNSTARTED', 'Not started'), ('RUNNING', 'On going'), ('COMPLETED', 'Completed')], default='UNSTARTED', max_length=9)),
                ('next', models.IntegerField(blank=True, null=True)),
                ('prev', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'item',
            },
            bases=('klazor.note',),
        ),
        migrations.CreateModel(
            name='Markdown',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'markdown',
            },
            bases=('klazor.content',),
        ),
        migrations.CreateModel(
            name='MoocCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Course')),
            ],
            options={
                'db_table': 'mooc_course',
            },
            bases=('klazor.course',),
        ),
        migrations.CreateModel(
            name='NotSchool',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Instructor')),
            ],
            options={
                'db_table': 'not_school',
            },
            bases=('klazor.instructor',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Instructor')),
                ('admissions_link', models.TextField(blank=True, null=True)),
                ('programs_link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school',
            },
            bases=('klazor.instructor',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Content')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'video',
            },
            bases=('klazor.content',),
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='klazor.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='resources',
            field=models.ManyToManyField(blank=True, to='klazor.Resource'),
        ),
        migrations.AddField(
            model_name='content',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='klazor.Note'),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('items', models.ManyToManyField(to='klazor.Item')),
                ('mooc_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='klazor.MoocCourse')),
            ],
            options={
                'db_table': 'week',
            },
        ),
        migrations.CreateModel(
            name='SchoolCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Course')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.SmallIntegerField(blank=True, null=True)),
                ('items', models.ManyToManyField(to='klazor.Item')),
            ],
            options={
                'db_table': 'school_course',
            },
            bases=('klazor.course',),
        ),
    ]
