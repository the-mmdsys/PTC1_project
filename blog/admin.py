from django.contrib import admin
from .models import Article, Comment, Category
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'language', 'status', 'created_at')
    list_filter = ('language', 'status', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'article', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'text')
    list_editable = ('status',)
    list_per_page = 20
