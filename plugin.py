from extras.plugins import PluginConfig

class NetBoxRoleCustomFieldsConfig(PluginConfig):
    name = 'netbox_role_customfields'
    verbose_name = 'NetBox Role Custom Fields'
    description = 'Custom Fields based on device roles in NetBox'
    version = '1.0'
    author = 'Your Name'
    base_url = 'netbox-role-customfields'

config = NetBoxRoleCustomFieldsConfig