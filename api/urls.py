from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('users', ProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))  # Corrected this line
]
