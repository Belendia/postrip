from django.contrib import admin
from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip_id')


admin.site.register(Trip, TripAdmin)
