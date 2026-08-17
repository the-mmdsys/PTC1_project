from django.contrib import admin
from .models import OrderRequest, ContactWithUs

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone_number', 'company_name')
    list_editable = ('status',) 

@admin.register(ContactWithUs)
class ContactWithUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'subject', 'email')
    list_editable = ('status',)