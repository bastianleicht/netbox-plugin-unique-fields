from django.db import models
from dcim.models import DeviceRole

class RoleCustomField(models.Model):
    FIELD_TYPE_CHOICES = [
        ('string', 'String'),
        ('integer', 'Integer'),
        ('boolean', 'Boolean'),
    ]

    device_role = models.ForeignKey(DeviceRole, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50, unique=True)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)
    field_default = models.TextField(null=True, blank=True, help_text="Default value for the custom field")

    def __str__(self):
        return f"{self.field_name} ({self.field_type}) for role {self.device_role.name}"
