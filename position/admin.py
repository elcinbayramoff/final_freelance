from django.contrib import admin
from .models import Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'department', 'created_at', 'updated_at')
    search_fields = ('name', 'department__name')
