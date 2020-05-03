from userAccountApi.viewsets import UserAccountViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserAccountViewset)