from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_establishments, name='get_establishments'),
    path('<int:id>', views.establishment_manager,
         name='establishment_manager'),
]
