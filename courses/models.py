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


class Course(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    resources = models.ManyToManyField(Resource, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course'


class Item(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    # Choices for type
    CM = 'CM'
    MC = 'MC'
    TD = 'TD'
    TP = 'TP'
    TYPE_CHOICES = (
        (CM, 'Cours magistral'),
        (MC, 'Element Mooc'),
        (TD, 'Travaux dirigés'),
        (TP, 'Travaux pratiques')
    )

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CM)
    content = models.TextField(blank=True, null=True)

    # Choices for status
    UNSTARTED = 'UNSTARTED'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = (
        (UNSTARTED, 'Not started'),
        (RUNNING, 'On going'),
        (COMPLETED, 'Completed'),
    )
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=UNSTARTED)
    next = models.IntegerField(blank=True, null=True)
    prev = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item'


class MoocCourse(Course):

    class Meta:
        db_table = 'mooc_course'


class NotSchool(Instructor):

    class Meta:
        db_table = 'not_school'


class Note(models.Model):
    content = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'note'


class School(Instructor):
    admissions_link = models.TextField(blank=True, null=True)
    programs_link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'school'


class SchoolCourse(Course):
    year = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    items = models.ManyToManyField(Item)

    class Meta:
        db_table = 'school_course'


class Week(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    mooc_course = models.ForeignKey(MoocCourse, models.DO_NOTHING)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'week'
