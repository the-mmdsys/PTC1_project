from rest_framework import serializers
from .models import Project, Category, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image', 'is_active')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'active_status',
            'logo',
            'order',
        )


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'cover_image',
            'category_name',
            'created_by',
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 
            'title', 
            'slug', 
            'category', 
            'description', 
            'cover_image', 
            'images', 
            'created_by'
        ]