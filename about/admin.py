from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

from .models import History, TeamMember

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ('title', 'year','order', 'created_at')
    list_editable = ('order',)  
    search_fields = ('title', 'year')
    list_filter = ('year', 'created_at', 'order')

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'position', 'created_at')
    search_fields = ('full_name', 'position', 'bio')
    list_filter = ('created_at',)