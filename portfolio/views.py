from rest_framework import generics
from .models import Category, Project
from .serializers import (
    CategorySerializer, 
    ProjectSerializer as ProjectListSerializer, 
    ProjectDetailSerializer
)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(active_status=True).order_by('order')
    serializer_class = CategorySerializer


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-id')
        category_id = self.request.GET.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'  