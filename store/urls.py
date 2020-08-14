from django.urls import path
from .views import StoreListView, RegisterStoreView

urlpatterns = [
    path('', StoreListView.as_view()),
    path('/register', RegisterStoreView.as_view())
]
