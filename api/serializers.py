from rest_framework import serializers
from klazor.models import *


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ('sequence', )

    def to_representation(self, obj):
        if isinstance(obj, MarkdownCell):
            return MarkdownCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, ImageCell):
            return ImageCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, VideoCell):
            return VideoCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, AudioCell):
            return AudioCellSerializer(obj, context=self.context).to_representation(obj)


class SheetSerializer(serializers.HyperlinkedModelSerializer):
    cell_set = CellSerializer(required=False, many=True)  # May be an anonymous user.

    class Meta:
        model = Sheet
        fields = ('title', 'cell_set')


class MarkdownCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkdownCell
        fields = ('sequence', 'text',)


class VideoCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCell
        fields = ('sequence', 'title', 'video', 'scale')


class ImageCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCell
        fields = ('sequence', 'title', 'image', 'scale')


class AudioCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioCell
        fields = ('sequence', 'title', 'audio')


class MoocCourseSerializer(serializers.HyperlinkedModelSerializer):
    week_set = CellSerializer(required=False, many=True)
    class Meta:
        model = MoocCourse
        fields = ('title', 'week_set',)


class WeekSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Week
        fields = ('title',)


class FileItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileItem
        fields = ('file',)