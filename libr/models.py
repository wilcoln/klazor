from django.db import models
from klazor.models import Item
# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'


class Author(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Book(Item):
    url = models.URLField(blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    author_set = models.ManyToManyField(Author)
    nb_pages = models.SmallIntegerField(blank=True, null=True)
    lang_alpha2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'book'



