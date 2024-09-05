from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_establishments, name='all_establishments'),
]
