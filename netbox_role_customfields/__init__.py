from netbox.plugins import PluginConfig


class RoleCustomFieldsConfig(PluginConfig):
    name = 'netbox_role_customfields'
    verbose_name = 'Role Specific Custom Fields'
    description = 'Restrict custom fields to specific device roles'
    version = '0.1.1'
    author = 'Bastian Leicht'
    author_email = 'bl@city-pc.de'
    base_url = 'role-custom-fields'
    required_settings = []
    default_settings = {}

config = RoleCustomFieldsConfig

