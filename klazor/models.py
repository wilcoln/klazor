# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    subtopics = models.ManyToManyField('Topic', blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'topic'


class Instructor(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'instructor'


class Item(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    folder = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item'


class FileItem(Item):
    file = models.FileField(upload_to='files')

    class Meta:
        db_table = 'file'


class Course(Item):
    topic_set = models.ManyToManyField(Topic, blank=True)
    instructor_set = models.ManyToManyField(Instructor, blank=True)
    resource_set = models.ManyToManyField(FileItem, blank=True)

    class Meta:
        db_table = 'course'


class Sheet(Item):
    class Meta:
        db_table = 'sheet'


class CourseItem(Sheet):
    completed = models.BooleanField(default=False)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'course_item'
        ordering = ['sequence', ]


class MoocCourse(Course):
    class Meta:
        db_table = 'mooc_course'


class NotSchool(Instructor):
    class Meta:
        db_table = 'not_school'


class School(Instructor):
    admissions_link = models.TextField(blank=True, null=True)
    programs_link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'school'


class SchoolCourse(Course):
    year = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    item_set = models.ManyToManyField(CourseItem)

    class Meta:
        db_table = 'school_course'


class Week(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    mooc_course = models.ForeignKey(MoocCourse, models.DO_NOTHING)
    item_set = models.ManyToManyField(CourseItem)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'week'


class Cell(models.Model):
    sequence = models.IntegerField(blank=False, null=False)
    sheet = models.ForeignKey(Sheet, models.CASCADE)

    class Meta:
        db_table = 'cell'
        ordering = ['sequence', ]


class MarkdownCell(Cell):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.text[:75] + '...') if len(self.text) > 75 else self.text

    class Meta:
        db_table = 'markdown_cell'


class VideoCell(Cell):
    title = models.CharField(max_length=50, blank=True, null=True)
    video = models.FileField(upload_to='videos')
    scale = models.FloatField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video_cell'


class AudioCell(Cell):
    title = models.CharField(max_length=50, blank=True, null=True)
    audio = models.FileField(upload_to='audios')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'audio_cell'


class ImageCell(Cell):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.FileField(upload_to='images')
    scale = models.FloatField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'image_cell'


class Folder(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    parent = models.ForeignKey('Folder', models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'folder'