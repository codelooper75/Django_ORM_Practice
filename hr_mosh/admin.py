from django.contrib import admin
from .models import Employees, Offices

# Register your models here.
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("first_name", 'last_name', 'job_title','salary','reporst_to', 'office' )
    list_display_links = ("first_name", "last_name")
    search_fields = ("first_name", 'last_name', 'job_title')
    list_filter = ('job_title','office')

@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ("address", 'city', 'state')
    list_display_links = ("address",)
    search_fields = ("address", 'city', 'state')
    list_filter = ('state',)

