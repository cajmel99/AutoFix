from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MechanicServiceViewSet, PublicServiceListViewSet

router = DefaultRouter()
router.register(r'mechanic/services', MechanicServiceViewSet, basename='mechanic-services')
router.register(r'services', PublicServiceListViewSet, basename='public-services')

urlpatterns = [
    path('', include(router.urls)),
]
