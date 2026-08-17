from rest_framework import viewsets
from .serializers import CategorySerializer, ProjectSerializer
from portfolio.api import selector

class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CategorySerializer

    def get_queryset(self):
        return selector.get_active_categories()


class ProjectViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        return selector.get_project_list(category_id=category_id)

    # AI 
    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            kwargs['fields'] = ('id', 'title', 'slug', 'cover_image', 'category')
        
        return ProjectSerializer(*args, **kwargs)