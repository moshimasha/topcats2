from django.contrib import admin
from django.urls import path, include
from .views import CreateUserView
from . import views
from .views import FileUploadView
from .views import LearnView
from .views import LoadView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('library/', LoadView.as_view(), name='library'),
    path('learn/', LearnView.as_view(), name='library'),
]

