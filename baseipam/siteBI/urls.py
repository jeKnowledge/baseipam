from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path(r'', views.noLanguage),
    path(r'<language>/', views.index),
    path(r'<language>/about', views.about),
    path(r'<language>/home', views.index),
    path(r'<language>/services', views.services),
]
