from rest_framework.viewsets import ModelViewSet
from ..models import RoleCustomFieldMapping
from . import serializers

class RoleCustomFieldMappingViewSet(ModelViewSet):
    queryset = RoleCustomFieldMapping.objects.all()
    serializer_class = serializers.RoleCustomFieldMappingSerializer