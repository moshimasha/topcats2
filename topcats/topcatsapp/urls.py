from django.contrib import admin
from django.urls import path, include
from .views import CreateUserView
from . import views
from .views import FileUploadView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]

