from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExploreViewSet, SearchViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'explore', ExploreViewSet, basename='explore')
router.register(r'search', SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
