from rest_framework import serializers
from core.serializers import DynamicFieldsModelSerializer
from portfolio.models import Project, Category, ProjectImage

class CategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'active_status', 'logo', 'order')

class ProjectImageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image', 'is_active')

class ProjectSerializer(DynamicFieldsModelSerializer):
    category = CategorySerializer(read_only=True, fields=('id', 'title'))
    images = ProjectImageSerializer(many=True, read_only=True, fields=('id', 'image'))

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'cover_image',
            'category',
            'images',
            'created_by',
            'created_at',  
        )