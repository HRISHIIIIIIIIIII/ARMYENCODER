# app58/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.encode_message, name='encode_message'),
]
