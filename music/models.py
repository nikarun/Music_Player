from django.db import models

class Album(models.Model):
    name=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    image=models.ImageField(max_length=1200,null=True)

    def __str__(self):
        return self.name



class Song(models.Model):
    title = models.CharField(max_length=50)
   # artist = models.CharField(max_length=50, null=True,blank=True)
   # lyricists=models.CharField(max_length=50, null=True,blank=True)
   # image = models.CharField(max_length=1200, null=True,blank=True)
   # song_url=models.CharField(max_length=1200, null=True,blank=True)
    file=models.FileField(null=True,blank=True)
    album_id=models.ForeignKey(Album,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

