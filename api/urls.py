from rest_framework import routers
from django.urls import path, include

from data.views import BaseAgreementViewSet, EndOfTermViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('report', BaseAgreementViewSet, basename='report')
router.register('endofterm', EndOfTermViewSet, basename='endofterm')

urlpatterns = [
    path('', include(router.urls)),
]