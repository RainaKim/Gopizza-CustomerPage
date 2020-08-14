from django.db import models

class Video(models.Model):
    name        = models.CharField(max_length = 50)
    video_url   = models.URLField(max_length = 3000)

    class Meta:
        db_table = 'videos'

class Image(models.Model):
    name        = models.CharField(max_length = 50)
    image_url   = models.URLField(max_length = 3000)

    class Meta:
        db_table = 'images'
