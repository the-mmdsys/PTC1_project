from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import History, TeamMember

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    # از فیلدهای واقعی date و title که در مدلت نوشتی استفاده کردیم
    list_display = ('title', 'date')
    search_fields = ('title', 'achievement')
    list_filter = ('date',)

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    # از فیلدهای واقعی full_name و position استفاده کردیم
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position', 'bio')