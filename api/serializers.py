from rest_framework import serializers
from klazor.models import *


class SheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sheet
        fields = ('title', )