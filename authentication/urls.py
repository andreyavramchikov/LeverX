from django.conf.urls import url, include
from rest_framework import routers

from .views import AccountViewSet


router = routers.SimpleRouter()
router.register(r'register', AccountViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls), name='register'),
]