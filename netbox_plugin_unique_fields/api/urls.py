from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('mappings', views.RoleCustomFieldMappingViewSet)

urlpatterns = router.urls

# netbox_role_custom_fields/api/views.py
from rest_framework.viewsets import ModelViewSet
from ..models import RoleCustomFieldMapping
from . import serializers

class RoleCustomFieldMappingViewSet(ModelViewSet):
    queryset = RoleCustomFieldMapping.objects.all()
    serializer_class = serializers.RoleCustomFieldMappingSerializer