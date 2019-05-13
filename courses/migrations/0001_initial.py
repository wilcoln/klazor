# Generated by Django 2.2.1 on 2019-05-13 05:06

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('categories', models.ManyToManyField(to='courses.Category')),
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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=2, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('UNSTARTED', 'Not started'), ('RUNNING', 'On going'), ('COMPLETED', 'Completed')], default='UNSTARTED', max_length=9)),
                ('next', models.IntegerField(blank=True, null=True)),
                ('prev', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'item',
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
            name='MoocCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Course')),
            ],
            options={
                'db_table': 'mooc_course',
            },
            bases=('courses.course',),
        ),
        migrations.CreateModel(
            name='NotSchool',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Instructor')),
            ],
            options={
                'db_table': 'not_school',
            },
            bases=('courses.instructor',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('instructor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Instructor')),
                ('admissions_link', models.TextField(blank=True, null=True)),
                ('programs_link', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school',
            },
            bases=('courses.instructor',),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Item')),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='courses.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='resources',
            field=models.ManyToManyField(to='courses.Resource'),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('items', models.ManyToManyField(to='courses.Item')),
                ('mooc_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.MoocCourse')),
            ],
            options={
                'db_table': 'week',
            },
        ),
        migrations.CreateModel(
            name='SchoolCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Course')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.SmallIntegerField(blank=True, null=True)),
                ('items', models.ManyToManyField(to='courses.Item')),
            ],
            options={
                'db_table': 'school_course',
            },
            bases=('courses.course',),
        ),
    ]
