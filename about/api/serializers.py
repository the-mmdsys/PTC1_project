from core.serializers import DynamicFieldsModelSerializer
from about.models import History, TeamMember

class HistorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = History
        fields = (
            'id', 
            'title', 
            'achievement', 
            'year',
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