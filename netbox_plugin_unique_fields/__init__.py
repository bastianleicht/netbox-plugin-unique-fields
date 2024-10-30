from extras.plugins import PluginConfig


class RoleCustomFieldsConfig(PluginConfig):
    name = 'netbox_role_custom_fields'
    verbose_name = 'Role Specific Custom Fields'
    description = 'Restrict custom fields to specific device roles'
    version = '0.1.1'
    author = 'Bastian Leicht'
    author_email = 'bl@city-pc.de'
    base_url = 'role-custom-fields'
    required_settings = []
    default_settings = {}

    def ready(self):
        super().ready()
        from . import signals

        # Register custom validators
        from extras.models import CustomField
        from .validators import validate_role_specific_field
        CustomField.validators.append(validate_role_specific_field)
