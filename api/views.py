from rest_framework import viewsets# , permissions
from api.serializers import *
from api.permissions import *
# Create your views here.


class TagViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows topics to be viewed or edited.
        """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class FolderViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows folders to be viewed or edited.
        """
    queryset = Folder.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = FolderSerializer

    def get_queryset(self):
        return Folder.objects.all().filter(owner=self.request.user)


class SheetViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows sheets to be viewed or edited.
        """
    permission_classes = [permissions.IsAuthenticated,
                          IsOwner]
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def get_queryset(self):
        return Sheet.objects.all().filter(owner=self.request.user)


class CellViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cells to be viewed or edited.
        """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cell.objects.all()
    serializer_class = DynamicCellSerializer


class FileItemViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows file items to be viewed or edited.
        """
    permission_classes = [permissions.IsAuthenticated,
                          IsOwner]
    queryset = FileItem.objects.all()
    serializer_class = FileItemSerializer
