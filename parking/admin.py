from django.contrib import admin

# Register your models here.
from .models import Commercial_Establishment, Vehicle

admin.site.register(Commercial_Establishment)
admin.site.register(Vehicle)
