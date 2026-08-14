from rest_framework import generics
from .models import History, TeamMember
from .serializers import HistorySerializer, TeamMemberSerializer

class HistoryListView(generics.ListAPIView):
    queryset = History.objects.all().order_by('date')
    serializer_class = HistorySerializer


class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all().order_by('full_name')
    serializer_class = TeamMemberSerializer