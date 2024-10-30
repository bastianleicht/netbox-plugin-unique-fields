from rest_framework import serializers
from ..models import RoleCustomFieldMapping


class RoleCustomFieldMappingSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_role_custom_fields-api:rolecustomfieldmapping-detail'
    )

    class Meta:
        model = RoleCustomFieldMapping
        fields = ['id', 'url', 'custom_field', 'device_role', 'description']