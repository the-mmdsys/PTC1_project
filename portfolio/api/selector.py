from ..models import Category, Project
from core.enums import ActiveStatus

def get_active_categories():
    return Category.objects.filter(active_status=ActiveStatus.ACTIVE)

def get_project_list(*, category_id=None):
    queryset = Project.objects.all().order_by('-created_at')
    
    if category_id:
        queryset = queryset.filter(category_id=category_id)
        
    return queryset