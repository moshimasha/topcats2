"""
URL configuration for topcats project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from topcatsapp.views import CreateUserView
from topcatsapp.views import LoginUserView

from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/",CreateUserView.as_view(), name="register"),
    path("api/login/", LoginUserView.as_view(), name="login"),
    path('api/', include('topcatsapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 