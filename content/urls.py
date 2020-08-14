from django.urls import path
from .views import ContentVideoView, ContentImageView

urlpatterns = [
    path('/image',ContentImageView.as_view()),
    path('/video',ContentVideoView.as_view()),
]
