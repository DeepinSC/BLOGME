from rest_framework import routers
from django.conf.urls import include, url

router = routers.DefaultRouter()

urlpatterns = url(
    'api',
    url(r'^', include(router.urls)),

)
