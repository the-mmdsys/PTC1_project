from rest_framework import viewsets
from ..models import History, TeamMember
from .serializers import HistorySerializer, TeamMemberSerializer

class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            kwargs['fields'] = ('id', 'title', 'year') 
        
        return super().get_serializer(*args, **kwargs)


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            kwargs['fields'] = ('id', 'full_name', 'position', 'image')
            
        return super().get_serializer(*args, **kwargs)