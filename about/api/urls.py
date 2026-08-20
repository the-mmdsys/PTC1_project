from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoryViewSet, TeamMemberViewSet

app_name = 'about'

router = DefaultRouter()
router.register(r'history', HistoryViewSet, basename='history')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')

urlpatterns = [
    path('', include(router.urls)),
]