from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Menu, Booking

admin.site.register(Menu)
admin.site.register(Booking)
