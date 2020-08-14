

DATABASES = {
    'default' : {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'gopizza',
        'USER': 'root',
        'PASSWORD': 'gopizza123',
        'HOST': 'gopizza.corduok34h8j.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

SECRET = {
        'SECRET_KEY':'8qwsp8muj8-dh97h3ret7*@r_(n6)j0nony%pyb+rt8(^u(g%r'
}

HASH = { 'algorithm' : 'HS256'}

S3_CONFIG = {
    'AWS_ACCESS_KEY_ID': 'AKIAVYJUUPWYMUFXA5FT',
    'AWS_SECRET_ACCESS_KEY': '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',
    'S3_BUCKET_NAME': 'gopizza-image-service'
}

