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


class CourseElementSerializer(SheetSerializer):
    class Meta(SheetSerializer.Meta):
        model = CourseElement
        fields = ('sequence', 'cell_set')


class CoursePartSerializer(serializers.ModelSerializer):
    courseelement_set = CourseElementSerializer(many=True)

    class Meta:
        model = CoursePart
        fields = ('level', 'sequence', 'type', 'title', 'courseelement_set', )


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', )

    def to_representation(self, obj):
        if isinstance(obj, MoocCourse):
            return MoocCourseSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, SchoolCourse):
            return SchoolCourseSerializer(obj, context=self.context).to_representation(obj)


class SchoolCourseSerializer(serializers.ModelSerializer):
    coursepart_set = CoursePartSerializer(many=True)
    topic_set = TopicSerializer(many=True)

    class Meta:
        model = SchoolCourse
        fields = ('title', 'topic_set', 'coursepart_set', 'year', 'semester', )


class MoocCourseSerializer(serializers.ModelSerializer):
    coursepart_set = CoursePartSerializer(many=True)
    topic_set = TopicSerializer(many=True)

    class Meta:
        model = MoocCourse
        fields = ('title', 'topic_set', 'coursepart_set', )


class FileItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileItem
        fields = ('file',)