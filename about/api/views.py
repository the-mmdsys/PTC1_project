from rest_framework import viewsets
from .serializers import HistorySerializer, TeamMemberSerializer
from about.api import selectors

class HistoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']  
    serializer_class = HistorySerializer

    def get_queryset(self):
        return selectors.get_history_list()


class TeamMemberViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = TeamMemberSerializer

    def get_queryset(self):
        return selectors.get_team_members()