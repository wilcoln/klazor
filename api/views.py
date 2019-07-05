from rest_framework import viewsets
from api.serializers import *
# Create your views here.


class SheetViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class CellViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class MoocCourseViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = MoocCourse.objects.all()
    serializer_class = MoocCourseSerializer


class WeekViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class FileItemViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = FileItem.objects.all()
    serializer_class = FileItemSerializer