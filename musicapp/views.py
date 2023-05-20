# from django.http import HttpResponse

# # Create your views here.

# def index(request):
#     return HttpResponse("Hello, Welcome to my Music App!!!, Do have a wonderful time!!!")


from rest_framework import generics

from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class LyricList(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

class LyricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer