from usersapp.views import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('data', UserViewset)
