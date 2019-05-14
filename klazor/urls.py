"""Klazor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from klazor.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('welcome/', welcome),
    path('mooc_courses/<int:id>/', view_mooc_course, name='mooc-course'),
    path('school_courses/<int:id>/', view_school_course, name='school-course'),
    path('add_course/', add_course),
    path('add_instructor/', add_instructor),
    path('save_course/', save_course),
    path('save_instructor/', save_instructor)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
