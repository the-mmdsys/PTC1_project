from modeltranslation.translator import register, TranslationOptions
from .models import Article, Comment

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'category', 'content', 'description', 'summary')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'text')
            