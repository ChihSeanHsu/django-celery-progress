from django.contrib import admin
from django.urls import path, include
from app_ajax.views import ajax_app, get_ajax

app_name = 'app_ajax'

urlpatterns = [
    path('', ajax_app, name='index'),
    path('ajax', get_ajax, name='ajax'),
]
