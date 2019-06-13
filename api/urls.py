from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
urlpatterns = [
    url(r'^provisionSIM/', views.provisionSIM),
]

urlpatterns = format_suffix_patterns(urlpatterns)
