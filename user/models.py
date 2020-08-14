from django.db import models

class User(models.Model):
    name            = models.CharField(max_length = 45)
    email           = models.EmailField(max_length = 200)
    phone_number    = models.CharField(max_length = 45)
    sex = models.ForeignKey('Sex', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'users'

class Sex(models.Model):
    name            = models.CharField(max_length = 45)

    class Meta:
        db_table = 'sexes'

class UploadImage(models.Model):
    name        = models.CharField(max_length = 45)
    image_url   = models.URLField(max_length = 3000)
    created_at  = models.DateTimeField(auto_now_add = True)
    user        = models.ForeignKey('User', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'upload_images'
