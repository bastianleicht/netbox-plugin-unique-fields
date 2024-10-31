from django.contrib import admin
from .models import RoleCustomField

@admin.register(RoleCustomField)
class RoleCustomFieldAdmin(admin.ModelAdmin):
    list_display = ('device_role', 'field_name', 'field_type', 'field_default')
    search_fields = ('device_role__name', 'field_name')
