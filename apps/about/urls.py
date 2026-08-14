from django.urls import path
from .views import HistoryListView, TeamMemberListView

app_name = 'about'

urlpatterns = [
    path('history/', HistoryListView.as_view(), name='history-list'),
    path('team/', TeamMemberListView.as_view(), name='team-member-list'),
]

