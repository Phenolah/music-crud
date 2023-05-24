# from django.http import HttpResponse

# # Create your views here.

# def index(request):
#     return HttpResponse("Hello, Welcome to my Music App!!!, Do have a wonderful time!!!")


from rest_framework import generics
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer


# Define your views here

class SongList(generics.ListCreateAPIView):
    """
    API endpoint that allows the listing and creation of songs.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows the retrieval, update, and deletion of a specific song.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtisteList(generics.ListCreateAPIView):
    """
    API endpoint that allows the listing and creation of artistes.
    """
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows the retrieval, update, and deletion of a specific artiste.
    """
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class LyricList(generics.ListCreateAPIView):
    """
    API endpoint that allows the listing and creation of lyrics.
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

class LyricDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows the retrieval, update, and deletion of a specific lyric.
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
