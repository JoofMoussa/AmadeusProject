from django.contrib import admin
from .models import Inscription


@admin.register(Inscription)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'doctor', 'date', 'time']
    date_hierarchy = ('date')
    list_filter = ['date', 'doctor', ]
    list_per_page = 20
    search_fields = ['doctor', 'name', ]
