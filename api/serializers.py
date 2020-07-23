from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from klazor.models import *


class FileItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileItem
        fields = ('id', 'type', 'name', 'file',)


class PropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposition
        fields = ('id', 'statement', 'is_true')


class DynamicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ()

    def to_representation(self, obj):
        if isinstance(obj, Sheet):
            return SheetSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, FileItem):
            return FileItemSerializer(obj, context=self.context).to_representation(obj)


class DynamicCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ()

    def to_representation(self, obj):
        if isinstance(obj, MarkdownCell):
            return MarkdownCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, ImageCell):
            return ImageCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, VideoCell):
            return VideoCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, YoutubeCell):
            return YoutubeCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, AudioCell):
            return AudioCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, FileCell):
            return FileCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, MultipleChoiceInputCell):
            return MultipleChoiceInputCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, NumericalInputCell):
            return NumericalInputCellSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, OpenEndedInputCell):
            return OpenEndedInputCellSerializer(obj, context=self.context).to_representation(obj)


class SheetSerializer(serializers.HyperlinkedModelSerializer):
    cell_set = DynamicCellSerializer(required=False, many=True)  # May be an anonymous user.

    class Meta:
        model = Sheet
        fields = ('id', 'type', 'name', 'cell_set', 'updated_at')


class CellSerializer(serializers.HyperlinkedModelSerializer):
    type = ReadOnlyField()

    class Meta:
        model = Cell
        fields = ()


class MarkdownCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = MarkdownCell
        fields = ('id', 'sequence', 'type', 'text',)


class FileCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = FileCell
        fields = ('id', 'sequence', 'type', 'title', 'url',)


class SubFolderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'name',)


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    item_set = DynamicItemSerializer(required=False, many=True)
    sub_folder_set = SubFolderSerializer(required=False, many=True)

    class Meta:
        model = Folder
        fields = ('id', 'name', 'item_set', 'sub_folder_set')


class VideoCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = VideoCell
        fields = ('id', 'sequence', 'type', 'title', 'url', 'scale')


class YoutubeCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = YoutubeCell
        fields = ('id', 'sequence', 'type', 'title', 'url', 'scale')


class ImageCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = ImageCell
        fields = ('id', 'sequence', 'type', 'title', 'url', 'scale')


class AudioCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = AudioCell
        fields = ('id', 'sequence', 'type', 'title', 'url')


class MultipleChoiceInputCellSerializer(CellSerializer):
    proposition_set = PropositionSerializer(required=False, many=True)

    class Meta(CellSerializer.Meta):
        model = MultipleChoiceInputCell
        fields = ('id', 'sequence', 'type', 'proposition_set')


class NumericalInputCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = NumericalInputCell
        fields = ('id', 'sequence', 'type', 'answer')


class OpenEndedInputCellSerializer(CellSerializer):
    class Meta(CellSerializer.Meta):
        model = OpenEndedInputCell
        fields = ('id', 'sequence', 'type', 'answer')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

