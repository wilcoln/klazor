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


class CourseViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursePartViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = CoursePart.objects.all()
    serializer_class = CoursePartSerializer


class FileItemViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    queryset = FileItem.objects.all()
    serializer_class = FileItemSerializer