from django.contrib import admin

from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'hire_date')
  list_display_links = ('id', 'first_name', 'last_name')
  search_fields = ('first_name', 'last_name', 'email')
  list_per_page = 25