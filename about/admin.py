from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import History, TeamMember

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'achievement')
    list_filter = ('date', 'created_at')

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'position', 'created_at')
    search_fields = ('full_name', 'position', 'bio')
    list_filter = ('created_at',)