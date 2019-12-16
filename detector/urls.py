from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from .views import BlackViewSet, WhiteViewSet

router = routers.SimpleRouter()
router.register(r'blacks', BlackViewSet)
router.register(r'whites', WhiteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]