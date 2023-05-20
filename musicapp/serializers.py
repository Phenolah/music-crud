from .models import Artiste, Song, Lyric
from rest_framework import serializers
#from datetime import datetime


#serializing models
class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiste
        fields=(
        "id",
        "first_name",
         "last_name",
         "Age",
        )

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields=(
        "title",
         "date_released",
        )

class LyricSerializer(serializers.HyperlinkedModelSerializer):
    # song_id = SongSerializer
    class Meta:
        model = Lyric
        fields=(
        "content",
        "song_id",
        )
        