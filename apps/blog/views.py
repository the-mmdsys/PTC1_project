from rest_framework import generics
from .models import Article, Comment
from .serializers import (
    ArticleListSerializer, 
    ArticleDetailSerializer, 
    CommentListSerializer  
)

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleListSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'  


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    
    def perform_create(self, serializer):
        article_id = self.kwargs.get('article_id')
        serializer.save(article_id=article_id) 