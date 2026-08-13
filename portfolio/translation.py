from modeltranslation.translator import register, TranslationOptions
from .models import Category, Project

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')