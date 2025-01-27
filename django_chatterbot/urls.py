"""django_chatterbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers

from django_chatterbot import views
from django_chatterbot.api import ChatterBotView
from django_chatterbot.api import AudioView
from django_chatterbot.views import ChatterBotAppView

router = routers.DefaultRouter()

urlpatterns = [
    re_path(r'^$', ChatterBotAppView.as_view()),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api/chatterbot/', ChatterBotView.as_view(), name='chatterbot'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('audio/', AudioView.as_view(), name='audio_view'),
]
