from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'article', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'text')
    list_editable = ('status',)  