from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_establishments, name='all_establishments'),
    path('<int:id>', views.get_establishment_by_id,
         name='get_establishment_by_id'),
]
