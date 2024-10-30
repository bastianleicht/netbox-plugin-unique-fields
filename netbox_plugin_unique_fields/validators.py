from django.core.exceptions import ValidationError
from .models import RoleCustomFieldMapping


def validate_role_specific_field(instance, custom_field_data):
    """
    Validate that custom field data only contains fields mapped to the device role
    """
    if not hasattr(instance, 'device_role'):
        return

    allowed_fields = RoleCustomFieldMapping.objects.filter(
        device_role=instance.device_role
    ).values_list('custom_field__name', flat=True)

    invalid_fields = []
    for field_name in custom_field_data:
        if field_name not in allowed_fields:
            invalid_fields.append(field_name)

    if invalid_fields:
        raise ValidationError(
            f"The following custom fields are not allowed for role {instance.device_role}: {', '.join(invalid_fields)}"
        )