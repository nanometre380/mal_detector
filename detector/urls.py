from django.urls import include
from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlackViewSet, WhiteViewSet

# router = routers.SimpleRouter()
# router.register(r'blacks', BlackViewSet)
# router.register(r'whites', WhiteViewSet)

black_list = BlackViewSet.as_view({
    'get' : 'list'
})

black_url = BlackViewSet.as_view({
    'get' : 'retrieve',
})

white_list = WhiteViewSet.as_view({
    'get' : 'list',
})

white_url = WhiteViewSet.as_view({
    'get' : 'retrieve',
})

urlpatterns = format_suffix_patterns([
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('blacks/', black_list, name='black_list'),
    path('blacks/<path:url>/', black_url, name='black_url'),   
    path('whites/', white_list, name='white_list'),
    path('whites/<path:url>/', white_url, name='white_url'),
    # url(r'^', include(router.urls)),
])

urlpatterns+=[
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]