# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


class Topic(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    subtopic_set = models.ManyToManyField('Topic', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'topic'


class Instructor(PolymorphicModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'instructor'


class Content(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    # remove null=True for these three
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    view_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Item(PolymorphicModel, Content):
    title = models.CharField(max_length=128, blank=True, null=True)
    folder = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item'
        ordering = ['id', ]


class FileItem(Item):
    file = models.FileField(upload_to='files', null=True)

    class Meta:
        db_table = 'file'


class Course(Item):
    topic_set = models.ManyToManyField(Topic, blank=True)
    instructor_set = models.ManyToManyField(Instructor, blank=True)
    resource_set = models.ManyToManyField(FileItem, blank=True)
    year = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'course'


class Sheet(Item):
    class Meta:
        db_table = 'sheet'


class CourseElement(Sheet):
    # completed = models.BooleanField(default=False)
    sequence = models.IntegerField(blank=True, null=True)
    course_part = models.ForeignKey('CoursePart', on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_element'
        ordering = ['sequence', ]


class School(Instructor):
    colloquial_name = models.CharField(max_length=8, blank=True, null=True)
    # admissions_link = models.TextField(blank=True, null=True)
    # programs_link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'school'


class CoursePart(models.Model):
    label = models.CharField(max_length=32, default='Week')
    title = models.CharField(max_length=64, blank=True, null=True)
    course = models.ForeignKey(Course, models.CASCADE)
    level = models.SmallIntegerField(default=1)
    sequence = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course_part'
        ordering = ['id', ]


class Cell(PolymorphicModel):
    sequence = models.IntegerField(blank=False, null=False)
    sheet = models.ForeignKey(Sheet, models.CASCADE)

    class Meta:
        db_table = 'cell'
        ordering = ['sequence', ]


class MediaCell(Cell):
    title = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class GraphicMediaCell(MediaCell):
    scale = models.FloatField(default=1)

    class Meta:
        abstract = True


class MarkdownCell(Cell):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.text[:75] + '...') if len(self.text) > 75 else self.text

    class Meta:
        db_table = 'markdown_cell'


class VideoCell(GraphicMediaCell):
    video = models.FileField(upload_to='videos')

    class Meta:
        db_table = 'video_cell'


class YoutubeCell(GraphicMediaCell):
    youtube = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'youtube_cell'


class AudioCell(MediaCell):
    audio = models.FileField(upload_to='audios')

    class Meta:
        db_table = 'audio_cell'


class ImageCell(GraphicMediaCell):
    image = models.FileField(upload_to='images')

    class Meta:
        db_table = 'image_cell'


class Folder(Content):
    name = models.CharField(max_length=128, blank=True, null=True)
    parent = models.ForeignKey('Folder', models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def siblings(self):
        return [folder for folder in self.parent.folder_set.filter(user=self.user) if folder.id != self.id and folder.id != 1]

    class Meta:
        db_table = 'folder'
        ordering = ['id', ]
