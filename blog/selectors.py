from .models import Article
from core.enums import ArticleStatus, CommentStatus

def get_published():
    return Article.objects.filter(status=ArticleStatus.PUBLISHED).order_by('-created_at')

def get_comments(article):
    return article.comments.filter(status=CommentStatus.APPROVED).order_by('created_at')