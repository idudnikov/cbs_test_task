from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, OrganizationViewSet

app_name = "api"

router = DefaultRouter()

router.register('events', EventViewSet, basename='events')
router.register('organizations', OrganizationViewSet, basename='organizations')


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path('auth/', include('djoser.urls.jwt')),
]
