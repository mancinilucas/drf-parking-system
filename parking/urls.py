from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('establishments/', views.get_establishments, name='get_establishments'),
    path('establishments/<int:id>', views.establishment_manager,
         name='establishment_manager'),
    path('vehicles/', views.get_vehicles, name='get_vehicles'),
    path('vehicles/<int:id>', views.vehicle_manager,
         name='establishment_manager'),
]
