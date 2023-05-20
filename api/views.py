from django.shortcuts import render
from songcrud.musicapp.models import Song
from rest_framework import viewsets
from rest_framework import permissions
from songcrud.musicapp.serializers import SongSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

