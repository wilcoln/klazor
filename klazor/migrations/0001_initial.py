# Generated by Django 2.2.2 on 2019-07-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_klazor.cell_set+', to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'cell',
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='klazor.Folder')),
            ],
            options={
                'db_table': 'folder',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
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
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='klazor.Folder')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_klazor.item_set+', to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='AudioCell',
            fields=[
                ('cell_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Cell')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('audio', models.FileField(upload_to='audios')),
            ],
            options={
                'db_table': 'audio_cell',
            },
            bases=('klazor.cell',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Item')),
                ('instructor_set', models.ManyToManyField(blank=True, to='klazor.Instructor')),
            ],
            options={
                'db_table': 'course',
            },
            bases=('klazor.item',),
        ),
        migrations.CreateModel(
            name='FileItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Item')),
                ('file', models.FileField(upload_to='files')),
            ],
            options={
                'db_table': 'file',
            },
            bases=('klazor.item',),
        ),
        migrations.CreateModel(
            name='ImageCell',
            fields=[
                ('cell_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Cell')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.FileField(upload_to='images')),
                ('scale', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'image_cell',
            },
            bases=('klazor.cell',),
        ),
        migrations.CreateModel(
            name='MarkdownCell',
            fields=[
                ('cell_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Cell')),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'markdown_cell',
            },
            bases=('klazor.cell',),
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
            name='Sheet',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Item')),
            ],
            options={
                'db_table': 'sheet',
            },
            bases=('klazor.item',),
        ),
        migrations.CreateModel(
            name='VideoCell',
            fields=[
                ('cell_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Cell')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('video', models.FileField(upload_to='videos')),
                ('scale', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'video_cell',
            },
            bases=('klazor.cell',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('subtopics', models.ManyToManyField(blank=True, to='klazor.Topic')),
            ],
            options={
                'db_table': 'topic',
            },
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
            name='SchoolCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Course')),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_course',
            },
            bases=('klazor.course',),
        ),
        migrations.CreateModel(
            name='CoursePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='klazor.CoursePart')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='klazor.Course')),
            ],
            options={
                'db_table': 'course_part',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='resource_set',
            field=models.ManyToManyField(blank=True, to='klazor.FileItem'),
        ),
        migrations.AddField(
            model_name='course',
            name='topic_set',
            field=models.ManyToManyField(blank=True, to='klazor.Topic'),
        ),
        migrations.AddField(
            model_name='cell',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klazor.Sheet'),
        ),
        migrations.CreateModel(
            name='CourseElement',
            fields=[
                ('sheet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='klazor.Sheet')),
                ('completed', models.BooleanField(default=False)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('course_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klazor.CoursePart')),
            ],
            options={
                'db_table': 'course_element',
                'ordering': ['sequence'],
            },
            bases=('klazor.sheet',),
        ),
    ]
