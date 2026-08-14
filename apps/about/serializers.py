from rest_framework import serializers
from .models import History, TeamMember


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = (
            'id', 
            'title', 
            'achievement', 
            'date'
        )


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = (
            'id', 
            'full_name', 
            'position', 
            'bio', 
            'image'
        )