from django.db import models
from netbox.models import CustomField
from dcim.models import DeviceRole


class RoleCustomFieldMapping(models.Model):
    """Map custom fields to specific device roles"""
    custom_field = models.ForeignKey(
        to=CustomField,
        on_delete=models.CASCADE,
        related_name='role_mappings'
    )
    device_role = models.ForeignKey(
        to=DeviceRole,
        on_delete=models.CASCADE,
        related_name='custom_field_mappings'
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        unique_together = ['custom_field', 'device_role']
        ordering = ['custom_field', 'device_role']
        verbose_name = 'Role Custom Field Mapping'
        verbose_name_plural = 'Role Custom Field Mappings'