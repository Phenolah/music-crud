from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from musicapp.models import Artiste, Lyric, Song
from musicapp.serializers import UserSerializer, SongSerializer, LyricSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Define your views here

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Artiste.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('-date_released')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

class LyricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lyrics to be viewed or edited.
    """
    queryset = Lyric.objects.all().order_by('-song_id')
    serializer_class = LyricSerializer
    permission_classes = [permissions.IsAuthenticated]


