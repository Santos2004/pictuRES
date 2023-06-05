from django.urls import path, include
from rest_framework.routers import *
from .views import ImageViewSet

router = SimpleRouter()
router.register('images', ImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls))
]