from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Project, ProjectImage
from django.utils.html import format_html

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'active_status', 'order')
    list_editable = ('active_status', 'order') 
    list_filter = ('active_status',)
    search_fields = ('title',)
    list_per_page = 20

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('title', 'slug',  'category', 'created_by')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    raw_id_fields = ('category', 'created_by',)
    prepopulated_fields = {'slug': ('title',)} 
    inlines = [ProjectImageInline] 


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image_thumbnail', 'is_active') 
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    
    image_thumbnail.short_description = 'Thumbnail'
   
    