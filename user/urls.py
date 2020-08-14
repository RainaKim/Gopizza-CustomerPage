from django.urls import path
from .views import UploadView, SignUpView, SignInView

urlpatterns = [
    path('/upload',UploadView.as_view()),
    path('/sign-up',SignUpView.as_view()),
    path('/sign-in',SignInView.as_view()),
]
