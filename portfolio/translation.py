from modeltranslation.translator import register, TranslationOptions
from .models import Category, Project
from modeltranslation.translator import translator, TranslationOptions
from about.models import History, TeamMember


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'achievement') 
translator.register(History, HistoryTranslationOptions)

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'bio') 

translator.register(TeamMember, TeamMemberTranslationOptions)