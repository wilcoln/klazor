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


class Tag(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Content(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Item(PolymorphicModel, Content):
    non_polymorphic = models.Manager()
    tag_set = models.ManyToManyField(Tag, blank=True)
    folder = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE)

    def type(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
        ordering = [
            'id',
        ]
        base_manager_name = 'non_polymorphic'


class FileItem(Item):
    file = models.FileField(upload_to='files', null=True)

    class Meta:
        db_table = 'file'


class Folder(Content):
    parent = models.ForeignKey('Folder', models.CASCADE, null=True, blank=True, related_name='sub_folder_set')

    def __str__(self):
        return self.name

    def siblings(self):
        result = []
        if self.parent:
            result = [
                folder for folder in self.parent.sub_folder_set.filter(owner=self.owner)
                if folder.id != self.id and folder.id != 1
            ]
        return result

    def ascendants(self):
        result = []
        folder = self
        while folder.id != 1:
            result.append(folder.parent)
            folder = folder.parent

        result.reverse()
        return result

    class Meta:
        db_table = 'folder'
        ordering = [
            'id',
        ]


class Sheet(Item):
    class Meta:
        db_table = 'sheet'


class Cell(PolymorphicModel):
    # non_polymorphic = models.Manager()
    sequence = models.IntegerField(blank=False, null=False)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)

    def type(self):
        return self.__class__.__name__[:-4]

    class Meta:
        db_table = 'cell'
        ordering = [
            'sequence',
        ]
        # base_manager_name = 'non_polymorphic'


class MediaCell(Cell):
    title = models.CharField(max_length=64, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

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

    class Meta:
        db_table = 'video_cell'


class YoutubeCell(GraphicMediaCell):

    class Meta:
        db_table = 'youtube_cell'


class AudioCell(MediaCell):

    class Meta:
        db_table = 'audio_cell'


class FileCell(MediaCell):

    class Meta:
        db_table = 'file_cell'


class ImageCell(GraphicMediaCell):

    class Meta:
        db_table = 'image_cell'


class MultipleChoiceInputCell(Cell):

    class Meta:
        db_table = 'multiple_choice_input_cell'


class NumericalInputCell(Cell):
    answer = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'numerical_input_cell'


class OpenEndedInputCell(Cell):
    answer = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'open_ended_input_cell'


class Proposition(models.Model):
    input_cell = models.ForeignKey(MultipleChoiceInputCell, on_delete=models.CASCADE)
    statement = models.TextField(blank=True, null=True)
    is_true = models.BooleanField(default=False)

    class Meta:
        db_table = 'proposition'
