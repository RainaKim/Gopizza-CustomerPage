from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Store(models.Model):
    name                = models.CharField(max_length = 50)
    tel                 = models.CharField(max_length = 50, null = True)
    lat                 = models.FloatField(null = True)
    lng                 = models.FloatField(null = True)
    location            = models.PointField(null = True, srid = 4326)
    code                = models.CharField(max_length = 20)
    country             = models.ForeignKey('Country',on_delete = models.SET_NULL, null = True)
    city                = models.ForeignKey('City', on_delete = models.SET_NULL, null = True)
    district            = models.ForeignKey('District', on_delete = models.SET_NULL, null = True)
    address1            = models.CharField(max_length = 100)
    address2            = models.CharField(max_length = 100)
    open_time           = models.TimeField(null = True)
    close_time          = models.TimeField(null = True)
    business_district   = models.ForeignKey('BusinessDistrict', on_delete = models.SET_NULL, null = True)
    objects             = GeoManager()

    class Meta:
        db_table = 'stores'

class Country(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'countries'

class City(models.Model):
    name        = models.CharField(max_length = 50)
    country     = models.ForeignKey('Country', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'cities'

class District(models.Model):
    name    = models.CharField(max_length = 50)
    country = models.ForeignKey('Country', on_delete = models.SET_NULL, null = True)
    city    = models.ForeignKey('City', on_delete = models.SET_NULL, null = True)
    
    class Meta:
        db_table = 'districts'

class StoreImage(models.Model):
    image_url   = models.URLField(max_length = 3000, default = f"https://gopizza-store-images.s3.ap-northeast-2.amazonaws.com/default.png")
    store       = models.ForeignKey('Store',on_delete = models.SET_NULL, null = True) 
    name        = models.CharField(max_length = 50,null=True)
    
    class Meta:
        db_table = 'store_images'

class BusinessDistrict(models.Model):
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'business_districts'

class RecommendedLocation(models.Model):
    location    = models.PointField(null = True)
    lat         = models.FloatField(null = True)
    lng         = models.FloatField(null = True)
    address     = models.CharField(max_length = 250, null = True)
    country     = models.ForeignKey('Country', on_delete = models.SET_NULL, null = True)
    city        = models.ForeignKey('City', on_delete = models.SET_NULL, null = True)
    objects     = GeoManager()

    class Meta:
        db_table = 'recommended_locations'



