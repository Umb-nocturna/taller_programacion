from django.urls import path, include
from rest_framework import routers
from .views import FriendViewSet

router = routers.DefaultRouter()
router.register(r'friends', FriendViewSet)

urlpatterns = [
    path('', include(router.urls))
]