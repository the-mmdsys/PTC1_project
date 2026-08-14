from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'slug',
            'title',
            'cover_image',
            'description',
            'summary',
        )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'full_name',
            'text',
            'created_at',
        )


class ArticleDetailSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'title',
            'cover_image',
            'content',
            'summary',
            'comments',
            'created_at',
            'description',
            'category',
        )


