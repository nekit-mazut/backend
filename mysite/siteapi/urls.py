from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, PageViewSet

router = DefaultRouter()
router.register(r'sites', SiteViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
