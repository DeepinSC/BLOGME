from rest_framework import routers
from django.conf.urls import include, url, patterns

router = routers.DefaultRouter()

app_name = 'api'

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
