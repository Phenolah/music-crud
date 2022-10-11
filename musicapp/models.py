from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
class Song(models.Model):
    tittle = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField(primary_key = True)
class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.IntegerField(primary_key = True)