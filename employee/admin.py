from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'surname', 'email', 'department', 'position', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'surname', 'email', 'user__username', 'department__name', 'position__name')
