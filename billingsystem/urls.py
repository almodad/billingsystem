"""billingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets, urls
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/',include('rest_framework.urls')),
    url(r'', views.provisionSIM),
    url(r'^provisionSIM/', views.provisionSIM),
    url(r'^activateSIM/', views.activateSIM),
    url(r'^querySubscriberInfo/', views.querySubscriberInfo),
    url(r'^adjustAccountBalance/', views.adjustAccountBalance),
]

urlpatterns = format_suffix_patterns(urlpatterns)

