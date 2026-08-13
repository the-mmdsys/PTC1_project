from django.contrib import admin
from .models import OrderRequest, ContactWithUs

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'is_reviewed', 'created_at')
    list_filter = ('is_reviewed', 'created_at')
    search_fields = ('full_name', 'phone_number', 'company_name')
    list_editable = ('is_reviewed',) 

@admin.register(ContactWithUs)
class ContactWithUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('full_name', 'subject', 'email')
    list_editable = ('is_read',)  