"""django_api_rest_snowflake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from django.urls import path, include
from rest_framework import routers
from employees.views import DepartmentsAPIView, UploadAPIView

departments_router = routers.SimpleRouter()
departments_router.register(
    r'departments',
    DepartmentsAPIView,
    basename='departments',
)

upload_router = routers.DefaultRouter()
upload_router.register(r'upload', UploadAPIView, basename="upload")

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/departments/', DepartmentsAPIView.as_view()),
    path('api/upload/', UploadAPIView.as_view()),
]
