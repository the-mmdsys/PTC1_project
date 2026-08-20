from rest_framework import viewsets, status
from rest_framework.response import Response

from blog.api import selectors
from .serializers import ArticleSerializer, CommentSerializer
from blog.api import services

class ArticleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_queryset(self):
        return selectors.get_published()

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            kwargs['fields'] = ('id', 'title', 'slug', 'category', 'cover_image', 'description', 'summary', 'created_at')
        return ArticleSerializer(*args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = services.create_comment(
            article=serializer.validated_data['article'],
            full_name=serializer.validated_data['full_name'],
            text=serializer.validated_data['text']
        )

        result_serializer = self.get_serializer(comment)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)