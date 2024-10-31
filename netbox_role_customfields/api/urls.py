from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('mappings', views.RoleCustomFieldMappingViewSet)

urlpatterns = router.urls