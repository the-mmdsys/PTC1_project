from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import History, TeamMember

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'achievement')
    list_filter = ('date',)

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position', 'bio')