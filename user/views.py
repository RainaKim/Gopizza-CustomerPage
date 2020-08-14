import json,jwt,bcrypt
import boto3

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from botocore.exceptions import  ClientError

from .models import User, UploadImage
from my_settings import S3_CONFIG,SECRET, HASH

class SignUpView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            crypted = password.decode('utf-8')
            User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = crypted,
                phone_number    = data['phone_number'],
                sex             = Sex.objects.get(name = data['sex'])
            )
            return HttpResponse(status = 200)
        except KeyError:
                return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)

class SignInView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
                    token = jwt.encode({'email' : data['email']}, SECRET,algorithm = HASH )
                    return JsonResponse({ 'Authorization' : token } , status = 200)
                
                return JsonResponse({ 'message' : 'INVALID_VALUE' } , status = 401)
            
            return JsonResponse({ 'message' : 'INVALID_USER' } , status = 400)
        
        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' } , status = 400)


class UploadView(View):
    s3_client = boto3.client(
    's3',
    aws_access_key_id = S3_CONFIG['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key = S3_CONFIG['AWS_SECRET_ACCESS_KEY'])
    def post(self,request):
        try:
            name = request.POST.get('name',None)
            image = request.FILES['filename']

            self.s3_client.upload_fileobj(image,"gopizza-image-service",image.name,
                                         ExtraArgs = {"ContentType": image.content_type})
            image_url = f"https://gopizza-image-service.s3.ap-northeast-2.amazonaws.com/{image.name}"
            UploadImage.objects.create(
                name        = name,
                image_url   = image_url
            )
            return HttpResponse(status = 200)
        
        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' },status = 400)

