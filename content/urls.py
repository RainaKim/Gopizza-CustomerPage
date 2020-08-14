from django.urls import path
from .views import ContentVideoView, ContentImageView

urlpatterns = [
    path('/image',ContentImageView.as_view()),
    path('/vidoe',ContentVideoView.as_view()),
]
