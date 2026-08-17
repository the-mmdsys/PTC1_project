from rest_framework import serializers
from core.serializers import DynamicFieldsModelSerializer
from about.models import History, TeamMember

class HistorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = History
        fields = (
            'id', 
            'title', 
            'achievement', 
            'date',
            'created_at', 
        )


class TeamMemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TeamMember
        fields = (
            'id', 
            'full_name', 
            'position', 
            'bio', 
            'image',
            'created_at',
        )