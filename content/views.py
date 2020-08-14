import json,jwt,bcrypt
import boto3

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from botocore.exceptions import  ClientError

from .models import Video, Image
from my_settings import S3_CONFIG,SECRET, HASH

class ContentImageView(View):
    def get(self,request):
        try:
            images = Image.objects.all()
            insta_images = Image.objects.all()[:21]
            insta = [insta_image.image_url for insta_image in insta_images]
            data = {
                'instagram-menu': insta,
                'asian-seafood' : images[21].image_url,
                'bacon-potato'  : images[22].image_url,
                'pasta-poster'  : images[23].image_url,
                'poster1'       : images[24].image_url
            }
            return JsonResponse({ 'data': data }, status = 200)
        
        except KeyError:
            return JsonResponse({ 'message': 'INVALID_KEYS' }, status = 400)

class ContentVideoView(View):
    def get(self,request):
        try:
            videos = list(Video.objects.values())
            return JsonResponse({ 'data' : videos },status = 200)
        
        except KeyError:
            return JsonResponse({ 'message': 'INVALID_KEYS' }, status = 400)
