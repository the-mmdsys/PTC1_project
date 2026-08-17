from rest_framework import serializers
from core.serializers import DynamicFieldsModelSerializer
from blog.models import Article, Comment
from blog.api import selectors


class CommentSerializer(DynamicFieldsModelSerializer):
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), 
        source='article', 
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'article_id', 'full_name', 'text', 'status', 'created_at')
        read_only_fields = ('id', 'status', 'created_at')


class ArticleSerializer(DynamicFieldsModelSerializer):
    approved_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id', 'slug', 'title', 'category', 'cover_image',
            'description', 'summary', 'content', 'status',
            'approved_comments', 'created_at'
        )

    def get_approved_comments(self, obj):
        comments = selectors.get_comments(obj)
        return CommentSerializer(comments, many=True, fields=('id', 'full_name', 'text', 'created_at')).data