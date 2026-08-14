from django.urls import path
from .views import ArticleListView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path('article-request/',ArticleListView.as_view(), name='article-request-create'),
    path('comment-rquest/', CommentCreateView.as_view(), name='comment-request-create'),
]