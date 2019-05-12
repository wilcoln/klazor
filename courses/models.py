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

    class Meta:
        db_table = 'category'


class Instructor(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instructor'


class Resource(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'resource'


class Course(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    instructors = models.ManyToManyField(Instructor, through='ACourseInstructor')
    resources = models.ManyToManyField(Resource, through='ACourseResource')
    categories = models.ManyToManyField(Category, through='ACategoryCourse')

    class Meta:
        db_table = 'course'


class Item(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    id_next = models.IntegerField(blank=True, null=True)
    id_prev = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'item'


class MoocCourse(models.Model):
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')

    class Meta:
        db_table = 'mooc_course'


class NonSchool(models.Model):
    id_instructor = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='id_instructor')

    class Meta:
        db_table = 'non_school'


class Note(models.Model):
    content = models.TextField(blank=True, null=True)
    id_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='id_item')

    class Meta:
        db_table = 'note'


class School(models.Model):
    admissions_link = models.TextField(blank=True, null=True)
    programs_link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'school'


class SchoolCourse(models.Model):
    year = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')
    items = models.ManyToManyField(Item, through='ASchoolCourseItem')

    class Meta:
        db_table = 'school_course'


class Week(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    id_mooc_course = models.ForeignKey(MoocCourse, models.DO_NOTHING, db_column='id_mooc_course')
    items = models.ManyToManyField(Item, through='AWeekItem')

    class Meta:
        db_table = 'week'


class ACategoryCourse(models.Model):
    id_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='id_category', primary_key=True)
    id_course = models.ForeignKey('Course', models.DO_NOTHING, db_column='id_course')

    class Meta:
        db_table = 'a_category_course'
        unique_together = (('id_category', 'id_course'),)


class ACourseInstructor(models.Model):
    id_course = models.ForeignKey('Course', models.DO_NOTHING, db_column='id_course', primary_key=True)
    id_instructor = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='id_instructor')

    class Meta:
        db_table = 'a_course_instructor'
        unique_together = (('id_course', 'id_instructor'),)


class ACourseResource(models.Model):
    id_resource = models.ForeignKey('Resource', models.DO_NOTHING, db_column='id_resource', primary_key=True)
    id_course = models.ForeignKey('Course', models.DO_NOTHING, db_column='id_Course')

    class Meta:
        db_table = 'a_course_resource'
        unique_together = (('id_resource', 'id_course'),)


class ASchoolCourseItem(models.Model):
    id_school_course = models.ForeignKey('SchoolCourse', models.DO_NOTHING, db_column='id_school_course', primary_key=True)
    id_item = models.ForeignKey('Item', models.DO_NOTHING, db_column='id_item')

    class Meta:
        db_table = 'a_school_course_item'
        unique_together = (('id_school_course', 'id_item'),)


class AWeekItem(models.Model):
    id_week = models.ForeignKey('Week', models.DO_NOTHING, db_column='id_week', primary_key=True)
    id_item = models.ForeignKey('Item', models.DO_NOTHING, db_column='id_item')

    class Meta:
        db_table = 'a_week_item'
        unique_together = (('id_week', 'id_item'),)
