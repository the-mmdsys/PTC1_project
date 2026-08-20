from ..models import History, TeamMember

def get_history_list():
    return History.objects.all().order_by('year')

def get_team_members():
    return TeamMember.objects.all().order_by('full_name')