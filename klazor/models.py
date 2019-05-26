# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'


class Instructor(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'instructor'


class Resource(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'resource'


class FileResource(Resource):
    file = models.FileField(upload_to='resources/files', )

    class Meta:
        db_table = 'file_resource'


class LinkResource(Resource):
    link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'link_resource'


class Course(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    category_set = models.ManyToManyField(Category, blank=True)
    instructor_set = models.ManyToManyField(Instructor, blank=True)
    resource_set = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course'


class Sheet(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sheet'


class Item(Sheet):
    completed = models.BooleanField(default=False)
    sequence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item'
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
    item_set = models.ManyToManyField(Item)

    class Meta:
        db_table = 'school_course'


class Week(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    mooc_course = models.ForeignKey(MoocCourse, models.DO_NOTHING)
    item_set = models.ManyToManyField(Item)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'week'


class Content(models.Model):
    sequence = models.IntegerField(blank=False, null=False)
    sheet = models.ForeignKey(Sheet, models.CASCADE)

    class Meta:
        db_table = 'content'
        ordering = ['sequence', ]


class MarkdownContent(Content):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.text[:75] + '...') if len(self.text) > 75 else self.text

    class Meta:
        db_table = 'markdown_content'


class VideoContent(Content):
    title = models.CharField(max_length=50, blank=True, null=True)
    video = models.FileField(upload_to='videos')
    display_width = models.FloatField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video_content'


class AudioContent(Content):
    title = models.CharField(max_length=50, blank=True, null=True)
    audio = models.FileField(upload_to='audios')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'audio_content'


class ImageContent(Content):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.FileField(upload_to='images')
    display_width = models.FloatField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'image_content'


class Folder(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sheet_set = models.ManyToManyField(Sheet, blank=True)
    parent = models.ForeignKey('Folder', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'folder'