from django.contrib import admin
from .models import Department, Country, Employee

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass