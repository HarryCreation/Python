from django.contrib import admin
from Contact.models import *
# Register your models here.



@admin.register(Employees)
class EmployeesAdminModel(admin.ModelAdmin):
    list_display = ['name', 'position', 'join_date']
    search_fields = ['name', 'position']
    
    # def has_add_permission(self, request):
    #     return super().has_add_permission()
