from rest_framework import serializers
from klazor.models import *


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ('id', 'sequence', )

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
        fields = ('id', 'title', 'cell_set')


class MarkdownCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkdownCell
        fields = ('id', 'sequence', 'text',)


class VideoCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCell
        fields = ('id', 'sequence', 'title', 'video', 'scale')


class ImageCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCell
        fields = ('id', 'sequence', 'title', 'image', 'scale')


class AudioCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioCell
        fields = ('id', 'sequence', 'title', 'audio')


class CourseElementSerializer(SheetSerializer):
    class Meta(SheetSerializer.Meta):
        model = CourseElement
        fields = ('id', 'sequence', 'title', 'cell_set')


class CoursePartSerializer(serializers.ModelSerializer):
    courseelement_set = CourseElementSerializer(many=True)

    class Meta:
        model = CoursePart
        fields = ('id', 'level', 'sequence', 'label', 'title', 'courseelement_set', )


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'title', 'subtopic_set')


class CourseSerializer(serializers.ModelSerializer):
    # Add resources_set and instructors_set
    class Meta:
        model = Course
        fields = ('id', 'title', )

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
        fields = ('id', 'title', 'topic_set', 'coursepart_set', 'year', 'semester', )


class MoocCourseSerializer(serializers.ModelSerializer):
    coursepart_set = CoursePartSerializer(many=True)
    topic_set = TopicSerializer(many=True)

    class Meta:
        model = MoocCourse
        fields = ('id', 'title', 'topic_set', 'coursepart_set', )


class FileItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileItem
        fields = ('id', 'file',)