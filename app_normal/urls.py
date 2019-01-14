from django.contrib import admin
from django.urls import path, include
from app_normal.views import normal_app

app_name = 'app_normal'

urlpatterns = [
    path('', normal_app, name='index')
]
