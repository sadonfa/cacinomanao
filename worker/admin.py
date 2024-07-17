from django.contrib import admin
from .models import Worker

# Register your models here.

@admin.register(Worker)
class TableAdmin(admin.ModelAdmin):
    list_display = ('dni', 'name', 'last_name', 'contratista')
    