import os
import django
import sys

from django.shortcuts import render
from django.views import View
os.environ.setdefault('DJANGO_SETTINGS_MODULE','gopizza.settings')
django.setup()

from content.models import Image, Video


def createInstaImage():
    bucket_name = "gopizza-main-content"
    quantity =21
    for i in range(1,quantity+1):
        image_name  = "instagram-menu/"+str(i)+".png"
        image_url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{image_name}"
        Image.objects.create(
            name = image_name,
            image_url = image_url
        )

def createImage():
    bucket_name = "gopizza-main-content"
    for i in ranage(quantity):
        image_name  = "content-image-"+i+".png"
    names = ['asian-seafood.psd','bacon-potato.psd','pasta-poster.jpg','poster1.ai']

    for name in names:
        image_name  = name
        image_url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{image_name}"
        Image.objects.create(
            name = image_name,
            image_url = image_url
        )

def createVideo():
    bucket_name = "gopizza-main-video"
    quantity = 0
    for i in ranage(quantity):
        video_name  = "content-video-" + i + ".png"
    for i in range(quantity):
        video_name  = i + ".png"
        video_url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{video_name}"
        Video.objects.create(
            name = video_name,
            video_url = video_url
        )

def createStore():
    bucket_name = "gopizza-store-images"
    store_quantity = 0
    for i in range(store_quantity):
        for j in range(image_quantity):
            image_name = "store-image-" + i + "-" + j + ".png"
            image_url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{image_name}"
            StoreImage.objects.create(
                name = image_name,
                image_url = image_url
                store_id = i
            )
